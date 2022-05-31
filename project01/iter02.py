
"""
## 需求-迭代2：用户查询功能:
1. 用户查询功能必须是在登录以后才能调用 ，否则给出权限不足提示
2. 若输入的用户名正确，返回登录用户的信息，password字段不显示   。
3. 若输入的用户名不正确 ，给出无查询结果的提示
4. 查询支持模糊查询。
"""

# 定义用户默认的数据
user_list = [{'role':'admin','account':'admin','password':'123456','dept':'tester'},{'role':'user','account':'dev','password':'123456','dept':'dev'}]
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


# 用户查询功能
def get_user(username):
    # 判断用户是否登录 ，若登录可进行查询 ，若未登录，则返回权限不足 。
    if result.get('code'):
        result.update({'code':11,'message':'用户未登录，无法查询用户数据'})
        return result

    # 用户登录的情况
    result.update({"user_list":[]})
    lst = []    # 存放用户信息的列表
    for x in user_list:
        print("进入到这一步了吗！！")
        account = x.get('account')
        if username in account:     # 支持模糊查询
            x.pop('password')       # 把该键值对删除
            lst.append(x)

    # 若查询出数据，返回成功的消息
    if lst:
        result.update({"message":"查询用户成功!","user_list":lst})
        return result

    # 若未查到数据，返回未成功的消息
    result.update({"code":12,"message":"未查询到用户"})
    return result





if __name__ == '__main__':

    flag = True

    while flag:
        vls = input('操作请输入编号:'
                    '\n 1:) 进行登录 '
                    '\n 2:) 进行查询用户，请输入用户名 '
                    '\n q:) 退出操作 '
                    '\n 其它字符:) 未知操作，请重新输入' )

        if not vls in ('1','2','q','quit'):
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
            get_result = get_user(name)
            print(get_result)
            print("=" * 30)

        if vls in ('q','quit'):
            flag = False
            print("退出成功！")

