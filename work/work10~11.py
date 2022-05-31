

# 10. 将一个列表的数据复制到另一个列表中。
alst = [2,34,675,22]
blst = ['1','ss','dd']
clst = [2,34,675,22]
alst.extend(blst)
print(alst)

# 11. 输出 9*9 乘法口诀表。
for x in range(1,10):
    for y in range(1,x+1):
        print(x,' * ',y,' = ',x * y,end=' ')
    print()


print('helloword',end='++')
print('ssss',end='\n')