# -*- coding: utf-8 -*-
"""第 5 章 示例代码：统计推断（抽样分布与置信区间）

用法：
    python chapters/ch05_code.py
"""
import numpy as np
import pandas as pd
from scipy import stats

print("=" * 60)
print("第 5 章  统计推断：抽样分布与置信区间")
print("=" * 60)

df = pd.read_csv("data/students.csv")
math_all = df["数学"]

# 1. 抽样演示：反复抽样，看样本均值的分布
print("\n【1】反复抽样，观察样本均值的抽样分布")
rng = np.random.default_rng(42)
sample_means = []
for _ in range(1000):
    sample = math_all.sample(50, random_state=rng.integers(0, 10**6))
    sample_means.append(sample.mean())
sample_means = np.array(sample_means)
print("1000 次样本均值的标准差（即标准误估计）：", round(sample_means.std(), 3))
print("理论标准误 = 总体标准差 / √50 ≈", round(math_all.std() / np.sqrt(50), 3))

# 2. 用 t 分布计算置信区间
print("\n【2】「数学」成绩均值的 95% 置信区间")
sample = math_all.sample(50, random_state=7)
n = len(sample)
xbar = sample.mean()
s = sample.std(ddof=1)          # 样本标准差（自由度 n-1）
se = s / np.sqrt(n)             # 标准误
t_crit = stats.t.ppf(0.975, df=n - 1)

ci_low = xbar - t_crit * se
ci_high = xbar + t_crit * se
print(f"样本量 n = {n}")
print(f"样本均值 x̄ = {xbar:.2f}")
print(f"样本标准差 s = {s:.2f}")
print(f"标准误 SE = {se:.2f}")
print(f"95% 置信区间：[{ci_low:.2f}, {ci_high:.2f}]")

# 对比总体真实均值
print(f"总体真实均值 μ = {math_all.mean():.2f}")
print(">>> 观察真实均值是否落在置信区间内")

# 3. 置信水平对区间宽度的影响
print("\n【3】不同置信水平的区间宽度对比")
for level, q in [(0.90, 0.95), (0.95, 0.975), (0.99, 0.995)]:
    t = stats.t.ppf(q, df=n - 1)
    lo = xbar - t * se
    hi = xbar + t * se
    print(f"{int(level*100)}% 置信区间：[{lo:.2f}, {hi:.2f}]  （宽度 {hi-lo:.2f}）")

# 4. scipy 内置的区间计算（更省事）
print("\n【4】用 scipy 一行算置信区间")
ci = stats.t.interval(0.95, df=n - 1, loc=xbar, scale=se)
print("scipy 结果：", (round(ci[0], 2), round(ci[1], 2)))
