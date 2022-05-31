

# 序列的通用操作

# 1. 索引: seq[index] ,index 代表的下标，默认从0开始 ; 索引支持：列表，元祖 ，字符串
lst = ['red','hello',2,3.5]
print(lst[1])          # 列表里的第二个值
print(lst[-1])

tp = ('red','hello',2,3.5)
print(tp[1])
print(tp[-1])

my_str = "redhello2"
print(my_str[1])
print(my_str[-1])


# 2. 序列的切片: seq[start:end:step] ,start代表位置，默认是从0开始，
# end是代表结束位置，如果不填写，代表列表的长度 ，step代表的是步长，默认是1
lst5 = ['red','green','blue','black','gold','orange']
print(lst5[1:5:1])      #获取第2个-5个元素
print(lst5[1:6:2])      #获取的偶数的值

print(lst5[::2])           # 省略了start和end
print(lst5[0:6:2])


print(lst5[2:])             # 省略了end和step
print(lst5[2:6:1])
print(lst5[2::])


print(lst5[1::2])           # 省略的是end

print(lst5[:3:])            # 省略的是start和step

print(lst5[::])
# print(lst5[])

# 列表中有10个元素 ，让你取出其中奇数个数的元素


# 3. 序列的相加和相乘: + , *

alst = [1,2]
blst = [3,4]
clst = alst +blst
print(clst)
astr = 'hello'
bstr = 'python'
print(astr + bstr)

dlst = alst * 2
print(dlst)

elst = [None] * 3
print(elst)

print("=======================")
print("=" * 60)


# 检查元素 ： in ,针对的是列表，字符串，元祖

lst6 = ['red','green','blue','black','gold','orange']

print('gold' in lst6)
print('gold1' in lst6)


# 序列中的方法 ：list()
# klst = []
print("="*20)
klst = list()
print(klst)
cstr = "abc"
mlst = list(cstr)
print(mlst)

nlst = [1,2,3]
dstr = str(nlst)
print("dstr:",dstr)
print(type(dstr))
estr = str(23)
print(type(estr))


#
lst7 = ['red','green','blue','black','gold','orange']
for x in lst7:
    print(x,end=' ')

# 循环序列中的索引和值
for index,vls in enumerate(lst7):
    print(index,'=====',vls)
