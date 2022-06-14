# 编写一个美元与人民币转换的程序，用户输入金额和汇率，输出转换为另一种货币表示的金额。（美元用符号’$’表示，人民币用￥表示，￥可以在中文输入法下按shift+4获取）
#
# 输入格式:
# 第一行输入一个以货币符号结尾的正数，数值作为金额，货币符号表明货币种类
#
# 第二行输入一个浮点数作为汇率
#
# 输出格式:
# 输入符合要求时输出一个带货币符号的数值（保留2位小数）
#
# 输入不符合要求时输出Data error!
#
# 输入样例:
# 58$
# 6.75
# 输出样例:
# 391.50￥
# 输入样例:
# 100￥
# 6.85
# 输出样例:
# 14.60$
value = input()
rate = eval(input())
if value.endswith('$'):
    money = eval(value[0:len(value)-1])  # 去掉最后一个标识符，并转化为整数或者浮点数
    money = money * rate
    print(f'{money:.2f}', end='￥')
elif value.endswith('￥'):
    money = eval(value[0:len(value)-1])  # 去掉最后一个标识符，并转化为整数或者浮点数
    money = money / rate
    print(f'{money:.2f}', end='$')
else:
    print('Data error!')