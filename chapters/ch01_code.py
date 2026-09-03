# -*- coding: utf-8 -*-
"""第 1 章 示例代码：数据分析与 Python 入门

运行前请先执行一次 `python generate_data.py` 生成示例数据。
用法：
    python chapters/ch01_code.py
"""
import numpy as np
import pandas as pd

print("=" * 60)
print("第 1 章  数据分析与 Python 入门")
print("=" * 60)

# 1. 变量与数据类型
print("\n【1】变量与数据类型")
name = "小明"
age = 20
height = 1.75
is_student = True
print(name, age, height, is_student)

# 2. 列表与字典
print("\n【2】列表与字典")
scores = [85, 90, 78, 92]
print("列表：", scores)
print("第一个元素：", scores[0])

student = {"姓名": "小明", "数学": 85, "英语": 90}
print("字典：", student)
print("数学成绩：", student["数学"])

# 3. 条件与循环
print("\n【3】条件与循环")
for s in scores:
    if s >= 90:
        print(f"{s} 分：优秀")
    elif s >= 60:
        print(f"{s} 分：及格")
    else:
        print(f"{s} 分：不及格")

# 4. 函数
print("\n【4】函数")


def average(nums):
    return sum(nums) / len(nums)


print("平均分：", average(scores))

# 5. NumPy 数组
print("\n【5】NumPy 数组")
arr = np.array([1, 2, 3, 4, 5])
print("数组：", arr)
print("均值：", arr.mean())
print("最大值：", arr.max())

# 6. Pandas 读取数据
print("\n【6】Pandas 读取示例数据")
df = pd.read_csv("data/students.csv")
print("数据形状（行数, 列数）：", df.shape)
print("\n各列数据类型：")
print(df.dtypes)
print("\n前 5 行：")
print(df.head())
print("\n整体信息：")
df.info()
