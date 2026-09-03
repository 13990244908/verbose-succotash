# -*- coding: utf-8 -*-
"""生成示例数据集（可复现）。

用法：
    python generate_data.py

会在 data/ 目录下生成：
    - students.csv   学生成绩数据（200 名学生）
    - sales.csv      销售数据（某店铺 60 天记录）

随机种子固定，保证每次生成结果完全一致，方便教学演示。
"""
import os

import numpy as np
import pandas as pd

# 固定随机种子，保证可复现
rng = np.random.default_rng(42)

os.makedirs("data", exist_ok=True)


def gen_students() -> pd.DataFrame:
    """生成学生成绩数据。"""
    n = 200
    # 学号：2024001 ~ 2024200
    student_ids = [f"2024{i:04d}" for i in range(1, n + 1)]
    gender = rng.choice(["男", "女"], size=n, p=[0.45, 0.55])
    major = rng.choice(["计算机", "经济学", "统计学", "文学"], size=n)

    # 三门成绩：用正态分布模拟，含一定随机波动
    math = np.clip(rng.normal(72, 12, n), 0, 100).round(1)
    english = np.clip(rng.normal(70, 14, n), 0, 100).round(1)
    programming = np.clip(rng.normal(68, 15, n), 0, 100).round(1)

    return pd.DataFrame(
        {
            "学号": student_ids,
            "性别": gender,
            "专业": major,
            "数学": math,
            "英语": english,
            "编程": programming,
        }
    )


def gen_sales() -> pd.DataFrame:
    """生成某店铺 60 天的销售记录。"""
    n_days = 60
    categories = ["食品", "日用品", "家电"]

    dates = pd.date_range("2025-01-01", periods=n_days, freq="D")
    # 每个日期随机出现 1~3 个品类
    records = []
    for d in dates:
        n_cat = int(rng.integers(1, 4))
        chosen = rng.choice(categories, size=n_cat, replace=False)
        for cat in chosen:
            if cat == "食品":
                sales = rng.normal(800, 150)
                qty = sales / rng.uniform(10, 20)
            elif cat == "日用品":
                sales = rng.normal(500, 120)
                qty = sales / rng.uniform(20, 40)
            else:  # 家电
                sales = rng.normal(3000, 800)
                qty = sales / rng.uniform(200, 500)
            records.append(
                {
                    "日期": d.strftime("%Y-%m-%d"),
                    "品类": cat,
                    "销售额": round(float(sales), 2),
                    "销量": round(float(qty), 2),
                }
            )

    return pd.DataFrame(records)


if __name__ == "__main__":
    students = gen_students()
    sales = gen_sales()

    students.to_csv("data/students.csv", index=False, encoding="utf-8-sig")
    sales.to_csv("data/sales.csv", index=False, encoding="utf-8-sig")

    print("已生成示例数据：")
    print(f"  data/students.csv  （{len(students)} 行）")
    print(f"  data/sales.csv     （{len(sales)} 行）")
    print("\nstudents.csv 预览：")
    print(students.head())
    print("\nsales.csv 预览：")
    print(sales.head())
