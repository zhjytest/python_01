import sys

from project02.iter03_add_user import login
import unittest
from parameterized import parameterized
from project02.HTMLTestRunner import HTMLTestRunner

# 问题 ：以前的测试报告太简单，不太美观 ，能否有更好一点的测试报告呢

# 解决方案 ：使用HTMLTestRunner模块生成测试报告 ，将报告输出到HTML文件，查看更加方便, 具体使用的是HTMLTestRunner()类


# 前置条件 ：直接使用现成的 。

"""
 类：HTMLTestRunner(f,title,description) 
        f :是指文件对象 ，一般是HTML文件
        title : 生成的测试报告标题
        description：生成测试报告的描述
 备注 ： 使用时需要放在测试方法的开头，并且前面加@，这叫装饰器(下去了解)  。
 
"""



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




if __name__ == '__main__':

    suite = unittest.TestLoader().discover('.',pattern='test_login5*.py')
    test_report = './test_report.html'

    with open(test_report,'wb') as f:
        runner = HTMLTestRunner(f,title='测试报告',description='测试报告试用版')
        runner.run(suite)



