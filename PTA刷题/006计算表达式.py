# 输入一个形式如"操作数 运算符 操作数"的表达式，对2个整数进行乘、整除和求余(%)运算。
#
# 输入格式:
# 在一行中输入形式如"操作数 运算符 操作数"的表达式。
#
# 输出格式:
# 在一行中输出表达式及计算结果。
#
# 输入样例1:
# 在这里给出一组输入。例如：
#
# 21  *  8
# 输出样例1:
# 在这里给出相应的输出。例如：
#
# 21*8=168
# 输入样例2:
# 在这里给出一组输入。例如：
#
# 21  !  8
# 输出样例1:
# 在这里给出相应的输出。例如：
#
# Invalid operator

# 提交显示答案错误
try:
    value = input()
    list = value.split()
    if list[1] == '*':
        result = int(list[0]) * int(list[2])
        print(f'{list[0]}{list[1]}{list[2]}={result}')
    elif list[1] == '//':
        result = int(list[0]) // int(list[2])
        print(f'{list[0]}{list[1]}{list[2]}={result}')
    elif list[1] == '%':
        result = int(list[0]) % int(list[2])
        print(f'{list[0]}{list[1]}{list[2]}={result}')
    else:
        print('Invalid operator')
except:
    print('Invalid operator')
