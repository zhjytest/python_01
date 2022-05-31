
"""
需求-迭代3：用户新增功能:
1. 将默认用户数据放在文件中保存，以上迭代功能查询数据都要从文件查询 。
2. 需要对文件的读写进行异常捕获
3. 用户可以输入关键字add进行新增用户 ，新增的用户信息可以保存到文件中 。
4. 同时进行查询时，也能查询出该用户 。
"""
import os

# 定义用户默认的数据

# 从文件读取数据，返回的是列表形式数据
def from_file_get_data(file_name):
    f = None
    try:
        f = open(file_name,'r')
        line = f.readline()
        user_data = eval(line)
        return user_data
    except Exception as e:
        print(e)
    finally:
        if not f:
            f.close()


# 向文件写入内容
def save_data(file_name,file_content):
    f = None
    try:
        f = open(file_name, 'w')
        f.write(str(file_content))
    except Exception as e:
        print(e)
    finally:
        if not f:
            f.close()


# 返回文件的绝对路径
def get_path(file_name):
    return os.path.abspath(file_name)


user_list = []

user_list =  user_list if user_list else from_file_get_data('user_data.txt')
# 定义默认返回结果
result = {'code':10,'message':''}


# 定义登录功能
def login(username,password):

    # 如果用户名为空或密码为空，给出用户名或密码不能为空
    if username is None:
        result.update({'code': 1, 'message': '用户名不能为空'})
        return result
    if password is None:
        result.update({'code': 1, 'message': '密码不能为空'})
        return result

    # 如果用户名和密码匹配，返回登录成功且还有列表
    for user_info in user_list:
        if username == user_info.get('account') and password == user_info.get('password'):
            result.update({'code':0,'message':'登录成功','user_list':user_list})
            return result

    #如果不匹配，返回用户名或密码不正确 ，code返回1。
    result.update({'code': 1, 'message': '登录失败，请检查您的用户名或密码是否填写正确。'})
    return result



class User():


    # 添加用户
    def add_user(self,user,password='123456',**kwargs):
        user_dict  = {}
        user_dict['account'] = user
        user_dict['password'] = password
        user_dict.update(**kwargs)
        user_list.append(user_dict)
        save_data('user_data.txt',user_list)
        result.update({"message":"用户保存成功"})
        return result


    # 查询用户
    def get_user(self,username):
        # 判断用户是否登录 ，若登录可进行查询 ，若未登录，则返回权限不足 。
        if result.get('code'):
            result.update({'code': 11, 'message': '用户未登录，无法查询用户数据'})
            return result

        # 用户登录的情况
        result.update({"user_list": []})
        lst = []  # 存放用户信息的列表
        for x in user_list:
            print("进入到这一步了吗！！")
            account = x.get('account')
            if username in account:  # 支持模糊查询
                x.pop('password')  # 把该键值对删除
                lst.append(x)

        # 若查询出数据，返回成功的消息
        if lst:
            result.update({"message": "查询用户成功!", "user_list": lst})
            return result

        # 若未查到数据，返回未成功的消息
        result.update({"code": 12, "message": "未查询到用户"})
        return result



if __name__ == '__main__':

    flag = True

    while flag:
        vls = input('操作请输入编号:'
                    '\n 1:) 进行登录 '
                    '\n 2:) 进行查询用户，请输入用户名 '
                    '\n 3:) 进行用户新增，请输入用户信息 '
                    '\n q:) 退出操作 '
                    '\n 其它字符:) 未知操作，请重新输入' )

        if not vls in ('1','2','3','q','quit'):
            print("="*30)
            continue
        if vls == '1':
            username = input("请输入用户名:")
            password = input("请输入密码")
            login_result = login(username,password)
            print(login_result)
            print("=" * 30)
            continue
        if vls == '2':
            name = input('请输入查询用户名:')
            user = User()
            get_result = user.get_user(name)
            print(get_result)
            print("=" * 30)

        if vls == '3':
            name = input('请输入添加的用户名:')
            user = User()
            get_result = user.get_user(name)
            if 12 == get_result.get('code'):
                password = input('请输入用户密码:')
                role = input('请输入角色名称:')
                dept = input("请输入部门名称:")
                user.add_user(name,password,role=role,dept=dept)
            if 0 == get_result.get('code'):
                result.update({"code":13,"message":"用户已存在，无法添加"})
                print(result)
            print(get_result)
            print("=" * 30)
        if vls in ('q','quit'):
            flag = False
            print("退出成功！")

