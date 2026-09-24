"""
02 运算符（Operators）

学习目标：
- 掌握算术、比较、赋值、逻辑、成员、身份运算符
- 掌握取整的三种方式（//、int()、round()）与取余（%）
- 理解运算符优先级
- 能在实际场景中正确选用运算符

如何在 VS Code 中运行：
1. 打开本文件
2. 右键编辑器 → 选择 "Run Python File in Terminal"
3. 或者按 Ctrl + F5（不调试直接运行）
"""

print("=" * 40)
print("1. 算术运算符")
print("=" * 40)

a, b = 17, 5
print(f"{a} + {b} =", a + b)      # 加法
print(f"{a} - {b} =", a - b)      # 减法
print(f"{a} * {b} =", a * b)      # 乘法
print(f"{a} / {b} =", a / b)      # 除法，结果一定是浮点数
print(f"{a} // {b} =", a // b)    # 整除，只保留整数部分
print(f"{a} % {b} =", a % b)      # 取余/取模
print(f"{a} ** {b} =", a ** b)    # 幂运算，17 的 5 次方

print()
print("整除与取余的常见用法：判断奇偶")
number = 42
print(f"{number} 是", "偶数" if number % 2 == 0 else "奇数")


print()
print("=" * 40)
print("1b. 取整的三种方式（重点区分）")
print("=" * 40)

# 方式一：// 整除，向下取整（往更小的方向）
# 方式二：int() 截断，直接去掉小数（往 0 的方向）
# 方式三：round() 四舍五入

print("正数时三者差别不大:")
print(f"  7 // 2      = {7 // 2}")
print(f"  int(7 / 2)  = {int(7 / 2)}")
print(f"  round(7 / 2)= {round(7 / 2)}")

print()
print("负数时 // 和 int() 结果不同（易踩坑）:")
print(f"  -7 // 2     = {-7 // 2}     # 向下取整，取更小的 -4")
print(f"  int(-7 / 2) = {int(-7 / 2)}     # 向 0 截断，取 -3")

print()
print("取余 % 的用法:")
print(f"  17 % 5 = {17 % 5}              # 17 除以 5 余 2")
print(f"  判断能否整除: 17 % 5 == 0 → {17 % 5 == 0}")
print(f"  20 % 5 == 0 → {20 % 5 == 0}          # 20 能被 5 整除")
print(f"  循环取值: 索引 7 在长度 5 的列表中对应 {7 % 5}")

print()
print("提示：round() 采用“银行家舍入”，round(2.5) =", round(2.5), "（取最近的偶数）")


print()
print("=" * 40)
print("2. 比较运算符")
print("=" * 40)

print(f"{a} == {b}:", a == b)     # 等于
print(f"{a} != {b}:", a != b)     # 不等于
print(f"{a} > {b}:", a > b)       # 大于
print(f"{a} < {b}:", a < b)       # 小于
print(f"{a} >= {b}:", a >= b)     # 大于等于
print(f"{a} <= {b}:", a <= b)     # 小于等于

# 比较结果是一个布尔值
result = a > b
print(f"比较结果 result 的类型是: {type(result)}")


print()
print("=" * 40)
print("3. 赋值运算符")
print("=" * 40)

x = 10
print(f"初始 x = {x}")

x += 3          # 等价于 x = x + 3
print(f"x += 3 后: {x}")

x -= 2          # 等价于 x = x - 2
print(f"x -= 2 后: {x}")

x *= 4          # 等价于 x = x * 4
print(f"x *= 4 后: {x}")

x //= 5         # 等价于 x = x // 5
print(f"x //= 5 后: {x}")

# 还有 **=、%=、/= 等，用法相同


print()
print("=" * 40)
print("4. 逻辑运算符")
print("=" * 40)

sunny = True
warm = False

print("晴天且温暖:", sunny and warm)     # 两者都为 True，结果才为 True
print("晴天或温暖:", sunny or warm)       # 只要有一个为 True，结果就为 True
print("不是晴天:", not sunny)             # 取反

age = 20
print(f"是否成年且是学生: {age >= 18 and age <= 25}")


print()
print("=" * 40)
print("5. 成员运算符与身份运算符")
print("=" * 40)

fruits = ["苹果", "香蕉", "橙子"]
print("苹果 在 fruits 里吗？", "苹果" in fruits)
print("西瓜 不在 fruits 里吗？", "西瓜" not in fruits)

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("x == y（值相等）:", x == y)
print("x is y（同一对象）:", x is y)      # False，两个不同列表
print("x is z（同一对象）:", x is z)      # True，z 就是 x


print()
print("=" * 40)
print("6. 运算符优先级")
print("=" * 40)

# 优先级：括号 > 幂 ** > 正负号 > 乘除取整除取余 > 加减 > 比较 > 赋值
value = 2 + 3 * 4 ** 2
print("2 + 3 * 4 ** 2 =", value)          # 先算 4**2=16，再 3*16=48，最后 2+48=50

# 不确定时，用括号让意图更清晰
value2 = (2 + 3) * 4 ** 2
print("(2 + 3) * 4 ** 2 =", value2)     # 先算括号里的 5，再 5*16=80


print()
print("=" * 40)
print("本节小结")
print("=" * 40)
print("- 算术：+ - * / //（整除）%（取余）**（幂）")
print("- 取整三种：// 向下取整、int() 向 0 截断、round() 四舍五入")
print("- 负数取整要小心：-7 // 2 = -4，但 int(-7/2) = -3")
print("- 比较：== != > < >= <=，结果是 bool")
print("- 赋值：+= -= *= //= 等，先运算再赋值")
print("- 逻辑：and、or、not，用于组合条件")
print("- 成员：in / not in，判断是否在序列中")
print("- 身份：is / is not，判断是否为同一对象")
print("- 优先级拿不准时，用括号 () 明确顺序")
