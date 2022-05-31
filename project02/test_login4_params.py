import sys

from project02.iter03_add_user import login
import unittest
from parameterized import parameterized

# 问题 ：测试数据太多时，通过编写多条测试用例与之对应显得代码冗余，维护性不高

# 解决方案 ：使用parameterized 包实现数据参数化 ，将列表中的数据在一条测试用例中循环运行，起到多条数据测试的作用,
    # 使用的具体方法是expand


# 前置条件 ：下载 安装 ： pip install parameterized

"""
 方法：expand(list) ，list : 存放数据的列表 
 备注 ： 使用时需要放在测试方法的开头，并且前面加@，这叫装饰器(下去了解)  。
 
"""

# 思考题 ：如何把所有的登录测试数据都整合到这一个方法中？

lst_data = [(0,'admin','123456'),(0,'dev','123456')]


class TestLogin(unittest.TestCase):


    # # 初始化方法
    # def setUp(self) -> None:
    #     print("开始运行用例",sys._getframe().f_code.co_name)


    # case1 : 输入正确的用户名和正确的密码进行登录
    @parameterized.expand(lst_data)
    def test_login_success(self,except_value,user_name,password):
        print("开始运行用例", sys._getframe().f_code.co_name)
        actual_value = login(user_name,password).get('code')
        print(user_name,password)
        self.assertEqual(except_value,actual_value)



    # # case2 : 输入错误的用户名或密码进行登录
    # def test_user_password_wrong(self):
    #     print("开始运行用例", sys._getframe().f_code.co_name)
    #     except_value = 1
    #     actual_value = login('admin','1234567').get('code')
    #     self.assertEqual(except_value,actual_value)
    #
    #
    # # case3 : 输入空的用户名或密码
    # def test_user_password_null(self):
    #     print("开始运行用例", sys._getframe().f_code.co_name)
    #     except_value = 1
    #     actual_value = login('admin','').get('code')
    #     self.assertEqual(except_value,actual_value)
    #
    #
    # # def tearDown(self) -> None:
    # #     print("开始运行用例", sys._getframe().f_code.co_name)





# 2. 进行测试 -使用断言：assert
# assert 1 == 1
# assert 1 == 2
# assert 3 == 4
# print("abc")


if __name__ == '__main__':
    unittest.main()         # 代表运行所有用例


