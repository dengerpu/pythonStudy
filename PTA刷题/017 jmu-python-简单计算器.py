# 输入一个表达式字符串，计算其结果
#
# 输入格式:
# 行1：输入字符串数目
# 下面分别输入要计算的表达式
# 输出格式:
# 输出计算结果，结果保留2位小数。对于异常数据能输出相应异常信息。
#
# 输入样例1:
# 4
# 1+1
# 56-23
# 5/3
# 5*3.5
# 输出样例1:
# 2.00
# 33.00
# 1.67
# 17.50
# 输入样例2:
# 3
# ab+23
# 2/0
# 23+36f
# 输出样例2:
# NameError
# ZeroDivisionError
# SyntaxError

n = int(input())
result_list = []
for i in range(n):
    value = input()
    try:
        result_list.append(f'{eval(value):.2f}')
    except NameError:
        result_list.append('NameError')
    except ZeroDivisionError:
        result_list.append("ZeroDivisionError")
    except SyntaxError:
        result_list.append("SyntaxError")
for item in result_list:
    print(item)
# eval函数作用：将字符串str当成有效地表达式来求值并返回计算结果
