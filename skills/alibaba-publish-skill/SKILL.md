---
name: alibaba-publish-skill
description: 阿里国际站智能发品/搬品工具。当用户提到“发品”、“搬品”、“上传商品”、“1688同步”、“采集上传”或提供 1688/淘宝/天猫/速卖通/亚马逊链接时，必须使用此技能。即便用户只是发了一个链接没有说明意图，也应触发此技能进行环境检查和引导。
---

# 阿里国际站发品 SKILL (v2.1)

本文件描述阿里国际站 URL 发品的可执行规范。

## 1. 核心原则与子代理执行规范

### 1.1 核心原则
- **接口优先**：直接调用后端 API，不要操作页面 UI，除非接口失效。
- **数据完整性 (至关重要)**：严禁在更新商品（如 `submitDraft.json`）时仅提交部分字段。该接口为全量覆盖逻辑，遗漏字段会导致商品数据（图片、属性、描述等）被清空。必须遵循“先全量查询、修改特定字段、全量提交”的流程。
- **子代理上下文同步 (关键)**：当使用 `sessions_spawn` 派生 `browser` 子代理时，父代理**必须**将本 Skill 中的 JS 代码模板、Token 逻辑和 Payload 结构完整写入 `task` 参数中。子代理无法自动感知 Skill 文件。
- **健壮性封装**：所有浏览器控制台脚本必须包裹在 `(async () => { ... })()` 中，严禁直接使用顶层 `await`，以兼容所有浏览器环境。

## 2. 环境与安全校验

### 2.1 登录与 CSRF Token
- **目标域名**：`https://post.alibaba.com`
- **Token 提取**：必须从 `window.csrfToken.tokenValue` 提取并在 Header 的 `X-XSRF-TOKEN` 中发送。
- **登录态轮询**：若未登录，引导至 `https://login.alibaba.com/newlogin/icbuLogin.htm`，并每 5 秒轮询一次。

## 3. 核心功能流程

### 3.1 资源预检 (Pre-check)
在触发任务前，必须调用预检接口确认配额：
- **接口**：`GET https://post.alibaba.com/product/batchEasyListing/batchPreCheck.json?transType=IMAGE_TRANSLATION_MAIN_6_DETAIL_30&totalCount=1`
- **错误转译**：
    - `BUDGET_LIMIT` -> **AI点数不足**，建议充值或减少翻译量。
    - `PHOTO_BANK_FULL` -> **图片银行空间不足**。
    - `DRAFT_FULL` -> **草稿箱已满**。

### 3.2 搬品任务触发与完整脚本模板
在 `browser` 工具的 `console` 中执行以下脚本（确保一次性执行，不要分步调试）：

