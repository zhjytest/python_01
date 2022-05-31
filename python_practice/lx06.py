

# 题目：打印出如下图案（菱形）:

"""
上面的图形公式 ： 2(n-1) + 1

n=1  3+1+3
n=2  2 +3 + 2
n=3  1  + 5 + 1
n=4  0  + 7  + 0

print(" " + "*" * (2*(n-1) + 1) + " ")

# 下面的图形公式
n=1 1 + 5 + 1
n=2 2 + 3 + 2
n=3 3  +1 + 3

space = n
star = 5-(n-1)2
"""
# 第一种写法
x = 4
for n in range(1,5):
    space = " " * (x - n)
    star = "*" * (2*(n-1) + 1)
    print(space + star +  space)
for n in range(1,4):
    space = " " * n
    star = (5-(n-1)*2) * "*"
    print(space + star + space)


print("="*20)
x = 4
for n in range(1,5):
    space = " "
    star = "*"
    space *=  (x - n)
    star *=  (2*(n-1) + 1)
    print(space + star + space)
for n in range(1,4):
    space = " "
    star = "*"
    space *=  n
    star *= (5-(n-1)*2)
    print(space + star + space)