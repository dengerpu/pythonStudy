print('用户手机账户原有话费余额为：\33[0;35m8元\33[m')
try:
    money = int(input('请输入要充值的金额：'))
    money += 8
    print('当前账户余额为\033[0;35m',money,'元\033[m')
except Exception as e:
    print(e)

