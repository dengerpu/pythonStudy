"""
抛出异常：
    raise 异常对象  # 当程序遇到raise,程序就报错
异常对象 = 异常类（参数）
抛出自定义异常：
    1.自定义异常类，自定义Exception或者BaseException
    2.选择书写，定义__init__方法，定义__str__方法
    3.在合适的时机抛出异常对象即可
"""
# 自定义异常类


class PasswordLengthError(Exception):
    def __init__(self, error):
        self.error = error
    def __str__(self):
        return f'发生异常：{self.error}'
    pass


def get_password():
    pwd = input('请输入密码：')
    if len(pwd) >=6:
        print('密码长度符合')
    else:
        # 抛出异常
        raise PasswordLengthError('密码长度不足6位')


# try:
#     get_password()
# except PasswordLengthError as e:
#     print(e)

get_password()
print('其他代码...')