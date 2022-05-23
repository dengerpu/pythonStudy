# 本题目要求计算以下分段函数的值（x为从键盘输入的一个任意实数）：
# y = -2*x-1 (x<=-2)
#   y = 3  (-2<x<=1)
#   y = 2*x+1 (x>1)
# 如果输入非数字，则输出“Input Error!”
# 输入格式:
# 在一行中输入一个实数x。
# 输出格式:
# 在一行中按”y=result”的格式输出，其中result保留两位小数。
# 输入样例:
# -2
# 输出样例:
# 在这里给出相应的输出。例如：
#
# y=3.00
try:
    x = float(input())
    if x <= -2:
        result = -2*x-1
    elif x <= 1:
        result = 3
    else:
        result = 2*x+1
    print(f'y={result:.2f}')
except:
    print('Input Error!')