```javascript
(async () => {
  const PRODUCT_URL = "用户提供的URL";
  const result = { steps: [] };
  try {
    const csrfToken = window.csrfToken?.tokenValue;
    if (!csrfToken) return "[Result] " + JSON.stringify({ status: "failed", reason: "CSRF Token Missing" });

    // 1. 预检
    const preCheckRes = await fetch("https://post.alibaba.com/product/batchEasyListing/batchPreCheck.json?transType=IMAGE_TRANSLATION_MAIN_6_DETAIL_30&totalCount=1");
    const preCheck = await preCheckRes.json();
    if (!preCheck.data.checkResult) return "[Result] " + JSON.stringify({ status: "failed", reason: "PRE_CHECK_FAILED", details: preCheck.data });

    // 2. 触发 (注意 jsonBody 嵌套)
    const payload = {
      jsonBody: {
        scene: "agentAccioWorkPublish",
        subScene: "multiUrlProduct",
        urlList: [PRODUCT_URL],
        imageTransType: "IMAGE_TRANSLATION_MAIN_6_DETAIL_30",
        publishCondition: { needPublish: true, qualityScore: "4.5", imgStrategy: "onlyMainExtractionStrategies" }
      }
    };

    const startRes = await fetch("https://post.alibaba.com/product/batchEasyListing/batchProductGenerateStart.json", {
      method: "POST",
      headers: { "Content-Type": "application/json", "X-XSRF-TOKEN": csrfToken },
      body: JSON.stringify(payload)
    });
    const startData = await startRes.json();
    if (!startData.success) return "[Result] " + JSON.stringify({ status: "failed", reason: "START_TASK_FAILED", data: startData });

    // 3. 轮询 (status 2 为成功, -1 为失败)
    let pollData = null;
    for (let i = 0; i < 60; i++) {
      await new Promise(r => setTimeout(r, 5000));
      const pollRes = await fetch("https://post.alibaba.com/product/batchEasyListing/getLatestRootTaskResult.json?needSubStatus=true&scene=agentAccioWorkPublish&subScene=multiUrlProduct");
      pollData = await pollRes.json();
      if (pollData.data.status === 2 || pollData.data.status === -1) break;
    }

    // 4. 获取明细
    const detailRes = await fetch(`https://post.alibaba.com/product/batchEasyListing/pageQueryTask.json?parentId=${pollData.data.taskId}`);
    const detailData = await detailRes.json();
    return "[Result] " + JSON.stringify({ status: "completed", summary: pollData.data, detail: detailData });
  } catch (e) { return "[Result] " + JSON.stringify({ status: "error", message: e.message }); }
})()
```

## 4. 业务错误深度转译表

| 原始错误码 | 用户侧描述 | 建议操作 |
| :--- | :--- | :--- |
| `PUB_BIZCHECK_CAT_PUB_RESTRICT` | **经营大类受限** | 商品类目不在经营范围内，请去“公司信息”修改大类或先存为草稿。 |
| `BUDGET_LIMIT` | **AI点数不足** | 账号 AI 点数已耗尽，请充值或切换账号。 |
| `INVALID_URL` | **链接无法识别** | 请检查输入的商品链接是否来自支持的平台（1688/淘宝等）。 |

## 5. 输出规范
严格遵循 `./references/INSTRUCTION.md` 进行 Markdown 报表输出。
- **概况表**：展示总数、成功上架、草稿数、失败数。
- **明细表**：展示原始 URL、商品 ID、最终状态、转译后的失败原因。

## 6. 子代理执行优化指南 (Anti-Loop)
- **拒绝碎片化测试**：子代理严禁频繁使用 `({ status: 'test' })` 进行环境探测。应信任父代理提供的完整 IIFE 模板，并一次性执行。
- **显式结果返回**：所有 `console` 输出必须带有 `[Result]` 前缀，以便工具链能够精准捕获并解析 JSON。
- **提前终止**：预检失败时必须立即返回结果，不要进入后续的触发或轮询逻辑。
- **防止数据损坏**：子代理在执行保存（Save）或发布（Publish）脚本前，必须通过 `console.log` 输出即将提交的 Payload 结构摘要（包含图片数量、属性数量），确保关键数据未丢失。

## 7. 数据完整性与安全保障规范 (Critical Safeguards)

### 7.1 覆盖逻辑预警
- **受影响接口**：`https://post.alibaba.com/product/publish/submitDraft.json` 及类似的更新接口。
- **行为风险**：此类接口采用 **Full Overwrite (全量覆盖)** 模式。若 Payload 中缺少 `images`、`productAttributes` 或 `description` 等字段，服务器会将对应字段更新为空，导致数据丢失。

### 7.2 强制执行流程 (Fetch-Modify-Submit)
更新现有商品或草稿时，必须遵循：
1. **Fetch**：调用 `getDraftDetail.json` 或相应查询接口获取商品全量数据。
2. **Modify**：仅在内存中修改需要变更的特定字段（如 `subject`, `keywords`）。
3. **Validate**：提交前检查 Payload 是否包含以下核心字段：
    - `mainImageVOList` (主图列表)
    - `productAttributeList` (产品属性)
    - `description` (详情描述)
4. **Submit**：提交经过校验的全量 Payload。

### 7.3 数据备份建议
在大批量（>10个）更新前，建议先将原始数据摘要（itemId + subject + 关键属性）记录在会话日志或本地文件中，以便发生意外时快速定位和恢复。
