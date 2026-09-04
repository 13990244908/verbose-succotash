---
name: concept-explainer
description: |
  This skill should be used when the user wants a self-contained, structured learning
  material for a single concept (e.g. "教我 Agent", "做一份关于 Transformer 的学习笔记",
  "make a study guide for <X>"). It produces one HTML file per concept with sections for
  learning goals, personal explanation, core mechanism, a concrete scenario, pitfalls,
  self-check questions, and verifiable source links. Do NOT use it for short Q&A, code-only
  tasks, or live tutoring.
agent_created: true
---

# Concept Explainer — 个人概念学习资料生成器

> 一个**可复用**的概念学习 Skill：传入任何概念名，按统一模板生成一份结构化 HTML 学习资料。
> 不为某一个概念而写，可直接换概念名复用。

---

## 1. 适用场景

满足以下**全部**特征时使用本 Skill：

- 用户想**深入理解一个名词/概念**（而不是求解一个具体问题）。
- 期望产出是**一份可长期保留、可重新打开阅读**的资料（HTML / Markdown / 笔记），而不是即时问答。
- 用户能接受一份**完整的教学结构**（学习目标 → 解释 → 机制 → 场景 → 边界 → 自测 → 资料来源）。
- 用户希望**可信、可核查**：每个非平凡断言都附引用链接。

**不建议使用本 Skill 的情况**：

- 用户只要一句话定义 / 一行例子 → 直接回答，不必调 Skill。
- 用户在做工程/编程任务 → 用对应任务的 Skill。
- 概念需要在多轮对话中持续迭代打磨 → 也可调，但应允许多次修改而不是一次性产出。

触发词示例：`教我 <X>` / `做一份 <X> 的学习资料` / `给我系统讲一下 <X>` / `learn <X>` /
`explain <X> for me` / `concept card for <X>`。

---

## 2. 输入信息

| 字段 | 必填 | 默认值 | 说明 |
|------|------|--------|------|
| `concept_name` | ✅ | — | 要学习的概念，建议同时给出英文名（如 "Agent"、"LLM Context"、"Skill"）。 |
| `audience` | ❌ | "本人（学习者）" | 读者是谁，决定解释深度与口吻。 |
| `depth` | ❌ | `medium` | `shallow` 一页纸 / `medium` 标准讲义 / `deep` 含历史脉络与研究前沿。 |
| `cite_source` | ❌ | `required` | 是否强制要求来源链接。`required` 时每个非平凡断言都要 `[name](url)`。 |
| `language` | ❌ | `zh-CN` | 输出语言；如概念带英文术语可保留英文。 |
| `related_concepts` | ❌ | `[]` | 需要在最后做"关联"小节时列出。 |

如果用户只给了 `concept_name`，其他字段用默认。如果用户在同一句话里提了多个概念，分别调用本 Skill 各产一份。

---

## 3. 生成步骤（按顺序执行）

**Step 1 — 框定问题（学习目标 + 关键问题）**

不要直接解释，先在本步骤用 3-5 行草拟：

- **学习目标**：3-5 条，每条是"读完之后**能做什么**"（avoid：理解 X、掌握 X 这类不可验证的目标）。
- **关键问题**：3-5 个，是真正驱动读者读下去的疑问句，不是搜索关键词。

把这两块放到最终 HTML 的最前面，告诉读者"为什么要读"。

**Step 2 — 画出概念地图**

私底下（不必展示给用户）用一段话决定：

- 这个概念由哪些**部件**组成？
- 这些部件之间是**什么关系**（顺序 / 嵌套 / 循环 / 反馈）？
- 它与哪些**相邻概念**容易混淆（需要"辨析"）？

这一步确保后续写出来的"机制"不是空话。

**Step 3 — 起草解释**

- **个人解释**用读者第一视角能听懂的话写，避免照搬百科条目或 AI 对话结果原句。
- **核心机制或组成**要把"部件 + 关系 + 工作方式"写清，必要时画一张 ASCII/Mermaid 图。
- **应用场景**挑一个**端到端**的例子：输入是什么 → 经过什么步骤 → 输出是什么。
- **边界/辨析**挑 2-3 个最常被混淆的相邻概念，写清"何时不等价"。
- **自测问题**3-5 题，给出要点答案（不是单纯 A/B/C）。
- **参考来源**每个非平凡断言一条，命名与 URL 都必须可核查；无来源标"（待核查）"。

**Step 4 — 自检**（必须执行，参考第 5 节的自检表）

完成初稿后**先过一遍自检**，不通过则改稿再来，不直接输出文件。

**Step 5 — 落盘**

输出文件命名：

