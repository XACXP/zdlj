import pandas as pd
import glob
import os

# For XLS files
xls_files = [
    r"E:\xwechat_files\wxid_gywnr0wtshih22_7c24\msg\file\2026-04\牛皮纸桶合同2025-05-16.xls",
    r"E:\xwechat_files\wxid_gywnr0wtshih22_7c24\msg\file\2026-04\牛皮纸桶合同2026-02-24.xls",
    r"E:\xwechat_files\wxid_gywnr0wtshih22_7c24\msg\file\2026-04\牛皮纸桶合同2026-02-27.xls",
    r"E:\xwechat_files\wxid_gywnr0wtshih22_7c24\msg\file\2026-04\四卒260172.XLS",
    r"E:\xwechat_files\wxid_gywnr0wtshih22_7c24\msg\file\2026-04\四卒260244-50372.XLS",
    r"E:\xwechat_files\wxid_gywnr0wtshih22_7c24\msg\file\2026-04\四卒260328.XLS"
]

results = []

for f in xls_files:
    if not os.path.exists(f):
        results.append(f"--- File: {f} Not Found ---\n")
        continue
    try:
        # Try reading with xlrd
        df = pd.read_excel(f)
        results.append(f"--- File: {os.path.basename(f)} ---\n{df.head(20).to_string()}\n")
    except Exception as e:
        results.append(f"--- File: {os.path.basename(f)} Error: {str(e)} ---\n")

with open("excel_summary.txt", "w", encoding="utf-8") as out:
    out.write("\n".join(results))
