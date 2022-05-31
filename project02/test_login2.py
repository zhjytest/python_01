import sys

from project02.iter03_add_user import login
import unittest

# 1.使用TestSuite()类将测试用例添加到套件中

# 作用 ：就是将用例添加到不同的套件中，以便可以按套件运行,运行时需要借助于其它的类运行，如TestTextRunner。

# 方法1：addTest(testcase) ，testcase代表测试用例 ，常用
# 方法2 ：addTests(tests)  ,tests代表一组测试用例，一般是放在列表中，用的少


# 2. 使用TestTextRunner()类运行测试套件用例
# 方法 ：run(suite)  ,suite传递的是套件


# 问题 ：使用TestSuite()中的addTest去添加测试用例效率太低，若用例少还可以，用例越多越难维护



class TestLogin(unittest.TestCase):


    # # 初始化方法
    # def setUp(self) -> None:
    #     print("开始运行用例",sys._getframe().f_code.co_name)

    # case1 : 输入正确的用户名和正确的密码进行登录
    def test_login_success(self):
        print("开始运行用例", sys._getframe().f_code.co_name)
        except_value = 0
        actual_value = login('admin','123456').get('code')
        self.assertEqual(except_value,actual_value)


    # case2 : 输入错误的用户名或密码进行登录
    def test_user_password_wrong(self):
        print("开始运行用例", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login('admin','1234567').get('code')
        self.assertEqual(except_value,actual_value)


    # case3 : 输入空的用户名或密码
    def test_user_password_null(self):
        print("开始运行用例", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login('admin','').get('code')
        self.assertEqual(except_value,actual_value)


    # def tearDown(self) -> None:
    #     print("开始运行用例", sys._getframe().f_code.co_name)





# 2. 进行测试 -使用断言：assert
# assert 1 == 1
# assert 1 == 2
# assert 3 == 4
# print("abc")


if __name__ == '__main__':
    # unittest.main()         # 代表运行所有用例
    print("==========")

    suite = unittest.TestSuite()
    suite.addTest(TestLogin('test_login_success'))
    suite.addTest(TestLogin('test_user_password_null'))
    print(suite)

    runner = unittest.TextTestRunner()
    runner.run(suite)