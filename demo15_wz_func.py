

# 函数 ： 位置参数 ，参数个数和顺序要一一对应，不能颠倒 。

def add(x,y):
    return x + y


print(add(3,4))
print(add('hello','world'))   # :helloworld
# print(add(3,4,5))
# print()


# 关键字参数 ：调用时使用key:value形式进行调用 。
def student_lesson(grade,subject):
    z = "{}年级上{}课".format(grade,subject)
    return z


print(student_lesson(grade=2,subject='语文'))
print(student_lesson(subject='语文',grade=2))

# 用处 ：实现一个函数 ，参数特别多，调用时不需要记住位置
# connect(host='localhost',username='root',password='root',database,port,commit)


# 默认参数 ： 其中某个参数会有默认值，带有默认值的参数放在最后面。
def study_language(name,language='python'):
    info = ("{}要学习{}语言".format(name,language))
    return info


print(study_language('张三','java'))
print(study_language('李四','python'))
print(study_language('王五'))


