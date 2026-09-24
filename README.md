# Python 基础语法学习资料

本套资料覆盖 Python 最核心的 5 个语法主题：

| 编号 | 文件 | 主题 | 内容要点 |
| --- | --- | --- | --- |
| 01 | `01_variables.py` | 变量 | 命名规则、常见类型、动态类型、多变量赋值 |
| 02 | `02_operators.py` | 运算符 | 算术、比较、赋值、逻辑、成员、身份、优先级 |
| 03 | `03_expressions.py` | 表达式 | 类型转换、字符串格式化、输入输出、表达式组合 |
| 04 | `04_control_flow.py` | 流程控制 | if/elif/else、for、while、break、continue、循环 else |
| 05 | `05_functions.py` | 函数 | 定义与调用、参数、返回值、默认参数、*args、**kwargs、作用域 |

每个文件都是**独立可运行**的 Python 脚本，内含中文注释、示例输出和本节小结，适合在 VS Code 中逐个运行学习。

---

## 环境准备

1. 安装 Python 3.8 或更高版本
2. 安装 [Visual Studio Code](https://code.visualstudio.com/)
3. 在 VS Code 中安装 Python 扩展（Microsoft 官方扩展）

本套资料**不依赖任何第三方库**，使用 Python 内置功能即可运行。

---

## 如何在 VS Code 中运行

### 方式一：右键运行（最推荐）

1. 在 VS Code 中打开本文件夹
2. 打开任意一个 `.py` 文件，例如 `01_variables.py`
3. 在编辑器空白处右键 → 选择 **"Run Python File in Terminal"**
4. 在下方终端查看输出

### 方式二：快捷键

1. 打开任意一个 `.py` 文件
2. 按 **Ctrl + F5** 即可不调试直接运行

### 方式三：调试运行

1. 打开任意一个 `.py` 文件
2. 在代码行号左侧点击设置断点
3. 按 **F5** 启动调试，可单步查看变量变化

---

## 推荐学习顺序

建议按编号顺序逐个打开并运行：

```bash
python 01_variables.py
python 02_operators.py
python 03_expressions.py
python 04_control_flow.py
python 05_functions.py
```

每运行完一个文件，先回顾文件底部的**本节小结**，再进入下一个主题。

---

## 练习与答案

练习题和参考答案在 `exercises/练习题.md` 中。建议先独立尝试，再看答案。

---

## 目录结构

```
python-basics/
├── README.md
├── 01_variables.py
├── 02_operators.py
├── 03_expressions.py
├── 04_control_flow.py
├── 05_functions.py
└── exercises/
    └── 练习题.md
```

---

## 学习建议

- 不要只看，**要动手改**：把示例里的数字、条件、字符串改一改，看看输出怎么变
- 遇到报错很正常，认真读错误信息是成长最快的方式
- 把每个文件的底部小结默写下来，检查自己是否真正理解