- 文件名：`<concept_name>` 的 kebab-case ASCII 形式，例：`agent` / `llm-context` / `skill`。
- 路径：`learning-materials/<slug>.html`。每个概念一个文件，方便做版本管理与交叉引用。
- HTML 必须自包含：CSS 内联、可双击在浏览器打开；不要引外部 CDN（除非被引用的图）；保留中文。
- 输出后用 `present_files` 预览给用户检查。

---

## 4. 输出结构

每个学习资料 HTML 必须包含以下小节（缺则补，Empty 删去不留空节）：

1. **标题与一句话定位** — 一句话说清"这是什么"。
2. **学习目标 + 关键问题** — 让读者带着目标读。
3. **个人解释** — 自己的话，能让小白听懂。
4. **核心机制或组成** — 拆部件、画关系、讲工作方式。
5. **一个具体应用场景** — 端到端：输入 → 处理 → 输出。
6. **容易混淆的问题与使用边界** — 与相邻概念的辨析。
7. **自测问题（带要点答案）** — 检验学习效果。
8. **参考来源** — 名称 + URL，每条都可点击。
9. **（可选）与其它概念的关联** — 留接口为 concept-relationship.html 准备。

样式建议：单一 `max-width: 760px` 居中；标题层级用 `<h2>/<h3>`；代码块用 `<pre>`；引用用 `<blockquote>` 自带边框；Mermaid 用 `<pre class="mermaid">` 包裹、引入 `mermaid.min.js`。

---

## 5. 资料来源要求

- **可核查**：所有 URL 都必须能打开。**禁止**伪造 paper、捏造博客、编造 `example.com`。
- **就近**：每个非平凡断言一句一引，或一整段一句引用。
- **权威**：技术类优先官方文档与学术论文；通用类允许维基百科 / 知名博客。
- **诚实标注**：个人猜想、课堂讲解、内部理解都注明"（个人判断）"或"（待核查）"。
- **复用价值**：来源尽量选不会失效的（官方文档 + DOI/arxiv 优先）。

---

## 6. 自检要求（生成完毕前必跑）

不通过则改稿直到全部通过：

- [ ] 完整性：必含 7 个小节（学习目标/关键问题、个人解释、机制、场景、辨析、自测、来源），缺一不可。
- [ ] 个人解释：是否真的用了"自己的话"，不是 AI 直出整段搬运？
- [ ] 机制：是否拆到"部件 + 关系 + 工作方式"？是否能让不熟这个概念的读者读完画出结构图？
- [ ] 场景：是否端到端（输入 → 处理 → 输出），不是只描述单点？
- [ ] 辨析：是否覆盖 2-3 个最容易被混淆的相邻概念？是否给出"何时不等价"？
- [ ] 来源：所有 URL 是否真实可达？引用是否与断言对应（不张冠李戴）？
- [ ] 自测：题目是否能让读者检验"是不是真的懂"，不是单纯复述定义？是否附答案要点？
- [ ] 措辞：是否回避了"AI 一定 / 本质就是 / 唯一正确"等绝对化表达？
- [ ] 复用性：把 `concept_name` 换成 "Transformer" 或 "REST" 这类技术名词，整个流程是否可以无缝套用？

**通过后再把文件写入 `learning-materials/<slug>.html`，并调用 `present_files` 预览给用户。**

---

## 7. 范例映射（本仓库内的实例）

| 概念 | 输入 | 输出文件 | 关联 |
|------|------|----------|------|
| Agent | `concept_name="Agent"` | `learning-materials/agent.html` | 与"上下文"、"Skill"关联 |
| 大模型的上下文 | `concept_name="大模型的上下文"` | `learning-materials/llm-context.html` | 决定 Agent 能力上限 |
| Skill | `concept_name="Skill"` | `learning-materials/skill.html` | 沉淀 Agent 的可复用知识 |

三份实例均按本 Skill 的 7 小节产出，并已在 `learning-materials/concept-relationship.html` 中画出三者的关系。

---

## 8. 复用方式

在 WorkBuddy 中：

- 项目级 Skill：本 Skill 已放在仓库 `.workbuddy/skills/concept-explainer/SKILL.md`，
  WorkBuddy 在该仓库工作时会自动识别，无需额外配置。
- 调用方式：在本仓库目录内对 WorkBuddy 说

  > 用 `concept-explainer` Skill 帮我学习 `<新概念>`，深度 `medium`。

  或者直接说：

  > 用项目里的 concept-explainer 给"Transformer"做一份学习资料。

- 增量产出：建议每次调用保存一个独立 HTML，便于跨概念横向比较、累积形成个人知识库。

---

## 9. 文件结构

```
.workbuddy/
└── skills/
    └── concept-explainer/
        ├── SKILL.md                    # 本文件
        └── references/
            ├── html-template.md        # HTML 骨架与样式说明
            └── learning-blueprint.md   # 学习目标 / 关键问题写法模板
```
