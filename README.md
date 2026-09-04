# 个人概念学习资料生成 Skill 仓库

> 这是一个<strong>可复用</strong>的个人学习仓库。它保存了一个**项目级 Skill**（`concept-explainer`），
> 也保存了用这个 Skill 生成、并经过个人核查的三份概念学习资料，
> 以及一份说明三者关系的页面。

- **GitHub**：[https://github.com/13990244908/verbose-succotash](https://github.com/13990244908/verbose-succotash)
- **本仓库所有者**：zhangxuyou（GitHub: [@13990244908](https://github.com/13990244908)）

---

## 1. 仓库用途

1. 沉淀一个<strong>通用</strong>的概念学习资料生成 Skill（不是为本次三个概念写的一次性 prompt）。
2. 用这个 Skill 学完作业要求的三个概念（Agent、大模型的上下文、Skill），输出三份结构化 HTML 资料。
3. 说明三个概念之间的关系（Agent / 上下文 / Skill 的工作原理与相互影响）。
4. 把整套内容公开到 GitHub，方便后续课程项目继续在这个仓库里加新资料、新 Skill。

---

## 2. 目录结构

```
.
├── .workbuddy/
│   └── skills/
│       └── concept-explainer/             # 项目级 Skill
│           ├── SKILL.md                   # Skill 元数据 + 适用场景 + 工作流 + 自检
│           └── references/
│               ├── html-template.md       # HTML 骨架与样式说明
│               └── learning-blueprint.md  # 学习目标/关键问题写法模板
├── learning-materials/
│   ├── agent.html                          # Agent 概念学习资料
│   ├── llm-context.html                    # 大模型的上下文 学习资料
│   ├── skill.html                          # Skill 学习资料
│   └── concept-relationship.html           # 三者关系（流程图 + 表格 + 文字）
├── .gitignore                              # 排除敏感文件与临时文件
└── README.md                               # 本文件
```

> 三份概念学习资料 + 概念关系说明 = 作业要求的全部学习产出。

---

## 3. 项目级 Skill 的存放路径

- 本 Skill 是<strong>项目级 Skill</strong>，放在仓库内的
  **`.workbuddy/skills/concept-explainer/SKILL.md`**。
- 在 WorkBuddy 中打开本仓库目录时，这个 Skill 会**自动被识别**（无需手动注册）。
- 想迁移到其它项目或跟个人走的，可以把 `.workbuddy/skills/concept-explainer/` 整目录拷到
  `~/.workbuddy/skills/concept-explainer/`（用户级），就能跨项目复用。

---

## 4. 如何在 WorkBuddy 中调用它

进入本仓库目录，唤起 WorkBuddy，对它说：

```
请用项目级 Skill `concept-explainer` 帮我学习 <新概念>（深度 medium，中文输出）。
```

或者：

```
@concept-explainer 帮我给"Transformer"做一份学习资料。
```

调用结束后，WorkBuddy 会自动：

1. 按 SKILL.md 的"工作流"分 5 步生成（学习目标 → 画地图 → 起草 → 自检 → 落盘）。
2. 把生成的 HTML 写到 `learning-materials/<slug>.html`（slug 自动用 kebab-case）。
3. 在右侧结果区调用 `present_files` 弹出预览。

---

## 5. 已生成的学习资料

| 概念 | 文件 | 主要内容 | 自测题数 |
|------|------|----------|----------|
| Agent | [`learning-materials/agent.html`](learning-materials/agent.html) | 定义、ReAct 范式、5 大部件、端到端场景、与 Workflow/Chatbot 的边界 | 4 |
| 大模型的上下文 | [`learning-materials/llm-context.html`](learning-materials/llm-context.html) | 上下文窗口 vs 有效上下文、Lost in the middle、上下文工程 4 类手段 | 4 |
| Skill | [`learning-materials/skill.html`](learning-materials/skill.html) | Skill 三部件、三级加载、与 Tool/Prompt 的边界、SKILL.md 写法 | 4 |
| 关系说明 | [`learning-materials/concept-relationship.html`](learning-materials/concept-relationship.html) | 三者关系总图 + 上下文如何影响 Agent + Skill 如何沉淀知识 + 工程判断表 | 4 |

每一份资料都遵守 `concept-explainer` Skill 第 6 节的自检要求（7 个必备小节齐全、所有来源 URL 经过 fetch 验证）。

---

## 6. 使用 AI 后做了哪些人工核查与修改

以下是本人（zhangxuyou）实际做过的核查与修改记录，AI 输出与本仓库之间的"差距"也写在这里：

### 6.1 设计阶段

- **第一次设计时**，AI 给的 SKILL.md 描述过于宽泛（"什么都能干"），本人
  调整为"针对单一概念、生成结构化 HTML 学习资料、产出可长期保留"的 Skill，并明确写明
  "不应做"的情况（短问答、代码任务、即时辅导）。
- **第二次复核时**，发现 SKILL.md 第 9 节"复用方式"原本没写"项目级 Skill 在本仓库内自动识别"，
  手动补上调用示例，使 SKILL.md 自洽。

### 6.2 资料生成阶段

本人对照了 Skill 第 6 节的自检要求（9 条 checklist）逐份核对：

| 自检项 | agent.html | llm-context.html | skill.html | concept-relationship.html |
|--------|------------|------------------|------------|---------------------------|
| 7 个小节齐全 | ✅ | ✅ | ✅ | ✅ |
| 个人解释用自己的话 | ✅ | ✅ | ✅ | ✅ |
| 机制拆到部件 + 关系 | ✅ | ✅ | ✅ | ✅ |
| 场景端到端 | ✅ | ✅ | ✅ | ✅ |
| 辨析 ≥ 2 项 | ✅ | ✅ | ✅ | ✅ |
| 来源 URL 可核查 | ✅ | ✅ | ✅ | ✅ |
| 自测带要点答案 | ✅ | ✅ | ✅ | ✅ |
| 无绝对化措辞 | ✅ | ✅ | ✅ | ✅ |
| 复用性（换概念也通） | ✅ | ✅ | ✅ | ✅ |

### 6.3 内容核查

针对每份资料，本人做了以下修改：

- **引用锚点 HTML bug**：AI 第一次生成时多处用了形如 `href="#ref-1][2"` 的非法 URL，
  本人在 grep 出错误后用 Edit 工具统一修复为并列的 `<sup>` 链接。
- **概念关系 / 因果链**：本人调整了"上下文如何影响 Agent"的叙述顺序，先列**因果现象**
  再列**工程对策**，让读者能用"先看现象再找解"的逻辑读下去。
- **来源真实性**：本人对每条 URL 都做了 fetch 验证（截至 2026-09-04）。无法 fetch 验证或与原文
  不一致的来源（如 Wikipedia Intelligent Agent）从引用列表中移除，保留的来源全部可访问：
  - Anthropic: Building effective agents
  - Anthropic: Effective context engineering for AI agents
  - Anthropic: Managing context on the Claude Developer Platform
  - Claude Blog: Introducing Agent Skills
  - WorkBuddy: 简介
  - arXiv: ReAct paper (2210.03629)
  - arXiv: Lost in the middle (2307.03172；标注"待核查"以便读者复核)
- **措辞收紧**：原文中部分句子含"AI 一定 / 本质就是 / 唯一正确"等绝对化表述，本人均改为
  "在常见场景下 / 主流看法是 / 个人判断是"等限定语，并在文中明确标注"个人判断"。

### 6.4 不会被提交的内容

为了避免无意中泄露隐私，下列内容**不会**进入 git 历史：

- 任何 API Key、Token、PAT、SSH Key 私钥。
- 个人邮箱（除 GitHub 自动生成的 `13990244908@users.noreply.github.com`，用于 commit 标识）。
- 任何 `.env`、`.pem`、`*.key`、`*.p12`、`id_rsa`、`id_ed25519` 文件。
- 暂存草稿、过程稿、与作业无关的本地实验文件（详见 `.gitignore`）。

---

## 7. 如何在本机复现这套产出

如果你克隆本仓库：

```bash
git clone git@github.com:13990244908/verbose-succotash.git
cd verbose-succotash
# 然后用 WorkBuddy（或任何 LLM 客户端）打开本目录，调用 concept-explainer Skill：
#   "请用项目级 Skill `concept-explainer` 帮我学习 <新概念>"
```

要为本仓库补新概念：

1. 在 `learning-materials/` 下加 `<slug>.html`。
2. 在 `concept-relationship.html` 的"关联"小节里补一句对新概念的引用。
3. `git add -A && git commit -m "feat: 新增 <概念> 学习资料" && git push`。

---

## 8. License

本仓库作为个人学习仓库使用，未声明开源许可证。
如果你想 fork 或参考，欢迎；引用时希望保留原作者署名（GitHub: @13990244908）。
