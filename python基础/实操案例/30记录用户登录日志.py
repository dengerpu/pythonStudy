import time


def show_info():
    print('输入提示数字，执行响应操作：0退出 1.查看登录日志')


# 记录日志
def write_logininfo(username):
    with open('log.txt', 'a', encoding='utf-8') as file:   # 好处是不用手动关闭
        s = f'用户名{username}，登陆时间：{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))}\n'
        file.write(s)


# 读取日志
def read_info():
    with open('log.txt', 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            else:
                print(line,end='')


username = input('请输入用户名：')
pwd = input('请输入密码：')
if username == 'admin' and pwd == 'admin':
    print('登陆成功！')
    write_logininfo(username)
    while True:
        show_info()
        num = input('请输入操作数字：')
        if num == '0':
            break
        elif num == '1':
            print('---------------登录日志-------------')
            read_info()
        else:
            print('输入有误，请重新输入：')
else:
    print('账号或密码错误')
