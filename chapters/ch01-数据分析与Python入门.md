# 第 1 章 数据分析与 Python 入门

## 1.1 什么是统计数据分析？

简单说，**统计数据分析**就是：**从一堆看似杂乱的数据里，用统计方法和计算机，找出有用的规律和结论**。

比如：

- 一家网店想知道「哪些商品卖得好」；
- 学校想知道「学生的数学成绩和英语成绩有没有关系」；
- 政府想知道「居民收入的中位数是多少」。

这些都是统计数据分析的典型场景。这门课会教你用 **Python** 这个工具，完成这些任务。

## 1.2 数据分析的一般流程

无论做什么分析，大致都遵循这五步：

```
提出问题 → 收集数据 → 清洗整理 → 探索分析 → 得出结论
```

| 步骤 | 要做的事 | 本课程对应章节 |
| --- | --- | --- |
| 提出问题 | 明确你想知道什么 | 第 1 章 |
| 收集数据 | 拿到数据（问卷、数据库、爬虫等） | 第 1 章 |
| 清洗整理 | 处理缺失值、错误值，规整格式 | 第 2 章 |
| 探索分析 | 计算统计量、画图、做推断 | 第 2~6 章 |
| 得出结论 | 用统计结论回答问题 | 第 5~6 章 |

> 记住：**分析是为「问题」服务的**，别为了用工具而用工具。

## 1.3 Python 基础速览

如果你没接触过编程，别慌，这一节我们把最常用的语法过一遍。

### 1.3.1 变量与数据类型

```python
# 变量：给数据起个名字
name = "小明"          # 字符串 str
age = 20               # 整数 int
height = 1.75          # 浮点数 float
is_student = True      # 布尔 bool

print(name, age, height, is_student)
```

### 1.3.2 列表与字典

```python
# 列表 list：一组有序的数据
scores = [85, 90, 78, 92]
print(scores[0])       # 取第一个元素，索引从 0 开始

# 字典 dict：键值对
student = {"姓名": "小明", "数学": 85, "英语": 90}
print(student["数学"])  # 通过键取值
```

### 1.3.3 条件与循环

```python
# 条件判断 if
score = 85
if score >= 60:
    print("及格")
else:
    print("不及格")

# 循环 for
for s in [85, 90, 78, 92]:
    print(s)
```

### 1.3.4 函数

```python
# 函数：把一段逻辑封装起来，方便复用
def average(nums):
    return sum(nums) / len(nums)

print(average([85, 90, 78, 92]))
```

## 1.4 NumPy 与 Pandas 初识

手动算一个列表的均值还行，但面对几千行、几万行的数据，就要靠专门的库了。这门课主要用两个库：

- **NumPy**：擅长数值计算，提供高效的数组和数学函数。
- **Pandas**：擅长处理表格数据（类似 Excel），是本课程的核心工具。

```python
import numpy as np      # 习惯上简称 np
import pandas as pd     # 习惯上简称 pd

# NumPy 数组
arr = np.array([1, 2, 3, 4, 5])
print("均值：", arr.mean())

# Pandas 读取 CSV
df = pd.read_csv("data/students.csv")
print(df.head())        # 看前 5 行
```

## 1.5 读取我们的示例数据

本课程准备了两个数据集，由 `generate_data.py` 生成：

- `data/students.csv`：学生成绩数据
- `data/sales.csv`：销售数据

运行下面的代码，感受一下「读数据 → 看结构」的过程：

```python
import pandas as pd

df = pd.read_csv("data/students.csv")
print("数据形状（行数, 列数）：", df.shape)
print("各列数据类型：")
print(df.dtypes)
print(df.head())
```

几个常用命令先混个脸熟：

| 命令 | 作用 |
| --- | --- |
| `df.head(n)` | 看前 n 行 |
| `df.shape` | 查看行数和列数 |
| `df.info()` | 查看整体信息 |
| `df.describe()` | 生成描述统计（下一章详解） |
| `df["某列"]` | 取某一列 |

## 1.6 本章小结

- 统计数据分析 = 用统计方法 + 计算机，从数据中找规律、得结论。
- 标准流程：提问题 → 收数据 → 清洗 → 探索 → 结论。
- Python 基础：变量、列表、字典、条件、循环、函数。
- NumPy 管数值计算，Pandas 管表格数据，是后面所有章节的基石。

## 练习

1. 用自己的话，写出数据分析的五个步骤。
2. 写一个 Python 函数 `max_score(scores)`，返回列表中的最高分。
3. 用 Pandas 读取 `data/sales.csv`，打印它的 `shape` 和 `head()`。

（答案见 `exercises/练习题.md`）
