#!/usr/bin/env python
# coding=utf-8

import sys

print "Hello World!"

# 不换行输出
print "不换行", "输出"

# 命令行参数
print "文件路径为:", sys.argv[0]
print "参数个数为:", len(sys.argv)
print "参数列表:", str(sys.argv)

# 将一个整数转换为Unicode字符
print unichr(65)
# 将一个整数(小于256)转换为一个字符
print chr(97)
# 十六进制
print hex(8)
# 八进制
print oct(8)

# 幂 - 返回x的y次幂
print 2 ** 3
# 取整除 - 返回商的整数部分（向下取整）
print 9 // 2

# 逻辑运算符
a = 10
b = 20
if a and b:
    print "a 和 b 都为 true"
else:
    print "a 和 b 其中一个为 false"

a = 0
b = 0
if a or b:
    print "a 和 b 其中一个为 true"
else:
    print "a 和 b 都为 false"

a = 30
if not a:
    print "not a 为 true"
else:
    print "not a 为 false"

# 成员运算符
tmp_list = [1, 2, 3, 4, 5, 6, 7]
# in 如果在指定的序列中找到值返回 True，否则返回 False
c = 1
if c in tmp_list:
    print "c 在给定的列表中"
else:
    print "c 不在给定的列表中"
# not in 如果在指定的序列中没有找到值返回 True，否则返回 False
d = 8
if d not in tmp_list:
    print "d 不在给定的列表中"
else:
    print "d 在给定列表中"

# 身份运算符
e = 40
f = 40
# is 是判断两个标识符是不是引用自一个对象
if e is f:
    print "e 和 f 引用的是同一个对象"
else:
    print "e 和 f 引用的是不同的对象"
# is not 是判断两个标识符是不是引用自不同对象
f = 50
if e is not f:
    print "e 和 f 引用的是不同的对象"
else:
    print "e 和 f 引用的是同一个对象"

# 循环语句
fruits = ['banana', 'apple', 'mango']

for fruit in fruits:
    print "当前水果为:", fruit

for index in range(len(fruits)):
    print "第", index + 1, "个水果为:", fruits[index]

# 字符串
print "输出原始字符串", R'"\n"'
print "我的名字是%s,年龄是%s" % ('Miven', 18)

# 列表
print tmp_list
tmp_list.append(8)  # 增
del tmp_list[0]     # 删
tmp_list[1] = 9     # 改
print tmp_list[0]   # 查
print tmp_list

# 字典(Dictionary)
tmp_dic = {"name": "解明智", "age": 18, "id": 1000}
del tmp_dic["id"]                   # 删
tmp_dic["weight"] = 55              # 增
tmp_dic["age"] = 26                 # 改
print "姓名:", tmp_dic["name"]      # 查
print tmp_dic
