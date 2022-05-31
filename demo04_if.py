

# 条件语句

"""
格式 ：
if 条件语句:
    执行代码块
"""

a = 10
if a >13:
    print("a是大于13的数")
else:
    print("a是小于13的数")



""" 多条件判断格式 ：
if 条件判断1:
代码1
elif 条件判断2:
代码2
elif 条件判断3：
代码3
else:
代码4
"""

score = 76
if score > 90:
    print("优秀")
elif score > 80:
    print("良")
elif score > 60:
    print("及格")
else:
    print("不及格")


if score > 75 and score <90 :
    print("良")


if 0:
    print("hello world")


if "abcd":
    print("hello1")

if "":
    print("hello2")



a_str = "hello"
b_str = "helloworld"

print(a_str in b_str)