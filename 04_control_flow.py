"""
04 流程控制（Control Flow）

学习目标：
- 掌握 if / elif / else 分支
- 掌握 for 循环和 while 循环
- 理解 break、continue、else（循环 else）
- 理解缩进在 Python 中的重要性

如何在 VS Code 中运行：
1. 打开本文件
2. 右键编辑器 → 选择 "Run Python File in Terminal"
3. 或者按 Ctrl + F5（不调试直接运行）
"""

print("=" * 40)
print("1. if / elif / else 分支")
print("=" * 40)

score = 78

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"分数 {score} 对应的等级是: {grade}")

# 嵌套 if
age = 25
has_ticket = True

if has_ticket:
    if age >= 18:
        print("请入场（成人票）")
    else:
        print("请入场（儿童票）")
else:
    print("请先购票")


print()
print("=" * 40)
print("2. for 循环：遍历序列")
print("=" * 40)

# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
print("水果清单:")
for fruit in fruits:
    print("  -", fruit)

# 遍历 range
print("\n0 到 4 的整数:")
for i in range(5):
    print(i, end=" ")
print()

print("1 到 10 的偶数:")
for i in range(2, 11, 2):
    print(i, end=" ")
print()

# 遍历字符串
word = "Python"
print("\n逐字符打印:")
for char in word:
    print(char, end=" ")
print()


print()
print("=" * 40)
print("3. while 循环：条件满足就继续")
print("=" * 40)

# 示例：计算 1 加到 100
n = 1
total = 0
while n <= 100:
    total += n
    n += 1
print(f"1 + 2 + ... + 100 = {total}")

# 示例：倒计时
count = 3
while count > 0:
    print(f"倒计时: {count}")
    count -= 1
print("发射！")


print()
print("=" * 40)
print("4. break 与 continue")
print("=" * 40)

# break：立即结束整个循环
print("找到第一个能被 7 整除的数:")
for num in range(1, 30):
    if num % 7 == 0:
        print(f"找到了: {num}")
        break

# continue：跳过当前轮次，进入下一轮
print("\n跳过 3 的倍数，打印 1-10 其他数:")
for num in range(1, 11):
    if num % 3 == 0:
        continue
    print(num, end=" ")
print()


print()
print("=" * 40)
print("5. 循环的 else 子句")
print("=" * 40)

# 当循环正常结束（没有被 break）时，else 会执行
for num in range(2, 10):
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} = {i} * {num // i}")
            break
    else:
        # 这个 else 对应的是内层 for 循环
        print(f"{num} 是质数")


print()
print("=" * 40)
print("6. 缩进是 Python 的语法！")
print("=" * 40)

# 同一代码块必须使用相同数量的缩进（通常 4 个空格）
if True:
    print("这一行属于 if 块")
    print("这一行也属于 if 块")
print("这一行不属于 if 块")

# 不要混用 Tab 和空格，VS Code 右下角可以设置缩进为空格 4


print()
print("=" * 40)
print("本节小结")
print("=" * 40)
print("- 分支：if / elif / else，条件为 True 才执行")
print("- for：遍历可迭代对象（列表、字符串、range 等）")
print("- while：条件为 True 时重复执行")
print("- break：跳出整个循环；continue：跳过本次")
print("- 循环正常结束时，else 子句可执行")
print("- Python 用缩进表示代码块，必须保持一致")
