password = input('支付宝支付密码：')
if password.isdigit():
    print('支付密码合法')
else:
    print('支付数字不合法')

print('-'*30)
print('支付数据合法' if password.isdigit() else '支付数据只能是数字')