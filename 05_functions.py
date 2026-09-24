"""
05 函数（Functions）

学习目标：
- 理解函数是“可重复使用的代码块”
- 掌握 def 定义函数、参数、返回值
- 理解位置参数、默认参数、关键字参数
- 了解局部变量与作用域

如何在 VS Code 中运行：
1. 打开本文件
2. 右键编辑器 → 选择 "Run Python File in Terminal"
3. 或者按 Ctrl + F5（不调试直接运行）
"""

print("=" * 40)
print("1. 什么是函数？")
print("=" * 40)

# 函数就是一段起个名字的代码，可以反复调用
def greet():
    print("你好！欢迎来到 Python 学习班。")

# 调用函数
greet()
greet()      # 可以重复调用


print()
print("=" * 40)
print("2. 带参数的函数")
print("=" * 40)

def greet_user(name):
    print(f"你好，{name}！")

greet_user("张三")
greet_user("李四")

# 函数可以有多个参数
def add(a, b):
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")


print()
print("=" * 40)
print("3. 返回值")
print("=" * 40)

def circle_area(radius):
    """根据半径计算圆面积"""
    return 3.14 * radius ** 2

area = circle_area(3)
print(f"半径为 3 的圆面积是: {area:.2f}")

# 函数可以返回多个值（实际是返回元组）
def min_max(numbers):
    return min(numbers), max(numbers)

smallest, largest = min_max([4, 1, 7, 3, 9])
print(f"最小值: {smallest}, 最大值: {largest}")


print()
print("=" * 40)
print("4. 默认参数")
print("=" * 40)

def make_coffee(size="中杯", sugar=True):
    sugar_text = "加糖" if sugar else "不加糖"
    print(f"制作一杯 {size} 咖啡，{sugar_text}")

make_coffee()                          # 用默认值
make_coffee("大杯")                     # 只改第一个参数
make_coffee(size="小杯", sugar=False)   # 用关键字参数


print()
print("=" * 40)
print("5. 关键字参数与任意参数")
print("=" * 40)

def describe_person(name, age, city="北京"):
    print(f"{name} 今年 {age} 岁，来自 {city}")

# 关键字参数顺序可以任意
describe_person(age=20, name="王五")

# *args：接收任意多个位置参数
def total(*numbers):
    result = 0
    for n in numbers:
        result += n
    return result

print(f"total(1, 2, 3) = {total(1, 2, 3)}")
print(f"total(10, 20) = {total(10, 20)}")

# **kwargs：接收任意多个关键字参数
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("学生信息:")
print_info(name="赵六", age=19, major="计算机")


print()
print("=" * 40)
print("6. 局部变量与作用域")
print("=" * 40)

outside = "我在函数外面"

def demo():
    inside = "我在函数里面"
    print("函数内访问 inside:", inside)
    print("函数内访问 outside:", outside)   # 函数内可以读取外部变量

demo()
# print(inside)  # 取消注释会报错：inside 只在函数内有效

# 如果要在函数内修改外部变量，需要用 global
counter = 0

def increment():
    global counter
    counter += 1
    print(f"counter = {counter}")

increment()
increment()


print()
print("=" * 40)
print("7. 文档字符串（docstring）")
print("=" * 40)

def calculate_bmi(weight, height):
    """
    计算 BMI 指数。

    参数:
        weight: 体重，单位公斤
        height: 身高，单位米

    返回:
        BMI 值
    """
    return weight / (height ** 2)

bmi = calculate_bmi(70, 1.75)
print(f"BMI = {bmi:.2f}")
print("函数文档:", calculate_bmi.__doc__)


print()
print("=" * 40)
print("本节小结")
print("=" * 40)
print("- 函数用 def 定义，起个名字，可反复调用")
print("- 参数让函数更灵活：位置参数、默认参数、关键字参数")
print("- return 用于把结果传回调用处")
print("- *args 接收任意多个位置参数，**kwargs 接收任意多个关键字参数")
print("- 局部变量只在函数内可见；global 可修改外部变量")
print("- 养成写 docstring 的好习惯")
