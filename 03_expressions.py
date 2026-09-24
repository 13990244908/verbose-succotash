"""
03 表达式（Expressions）

学习目标：
- 理解表达式是由变量、字面量、运算符组成的“可求值的式子”
- 掌握类型转换、字符串格式化、输入输出
- 学会把复杂需求拆成若干表达式逐步实现

如何在 VS Code 中运行：
1. 打开本文件
2. 右键编辑器 → 选择 "Run Python File in Terminal"
3. 或者按 Ctrl + F5（不调试直接运行）
"""

print("=" * 40)
print("1. 什么是表达式？")
print("=" * 40)

# 表达式就是可以被 Python 求值并返回一个值的式子
print("字面量表达式:", 3 + 5)           # 8
print("变量表达式:", 10 * 2)            # 20

radius = 5
area = 3.14 * radius ** 2              # 右边整体就是一个表达式
print(f"半径为 {radius} 的圆面积:", area)


print()
print("=" * 40)
print("2. 类型转换")
print("=" * 40)

# int()：把可转换的对象转成整数
print("int('123') =", int("123"))
print("int(3.7) =", int(3.7))          # 截断小数，不是四舍五入

# float()：转成浮点数
print("float('3.14') =", float("3.14"))
print("float(5) =", float(5))

# str()：转成字符串
print("str(100) =", str(100))
print("str(True) =", str(True))

# bool()：转成布尔值
print("bool(1) =", bool(1))
print("bool(0) =", bool(0))
print("bool('') =", bool(""))
print("bool('hello') =", bool("hello"))

# 常见坑：字符串拼接不能和数字直接混用
age = 25
# print("我今年" + age + "岁")          # 会报错！
print("正确做法:", "我今年" + str(age) + "岁")


print()
print("=" * 40)
print("3. 字符串格式化")
print("=" * 40)

name = "李明"
score = 92.5

# 方式一：% 占位符（较老，了解即可）
print("%s 考了 %.1f 分" % (name, score))

# 方式二：str.format()
print("{} 考了 {:.1f} 分".format(name, score))

# 方式三：f-string（推荐，最直观）
print(f"{name} 考了 {score:.1f} 分")

# f-string 里还能直接写表达式
print(f"{name} 的成绩是 {score}，四舍五入为 {round(score)} 分")


print()
print("=" * 40)
print("4. 输入与输出")
print("=" * 40)

# input() 得到的一定是字符串
# 下面这行注释掉了，因为需要手动输入。你可以在 VS Code 里取消注释后运行体验：
# user_input = input("请输入一个数字: ")
# number = int(user_input)
# print(f"你输入的数字是 {number}，它的平方是 {number ** 2}")

# 为了在自动运行时也能看到输出，这里用固定值模拟
user_input = "7"
number = int(user_input)
print(f"假设输入的是 {number}，它的平方是 {number ** 2}")


print()
print("=" * 40)
print("5. 表达式的组合")
print("=" * 40)

# 把复杂计算拆成多个表达式，可读性更好
price = 199
quantity = 3
discount = 0.85

subtotal = price * quantity            # 小计
final_price = subtotal * discount      # 折后价
print(f"单价 {price}，数量 {quantity}，折扣 {discount}")
print(f"小计: {subtotal}，折后价: {final_price:.2f}")


print()
print("=" * 40)
print("本节小结")
print("=" * 40)
print("- 表达式 = 可以被求值并返回结果的式子")
print("- 类型转换：int()、float()、str()、bool()")
print("- 字符串格式化推荐用 f-string：f'{变量:.1f}'")
print("- input() 返回字符串，做计算前要转换类型")
print("- 复杂表达式可拆成多个小表达式，提高可读性")
