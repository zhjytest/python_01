


# mian ：__main__ ,每个文件都有一个名字 ，就叫__main__


def div1(x,y):
    try:
        z = x / y
        return z
    except ZeroDivisionError as e:
        print("除法不能出现被0除的情况")
        print(e)


print(div1(4,4))
print(__name__)


if __name__ == '__main__':
    print(div1(3,4))
