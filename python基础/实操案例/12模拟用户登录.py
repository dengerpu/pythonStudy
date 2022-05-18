i = 3
while i:
    user = input('请输入账号：')
    pwd = input('请输入密码：')
    i -= 1
    if user == 'admin' and pwd == 'admin':
        print('登录成功')
        break
    else:
        if i != 0:
            print(f'账号或者密码错误，您还有{i}次机会')
        else:
            print('账号已被锁定')