import sys

from project02.iter03_add_user import login
import unittest

# 1.使用TestCase编写测试用例

# 作用1 ： 可以测试用例断言(测试)
# 作用2 ： 进行初始化或清除操作 。

class TestLogin(unittest.TestCase):


    # 初始化方法
    def setUp(self) -> None:
        print("开始运行用例",sys._getframe().f_code.co_name)

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
        except_value = 2
        actual_value = login('admin','').get('code')
        self.assertEqual(except_value,actual_value)


    def tearDown(self) -> None:
        print("开始运行用例", sys._getframe().f_code.co_name)





# 2. 进行测试 -使用断言：assert
# assert 1 == 1
# assert 1 == 2
# assert 3 == 4
# print("abc")


if __name__ == '__main__':
    unittest.main()