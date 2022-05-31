
# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

astr = "sjfksdjfksd fhfdsd88754359#$%^&dfsdf3"

zf = 0
kg = 0
sz = 0
other = 0

for x in astr:
    if x.isalpha():     # 判断是字符
        zf += 1
    elif x.isdigit():    # 判断是数字
        sz += 1
    elif x.isspace():   # 判断是空格
        kg += 1
    else:
        other += 1
print("字符:",zf)
print("数字:",sz)
print("空格:",kg)
print("其它字符:",other)


