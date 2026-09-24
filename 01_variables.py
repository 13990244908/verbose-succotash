"""
01 变量（Variables）

学习目标：
- 理解变量是“给数据贴的标签”
- 掌握变量命名规则
- 掌握基本类型：整数、浮点数、布尔值、字符串、空值
- 掌握容器类型：list（列表）、tuple（元组）、set（集合）、dict（字典）
- 理解 Python 是动态类型语言：同一个变量可以先装字符串，再装数值

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
print("2. 容器类型：list / tuple / set / dict")
print("=" * 40)

# list 列表：有序、可修改，用方括号 []
scores = [85, 92, 78]
print("list 列表:", scores, "类型:", type(scores))
scores[0] = 90                      # 可以修改元素
print("  修改后:", scores)

# tuple 元组：有序、不可修改，用圆括号 ()
point = (3, 5)
print("tuple 元组:", point, "类型:", type(point))
# point[0] = 10                     # 取消注释会报错：元组不可修改
print("  元组创建后不能修改元素")

# set 集合：无序、自动去重，用花括号 {}
unique_nums = {1, 2, 2, 3, 3, 3}
print("set 集合:", unique_nums, "类型:", type(unique_nums))
print("  集合会自动去重，重复的 2 和 3 只保留一个")

# dict 字典：键值对，用 {键: 值}
student = {"姓名": "张三", "年龄": 20, "专业": "计算机"}
print("dict 字典:", student, "类型:", type(student))
print("  按键取值:", student["姓名"])

print()
print("注意：{} 表示空字典，不是空集合；空集合要用 set()")
empty_dict = {}
empty_set = set()
print("  {} 的类型:", type(empty_dict))
print("  set() 的类型:", type(empty_set))


print()
print("=" * 40)
print("3. 变量命名规则")
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
print("4. 变量的类型是可以变的（动态类型）")
print("=" * 40)

# 重点：同一个变量可以先装字符串，再装数值，类型随之改变
value = "一百"
print("value 现在是字符串:", value, type(value))

value = 100               # 同一个变量改成整数
print("value 现在是整数:", value, type(value))

value = 3.14              # 再改成浮点数
print("value 现在是浮点数:", value, type(value))

print("这就是 Python 的“动态类型”：类型由当前装的值决定，不需要事先声明")


print()
print("=" * 40)
print("5. 多变量同时赋值")
print("=" * 40)

a, b, c = 1, 2, 3
print("a, b, c =", a, b, c)

m = n = 0               # 多个变量指向同一个初始值
print("m, n =", m, n)


print()
print("=" * 40)
print("6. 删除变量")
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
print("- 基本类型：int（整数）、float（浮点数）、bool（布尔）、str（字符串）、None（空值）")
print("- 容器类型：list（有序可变）、tuple（有序不可变）、set（无序去重）、dict（键值对）")
print("- 注意：{} 是空字典，空集合要写 set()")
print("- Python 是动态类型：同一个变量可以先装字符串，再装数值")
