# 类的多肽
"""
1. 必须是继承关系
2. 子类中的方法覆盖了父类的方法

继承和多肽的区别 ：
如果说子类直接调用的是父类的方法 ： 继承
如果说子类中的方法直接覆盖了父类的方法 ： 多肽
"""
class People():


    def eat(self,people_type):
        print(people_type,"在吃饭")


class Students(People):

    def eat(self,grade):
        super().eat(grade)
        print(grade,"年级学生正在吃饭")


class Teacher(People):

    def eat(self,subject,time):
        print("{}的老师在{}时间吃饭".format(subject,time))

    def regies(self):
        pass


s = Students()
s.eat("2年级")

print("=========")

t = Teacher()
t.eat("语文学科",'12:00')


