
# 字典

# 1. 字典的定义 ： 变量名 = {key1:value1 , key2:value2}

dct1 = {}
dct2 = {'a':1,'b':2,'c':3}
print(dct1)
print(dct2)

# 2. 字典的获取 : dict['键名']
print("获取字典dct2中键名为b的值:",dct2['b'])
# print("获取字典dct2中键名为d的值:",dct2['d'])     # 键名不存在会报错

# 字典的获取 ：dict.get(键名)
print("获取字典dct2中键名为b的值:",dct2.get('b'))
print("获取字典dct2中键名为d的值:",dct2.get('d'))

# 3. 更新字典的某个值 ：dict['键名'] = 新值
dct2['c'] = 31
print(dct2)


# 4. 更新字典里的值到另外一个字典 ：dict.update(dict1)
dct3 = {'e':22,'f':'hello'}
dct2.update(dct3)
print("更新后的字典显示:",dct2)

# 5. 判断字典中是否存在某个键名 : '键名' in dict
print('e' in dct2)
print('g' in dct2)

# 6.获取字典中所有的键名 ： dict.keys()
print("获取字典中所有的键名:",dct2.keys())

for x in dct2.keys():
    print(x)

# 7.获取字典中所有的值 ：dict.values()
print("获取字典中所有的值:",dct2.values())
for x in dct2.values():
    print(x)

# 8.获取字典中所有的键值对 ：dict.items()
print("获取字典中所有的键值对:",dct2.items())
for x,y in dct2.items():
    print(x,"======",y)

