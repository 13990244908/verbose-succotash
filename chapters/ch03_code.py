# -*- coding: utf-8 -*-
"""第 3 章 示例代码：数据可视化

用法：
    python chapters/ch03_code.py
生成的图片会保存到本目录下（fig_hist.png 等）。
"""
import matplotlib

# 设置中文字体，避免中文显示为方块
matplotlib.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
matplotlib.rcParams["axes.unicode_minus"] = False

import matplotlib.pyplot as plt
import pandas as pd

print("=" * 60)
print("第 3 章  数据可视化")
print("=" * 60)

students = pd.read_csv("data/students.csv")
sales = pd.read_csv("data/sales.csv")

# 1. 直方图：数学成绩分布
plt.figure(figsize=(8, 5))
plt.hist(students["数学"], bins=20, color="skyblue", edgecolor="black")
plt.xlabel("数学成绩")
plt.ylabel("人数")
plt.title("数学成绩分布")
plt.savefig("chapters/fig_hist.png", dpi=150)
print("已保存：chapters/fig_hist.png")

# 2. 箱线图：数学 vs 英语
plt.figure(figsize=(8, 5))
plt.boxplot([students["数学"], students["英语"]], tick_labels=["数学", "英语"])
plt.ylabel("成绩")
plt.title("数学与英语成绩箱线图")
plt.savefig("chapters/fig_box.png", dpi=150)
print("已保存：chapters/fig_box.png")

# 3. 散点图：数学 vs 英语 的关系
plt.figure(figsize=(8, 5))
plt.scatter(students["数学"], students["英语"], alpha=0.5)
plt.xlabel("数学")
plt.ylabel("英语")
plt.title("数学 vs 英语")
plt.savefig("chapters/fig_scatter.png", dpi=150)
print("已保存：chapters/fig_scatter.png")

# 4. 柱状图：各专业人数
plt.figure(figsize=(8, 5))
counts = students["专业"].value_counts()
plt.bar(counts.index, counts.values, color="orange", edgecolor="black")
plt.xlabel("专业")
plt.ylabel("人数")
plt.title("各专业人数")
plt.savefig("chapters/fig_bar.png", dpi=150)
print("已保存：chapters/fig_bar.png")

# 5. 柱状图：各品类总销售额
plt.figure(figsize=(8, 5))
cat_sales = sales.groupby("品类")["销售额"].sum()
plt.bar(cat_sales.index, cat_sales.values, color="lightgreen", edgecolor="black")
plt.xlabel("品类")
plt.ylabel("总销售额")
plt.title("各品类总销售额")
plt.savefig("chapters/fig_sales.png", dpi=150)
print("已保存：chapters/fig_sales.png")

print("\n全部图片已生成完毕，可打开 chapters/ 目录查看。")
