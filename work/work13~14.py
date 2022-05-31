

# 13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。


# 14. 题目：打印出如下图案（菱形）:

"""
上面的循环 ：
n=1  3 + 1 + 3
n=2  2 + 3 + 2
n=3  1 + 5 + 1
n=4  0 + 7 + 0

space = " " * (x-n)
star = "*" * (2 * (n-1) + 1)


下面的循环:
n=1  1 + 5
n=2  2 + 3
n=3  3 + 1
space = n * " "
star = (5 - (n-1)*2) * "*"
"""

num = 5         # 总数
x = num - 1     # 循环轮次

for n in range(1,num):
    space = " " * (x-n)
    star = "*" * (2 *(n-1) + 1)
    print(space + star)
    # print(space + star + space)

for n in range(1,4):
    space = n * " "
    star = (5 - (n - 1) * 2) * "*"
    print(space + star)

