# HTML 学习资料模板

适用于 `concept-explainer` 生成的 `learning-materials/<slug>.html`。

## 1. 文档结构（HTML 5 骨架）

```html
<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>{概念名} — 学习资料</title>
  <style>
    :root { --fg:#1f2329; --muted:#58606b; --bg:#ffffff; --card:#f6f8fa; --accent:#0969da; --warn:#bf3989; }
    @media (prefers-color-scheme: dark) {
      :root { --fg:#e6edf3; --muted:#8b949e; --bg:#0d1117; --card:#161b22; --accent:#58a6ff; --warn:#ff7b72; }
    }
    html, body { margin:0; padding:0; background:var(--bg); color:var(--fg); }
    body { font: 16px/1.7 -apple-system, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
           max-width: 780px; margin: 0 auto; padding: 32px 24px 96px; }
    h1 { font-size: 32px; line-height: 1.25; margin: 0 0 8px; letter-spacing: -0.02em; }
    h2 { font-size: 22px; line-height: 1.3; margin: 40px 0 12px; padding-bottom: 6px; border-bottom: 1px solid var(--card); }
    h3 { font-size: 17px; margin: 24px 0 8px; color: var(--accent); }
    p  { margin: 10px 0; }
    .tag { display:inline-block; padding:2px 10px; border-radius:999px; background:var(--card); color:var(--muted); font-size:12px; margin-right:6px; }
    blockquote { margin: 12px 0; padding: 10px 16px; border-left: 3px solid var(--accent); background: var(--card); color: var(--muted); border-radius: 0 6px 6px 0; }
    code, pre { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; }
    code { padding: 1px 6px; background: var(--card); border-radius: 4px; font-size: 0.92em; }
    pre { padding: 14px 16px; background: var(--card); border-radius: 8px; overflow-x: auto; line-height: 1.55; }
    table { width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 14px; }
    th, td { padding: 8px 10px; border-bottom: 1px solid var(--card); text-align: left; vertical-align: top; }
    th { background: var(--card); color: var(--muted); font-weight: 600; }
    ul, ol { padding-left: 22px; }
    li { margin: 4px 0; }
    .source a { word-break: break-all; }
    .meta { color: var(--muted); font-size: 13px; margin-top: 4px; }
    .callout { border-left: 3px solid var(--warn); background: var(--card); padding: 12px 16px; border-radius: 0 6px 6px 0; }
    hr { border: none; border-top: 1px dashed var(--card); margin: 32px 0; }
  </style>
</head>
<body>
  <header>
    <p class="meta"><span class="tag">学习资料</span><span class="meta">由 concept-explainer Skill 生成 · 生成时间：{ISO 日期}</span></p>
    <h1>{概念名}</h1>
    <p class="meta">{一句话定位：这是什么、不是什么、为什么重要}</p>
  </header>

  <h2>学习目标 &amp; 关键问题</h2>
  <h3>读完能做：</h3>
  <ol>
    <li>{动词开头的可验证目标}</li>
  </ol>
  <h3>会回答：</h3>
  <ul>
    <li>{驱动读者读下去的疑问句}</li>
  </ul>

  <h2>个人解释</h2>
  <p>{用自己的话，能让小白听懂。避免照搬 AI 输出原句。}</p>

  <h2>核心机制或组成</h2>
  <p>{拆部件 + 关系 + 工作方式。必要时给 ASCII/Mermaid 图。}</p>
  <pre class="mermaid">{可被 mermaid.js 渲染的图}</pre>

  <h2>一个具体应用场景</h2>
  <p><strong>输入：</strong>{具体的}</p>
  <p><strong>处理：</strong>{步骤化}</p>
  <p><strong>输出：</strong>{具体的}</p>

  <h2>容易混淆的问题与使用边界</h2>
  <table>
    <thead><tr><th>易混淆点</th><th>本概念</th><th>相邻概念</th></tr></thead>
    <tbody>
      <tr><td>{点}</td><td>{定义}</td><td>{区别}</td></tr>
    </tbody>
  </table>

  <h2>自测问题</h2>
  <ol>
    <li><strong>{题目}</strong><br/>要点：{答案要点，2-3 句}</li>
  </ol>

  <h2>参考来源</h2>
  <ol class="source">
    <li><a href="{url}">{来源名}</a> — {一句话说明被引用的内容}</li>
  </ol>

  <h2>与其他概念的关联</h2>
  <p>{若干句，点到为止；详细关系看 concept-relationship.html。}</p>

  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script>if (window.mermaid) mermaid.initialize({ startOnLoad: true, securityLevel: 'loose' });</script>
</body>
</html>
```

## 2. 写作要点

- **个人解释 ≠ AI 输出原句**：写完通读一遍，确保是"自己"在讲，不是把模型答复整段搬运。
- **机制图用 Mermaid**：本仓库的 HTML 默认引入 `mermaid.min.js`，可直接写 `<pre class="mermaid">`。
- **来源就近引用**：正文段尾附 `[来源名](URL)`；不要全部堆在最后。
- **避免绝对化措辞**："AI 一定 / 本质就是 / 唯一正确"一律换成 "在常见场景下 / 在我的理解里 / 主流看法是"。
- **可双击在浏览器打开**：所有 CSS 内联，仅 mermaid.js 是 CDN，可断网情况下其他部分仍可阅读。
