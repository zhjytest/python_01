



# 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
a = 120
if 1<= a <= 100:
    print(a)


# 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
x = input("请输入一个整数:")
y = input("请输入一个整数:")
z = input("请输入一个整数:")
alst = []
alst.append(int(x))
alst.append(int(y))
alst.append(int(z))
alst.sort()
print(alst)
