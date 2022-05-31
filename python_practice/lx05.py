
# 将一个列表的数据复制到另一个列表中。
lst = [1,2,3,3]
lst1 = [2,3,4,5]
lst.extend(lst1)
print(lst)


# 输出 9*9 乘法口诀表。
for x in range(1,10):
    for y in range(1,x+1):
        print('',y , '*' , x , '=' , y*x,end=' ')
    print()


# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

# xyz = input("请输入一行字符")
# a,b,c,d=0,0,0,0
# for x in xyz:
#     if x.isspace():
#         a += 0
#     elif x.isdigit():
#         b += 0
#     elif x.isalpha():
#         c += 0
#     else:
#         d += 0


# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

"""
2 = 2 * 10 ** 0
22 = 2 * 10 ** 1 +  2 * 10 ** 0
222 = 2 * 10 ** 2 + 2 * 10 ** 1 +  2 * 10 ** 0

==>  第一步 ：找参数
a = 2
循环的次数 ： i
temp = 0

==> 第二步 ：找规律
公式 = a * 10 ** i
temp = a * 10 ** i + temp 
sum = a * 10 ** i + temp
x 代表循环次数 
"""


a = 2
n = input("请输入一个数字:")
n =int(n)
sum = 0
temp = 0
for x in range(n):
    temp += a * 10 ** x
    print(temp)
    sum += temp
print(sum)