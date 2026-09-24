"""
01 变量（Variables）

学习目标：
- 理解变量是“给数据贴的标签”
- 掌握变量命名规则
- 区分整型、浮点型、字符串、布尔型、空值
- 了解 Python 是动态类型语言

如何在 VS Code 中运行：
1. 打开本文件
2. 右键编辑器 → 选择 "Run Python File in Terminal"
3. 或者按 Ctrl + F5（不调试直接运行）
"""

print("=" * 40)
print("1. 变量就是给数据贴的标签")
print("=" * 40)

age = 25                 # 整数（int）
height = 1.75            # 浮点数（float）
name = "张三"            # 字符串（str）
is_student = True        # 布尔值（bool）
nothing = None           # 空值（NoneType）

print("年龄:", age, "类型:", type(age))
print("身高:", height, "类型:", type(height))
print("姓名:", name, "类型:", type(name))
print("是否学生:", is_student, "类型:", type(is_student))
print("空值:", nothing, "类型:", type(nothing))


print()
print("=" * 40)
print("2. 变量命名规则")
print("=" * 40)

# 合法命名
user_name = "小明"
_score = 90
PI = 3.14159              # 大写通常表示常量
student2 = "小红"

# 不合法命名示例（被注释掉，取消注释会报错）
# 2student = "小红"      # 不能以数字开头
# my-name = "小明"       # 不能含连字符
# class = "三班"         # 不能用 Python 关键字

print("合法变量示例:", user_name, _score, PI, student2)
print("提示：Python 关键字不能作为变量名，例如 class / if / for / def / True / None")


print()
print("=" * 40)
print("3. 变量可以重新赋值，类型也会随之改变")
print("=" * 40)

x = 100
print("x 是整数:", x, type(x))

x = "一百"               # 同一个变量现在变成字符串
print("x 变成字符串:", x, type(x))

# 这种不需要事先声明类型的特性，叫做“动态类型”


print()
print("=" * 40)
print("4. 多变量同时赋值")
print("=" * 40)

a, b, c = 1, 2, 3
print("a, b, c =", a, b, c)

m = n = 0               # 多个变量指向同一个初始值
print("m, n =", m, n)


print()
print("=" * 40)
print("5. 删除变量")
print("=" * 40)

temp = "临时数据"
print("删除前:", temp)
del temp
# print(temp)            # 取消注释会报错：NameError: name 'temp' is not defined
print("temp 已被删除（再访问会报错）")


print()
print("=" * 40)
print("本节小结")
print("=" * 40)
print("- 变量 = 名字 + 数据；用 = 赋值")
print("- 命名：字母/下划线开头，区分大小写，不能用关键字")
print("- Python 是动态类型：变量类型由当前值决定")
print("- 常用类型：int、float、str、bool、NoneType")
