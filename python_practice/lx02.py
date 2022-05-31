
# 2. 打印1~100内被3整除的所有数的和 。
sum = 0
for x in range(3,100,3):
    sum += x
print(sum)


# 3. 使用range()输出1~10内的所有奇数 。
for x in range(1,10,2):
    print(x)

# 2. 打印1~100所有偶数的和 减去 所有奇数的和 的值
ous,jis = 0,0

for x in range(1,101):
    if x % 2 ==0 :
        ous += x
    else:
        jis += x

print(ous - jis)
# 3. 求1+2+3+...+100的和
sum = 0
for x in range(1,101):
    sum += x
print(sum)


# 判断一个数n能同时被3和5整除
a = input("请输入一个整数:")
if int(a) % 3 == 0 and int(a) % 5 == 0 :
    print(a,"能被3和5同时整除")
else:
    print(a, "不能被3和5同时整除")