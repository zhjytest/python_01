

# 实例变量

# 实例: 创建学生类，要求有属性：姓名和年级 ; 方法有：学习的方法，打印学生的上课情况
class Students():

    # name = "张三"
    # grade = "5年级"


    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        sex = '男'



    def study(self):
        print("这里的self是:",self)
        score = 60



    def eat(self):
        print(self.name,"是",self.grade,"正在吃饭")



s1 = Students('张三','5年级')
print(s1.eat())
