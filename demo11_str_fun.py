

# 字符串方法演示

# 1.连接字符串 ： join(seq)
astr = "+"
bstr = astr.join("world")
print(bstr)


# 2.分割字符串 ： split(str="") ,其中str代表分割符
cstr = "helloworldpythonjavaphp"
dstr = cstr.split("o")
print(dstr)


# 查找字符串 ：find(substr) ,如果找到了返回的是最小索引,没有找到返回-1
estr = "hellowrold"
print(estr.find("l"))
print(estr.find("x"))
print(estr.index("l"))


# 查找以xxx结尾的字符串 ： endswith('xxx')
fstr = "测试报告.doc"
if fstr.endswith('.doc'):
    print("它是一个word文档")


# 替换字符串 ：replace(old_value,new_value)
gstr = "hello world"
hstr = gstr.replace('world','python')
print(hstr)



