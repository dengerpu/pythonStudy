# 本题目要求根据以下分段函数的定义，计算输入的x对应的y值，输出结果保留两位小数；如果输入的x是非数值型数据，输出'Input Error'。注意：使用math库
#
# f(x) = cos(x) + e的x次方（x>0）
# f(x) = 0 (x<=0)
#
# 输入格式:
# 在一行中输入x的值。
#
# 输出格式:
# 按“f(x) = result”的格式输出，其中x与result都保留两位小数，注意'='两边有空格。
#
# 如果输入的x是非数值型数据，输出：Input Error
#
# 输入样例1:
# 1.5
# 输出样例1:
# f(1.50) = 4.55
# 输入样例2:
# -4
# 输出样例2:
# f(-4.00) = 0.00
# 输入样例3:
# abc
# 输出样例3:
# Input Error
import math
try:
    x = eval(input())
    result = (math.cos(x) + math.exp(x)) if x > 0 else  0
    print(f'f({x:.2f}) = {result:.2f}')
except:
    print('Input Error')


