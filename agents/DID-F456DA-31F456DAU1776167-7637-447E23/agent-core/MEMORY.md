# Agent Memory

## Core Synchronization Strategy (Multi-terminal)
- **Concept**: Home (Office branch) <-> GitHub (Cloud) <-> Factory (Production center).
- **Workflow**:
    - **Morning (Start)**: Command: "同步云端最新的数据" (Sync latest cloud data) -> Git Pull.
    - **Evening (End)**: Command: "把今天的工作同步到 GitHub" (Sync today's work to GitHub) -> Git Push.
- **Sync Scope**:
    - `project/`: Scripts and code.
    - `agent-core/MEMORY.md`: Business context and preferences.
    - `agent-core/diary/`: Daily logs.
    - `agent-core/skills/`: Custom skills.
- **Conflict Policy**:
    - **Code/Scripts**: "Factory first" (Source of Truth).
    - **Notes/Memory**: **Strict Content Merging**. I will merge additions from both terminals to ensure no notes, memories, or logs are lost. This is a critical priority for data continuity.
