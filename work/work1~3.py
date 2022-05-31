
# 用户输入：input("字符串")
# s = input("请输入一个字符:")
# print(s)

# 将字符串转化为整数 ：int(str)  ,注意 ： 只能转化数字的字符串
# a = int('10')
# b = int('c')        # error
# print(type(a))
# print(type(b))

# 1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
# a = input("请输入一个整数:")
# b = input("请输入一个整数:")
# c = input("请输入一个整数:")
# d = input("请输入一个整数:")
#
# print(int(a)+int(b)-int(c)*int(d))



# 2. 打印1~100内被3整除的所有数的和 。
sum = 0
for x in range(1,101):
    if x % 3 == 0:
        sum += x
print(sum)

sum1 = 0
for x in range(3,101,3):
    sum1 += x
print(sum1)

sum2 = 0
x = 1
while x <= 100:
    if x % 3 == 0:
        sum2 += x
    x += 1
print(sum2)
# 3. 使用range()输出1~10内的所有奇数 。
for x in range(1,11,2):
    print(x)
# print(sum3)