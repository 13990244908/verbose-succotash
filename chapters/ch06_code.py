# -*- coding: utf-8 -*-
"""第 6 章 示例代码：假设检验

用法：
    python chapters/ch06_code.py
"""
import pandas as pd
from scipy import stats

print("=" * 60)
print("第 6 章  假设检验")
print("=" * 60)

df = pd.read_csv("data/students.csv")

ALPHA = 0.05


def report(name, p_value):
    verdict = "拒绝 H₀（差异显著）" if p_value < ALPHA else "不能拒绝 H₀（差异不显著）"
    print(f"{name}: p 值 = {p_value:.4f}  →  {verdict}")


# 1. 单样本 t 检验：数学均值是否等于 75？
print("\n【1】单样本 t 检验：数学均值是否等于 75")
sample = df["数学"].sample(50, random_state=1)
t_stat, p_value = stats.ttest_1samp(sample, popmean=75)
print(f"t 统计量 = {t_stat:.3f}")
report("单样本 t 检验", p_value)

# 2. 双样本 t 检验：男女数学成绩是否不同？
print("\n【2】双样本 t 检验：男生 vs 女生 数学成绩")
male = df[df["性别"] == "男"]["数学"]
female = df[df["性别"] == "女"]["数学"]
t_stat, p_value = stats.ttest_ind(male, female)
print(f"男生均值 = {male.mean():.2f}，女生均值 = {female.mean():.2f}")
print(f"t 统计量 = {t_stat:.3f}")
report("双样本 t 检验", p_value)

# 3. 双样本 t 检验：男女编程成绩是否不同？
print("\n【3】双样本 t 检验：男生 vs 女生 编程成绩")
male_p = df[df["性别"] == "男"]["编程"]
female_p = df[df["性别"] == "女"]["编程"]
t_stat, p_value = stats.ttest_ind(male_p, female_p)
print(f"男生均值 = {male_p.mean():.2f}，女生均值 = {female_p.mean():.2f}")
report("双样本 t 检验", p_value)

# 4. 卡方检验：专业与性别是否相关？
print("\n【4】卡方检验：专业 与 性别 是否相关")
table = pd.crosstab(df["专业"], df["性别"])
print("列联表：")
print(table)
chi2, p_value, dof, expected = stats.chi2_contingency(table)
print(f"卡方统计量 = {chi2:.3f}，自由度 = {dof}")
report("卡方检验", p_value)

print("\n提示：显著性水平 α = 0.05。p < 0.05 才认为差异/相关显著。")
