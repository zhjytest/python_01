print("====")

"""
需求-迭代1：登录功能
1. 定义两条用户数据 ，要求用户数据的属性包括用户角色，用户账号，密码，部门
2.要求返回的格式是字典形式 ，包含两个字段，code和message ,code为0代表成功，为1代表失败 ；message给出相应的提示 ，格式如 ：{'code':0,'message':''}
3.用户通过控制台输入用户名和密码，判断用户名和密码是否和定义数据中的用户名密码向匹配，若匹配返回成功登录消息体，并把用户列表也追加到返回结果中
4.若用户名输入为空或密码输入为空，都给出对应的提示，如用户名不能为空
5.若用户名或密码不匹配，都给出登录失败，请检查您的用户名或密码是否填写正确。提示
"""


"""
需求-迭代2：用户查询功能:
1.用户查询功能必须是在登录以后才能调用 ，否则给出权限不足提示
2.若输入的用户名正确，返回登录用户的信息，password的密码使用*代替  。
3.若输入的用户名不正确 ，给出无查询结果的提示
4.查询支持模糊查询。
"""

"""
需求-迭代3：用户新增功能:
1.将默认用户数据放在文件中保存，以上迭代功能查询数据都要从文件查询 。
2.用户可以输入关键字add进行新增用户 ，新增的用户信息可以保存到文件中 。
3.同时进行查询时，也能查询出该用户 。
"""


"""
需求-迭代4：
"""


# 定义用户默认的数据
user_list = [{'role':'admin','account':'admin','password':'123456','dept':'tester'},{'role':'user','account':'dev','password':'123456','dept':'dev'}]
# 定义默认返回结果
result = {'code':0,'message':''}


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
            result.update({'message':'登录成功','user_list':user_list})
            return result

    #如果不匹配，返回用户名或密码不正确 ，code返回1。
    result.update({'code': 1, 'message': '登录失败，请检查您的用户名或密码是否填写正确。'})
    return result



# 定义查询功能
def get_user(username):
    pass


# 用户新增功能

if __name__ == '__main__':

    username = input("请输入用户名:")
    password = input("请输入密码")

    login_result = login(username,password)
    print(login_result)


