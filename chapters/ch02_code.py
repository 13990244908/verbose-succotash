# -*- coding: utf-8 -*-
"""第 2 章 示例代码：描述统计

用法：
    python chapters/ch02_code.py
"""
import pandas as pd

print("=" * 60)
print("第 2 章  描述统计：集中趋势与离散程度")
print("=" * 60)

df = pd.read_csv("data/students.csv")

# 1. 集中趋势
print("\n【1】集中趋势 —— 以「数学」成绩为例")
math = df["数学"]
print("均值 mean  ：", round(math.mean(), 2))
print("中位数 median：", math.median())
print("众数 mode   ：", list(math.mode()))

# 2. 离散程度
print("\n【2】离散程度 —— 以「数学」成绩为例")
print("极差 range  ：", round(math.max() - math.min(), 2))
print("方差 var    ：", round(math.var(), 2))
print("标准差 std  ：", round(math.std(), 2))
print("下四分位数 Q1：", math.quantile(0.25))
print("上四分位数 Q3：", math.quantile(0.75))
print("四分位距 IQR ：", round(math.quantile(0.75) - math.quantile(0.25), 2))

# 3. 演示均值对极端值的敏感性
print("\n【3】均值 vs 中位数：谁更稳健？")
demo = [5000, 5200, 4800, 5300, 100000]
demo_series = pd.Series(demo)
print("数据：", demo)
print("均值  ：", demo_series.mean())
print("中位数：", demo_series.median())
print(">>> 中位数更能代表大多数人的收入水平")

# 4. describe() 一键描述统计
print("\n【4】describe() 一键生成描述统计")
print(df[["数学", "英语", "编程"]].describe().round(2))

# 5. 分组描述统计（按性别看各科均值）
print("\n【5】按「性别」分组的各科均值")
print(df.groupby("性别")[["数学", "英语", "编程"]].mean().round(2))
