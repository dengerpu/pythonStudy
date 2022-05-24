# 本题目要求根据以下分段函数的定义，计算输入的浮点数x对应的y值，输出结果保留两位小数。注意：使用math库
#
# f(x) = cos(x) + e的x次方  （x>3.5）
# f(x) = tan(x) + ln(1+x)  (0<x<=3.5)
# f(x) = 0 (x<=0)
#
# 输入格式:
# 在一行中输入x的值。
#
# 输出格式:
# 计算结果保留两位小数输出。
#
# 输入样例1:
# -1
# 输出样例1:
# 0.00
# 输入样例2:
# 3.5
# 输出样例:
# 1.88
import math

x = eval(input())
if x > 3.5:
    result = math.cos(x) + math.exp(x)
elif x > 0:
    result = math.tan(x) + math.log((1+x), math.e)
else:
    result = 0
print(f'{result:.2f}')