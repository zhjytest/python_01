# 类的继承
"""
1. 必须具有父子关系 ，有父类和子类
2. 在子类中可以直接调用父类中的方法(功能)或属性(数据)
"""
class People():

    age = 0

    def eat(self,people_type):
        print(people_type,"在吃饭")


class Students(People):

    pass


class Teacher(People):

    pass

s = Students()
s.eat("学生")
# Students.age = '20'
print(Students.age)

t = Teacher()
# Teacher.age = '40'
print(Teacher.age)
t.eat("老师")