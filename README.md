# 实践作业 02：Python 基础 + 调用大模型 API

## 一、老师到底想让你做什么

一句话：**用你自己的 Python 代码，把智谱 GLM 大模型调通，让它回答一个问题。**

课堂上演示的 `02.ipynb` 其实是两块拼起来的：

| 部分 | 格子 | 作用 | 是不是作业重点 |
| --- | --- | --- | --- |
| Python 基础复习 | 第 1 ~ 10 格 | 变量、运算符、流程控制、函数、类、模块、异常处理 | 铺垫，确保你会写 Python |
| **调用 GLM 大模型** | 第 11 ~ 14 格 | 读 Key → 建客户端 → 发提示词 → 拿回复 | **这才是要交的** |

最终交付物很明确：

1. 一个**跑通了的 notebook**（每个格子下面都有输出）
2. 第 14 格里 GLM 对「西北民族大学广告学专业」的回答文字

**老师真正想表达的是**：大模型不只有网页聊天框这一种用法——你可以用几行 Python 把它接进自己的程序。这是这门课后面用 AI 处理广告数据、生成分析报告的基础。

## 二、三步把它跑起来

### 第 1 步：申请 API Key

1. 打开 https://open.bigmodel.cn ，注册并登录
2. 右上角头像 → 「API Keys」→ 创建新 Key
3. **立刻复制保存**（关闭弹窗后就再也看不到了）

### 第 2 步：配置 .env

把 `.env.example` 复制成 `.env`：

```bash
cp .env.example .env
```

然后编辑 `.env`，把 Key 填进去：

```
ZHIPU_API_KEY=sk-xxxxxx这里换成你自己的
```

> 注意：文件名必须是 `.env`，不能是 `.env.txt`。Windows 资源管理器默认隐藏扩展名，建议直接用 VS Code 操作。

### 第 3 步：装依赖并运行

```bash
pip install -r requirements.txt
```

> ⚠️ **最常见的坑**：老师代码里写的是 `from zai import ZhipuAiClient`，但**安装包名是 `zai-sdk`**。
> 直接 `pip install zai` 装到的是另一个同名占位包，然后会报 `ModuleNotFoundError: No module named 'zai'`。
> 正确写法是 `pip install zai-sdk`（`requirements.txt` 里已经写好了）。

然后用 VS Code 打开 `02.ipynb`，从上往下一个一个格子运行（`Shift + Enter`）。

第 1 ~ 10 格是纯 Python 基础，不需要 Key 就能跑；第 11 ~ 14 格才需要 Key。

## 三、目录结构

```
llm-api-practice/
├── 02.ipynb          # 作业主体（18 格）
├── .env.example      # 环境变量模板
├── .env              # 你自己创建的，不要提交
├── requirements.txt  # 依赖清单
├── .gitignore        # 已忽略 .env
└── README.md
```

## 四、常见问题

| 现象 | 原因 | 解决 |
| --- | --- | --- |
| `No module named 'zai'` | 装错包了 | `pip install zai-sdk`（**不是** `pip install zai`） |
| `No module named 'dotenv'` | 没装 python-dotenv | `pip install python-dotenv` |
| 提示找不到 ZHIPU_API_KEY | `.env` 没建或名字不对 | 确认文件名是 `.env`，内容是 `ZHIPU_API_KEY=...` |
| 报 401 鉴权失败 | Key 填错或已失效 | 回开放平台重新复制 |
| 报模型不存在 / 无权限 | 账号没开通 `glm-5.3` | 把第 12、13 格的 `model="glm-5.3"` 改成 `"glm-4.6"` |
| 改了 `.env` 还是读不到 | notebook 需要重启内核 | 重启内核后再跑第 11 格 |
| 老师那格 `import 模块A` 报错 | 老师用的是示意代码，没有真实模块 | 本作业已改成用 `math` 模块演示，可直接运行 |

## 五、关于课上那个疑问："WorkBuddy 提供模型服务吗"

- **WorkBuddy 不是 LLM API 提供商**：它不卖 token、不对外发 API Key，所以你不能像调智谱那样去调「WorkBuddy 的 API」。
- **但 WorkBuddy 能帮你调别人的 API**：智谱、通义、OpenAI、Kimi……只要对方有 HTTP 接口或 Python SDK，WorkBuddy 都能帮你写调用代码、修 bug、解释报错。

所以这次作业该用的还是**智谱的 Key 和智谱的 API**，WorkBuddy 负责帮你把代码写对、跑通。

## 六、提交前检查清单

- [ ] 所有格子都运行过，下面有输出
- [ ] 第 14 格能看到 GLM 对广告学专业的介绍
- [ ] `.env` 没有被提交进仓库（已在 `.gitignore` 中忽略）
- [ ] 如果用 Git 提交，先 `git status` 确认没有 `.env`
