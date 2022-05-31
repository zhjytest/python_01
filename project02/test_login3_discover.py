import sys

from project02.iter03_add_user import login
import unittest


# 问题 ：使用TestSuite()中的addTest去添加测试用例效率太低，若用例少还可以，用例越多越难维护

# 解决方案 ：使用TestLoader()类去解决 ，它可以将用例批量添加到测试套件中(作用) ，具体使用方法discover完成

"""
 方法：discover(test_dir, pattern='test*.py')
 
 test_dir : 指定要匹配的目录 
 patten : 指定匹配的模式，比如搜索test_dir目录下所有的以test开头，同时以py结尾的文件   
"""




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

    def test_login_success1(self):
        print("开始运行用例", sys._getframe().f_code.co_name)
        except_value = 0
        actual_value = login('dev','123456').get('code')
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

    # suite = unittest.TestSuite()
    # suite.addTest(TestLogin('test_login_success'))
    # suite.addTest(TestLogin('test_user_password_null'))

    suite = unittest.TestLoader().discover('.',pattern='test_login3*.py')
    print(suite)

    runner = unittest.TextTestRunner()
    runner.run(suite)