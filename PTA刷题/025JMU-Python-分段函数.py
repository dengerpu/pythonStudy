# 本题目要求根据以下分段函数的定义，计算输入的浮点数x对应的y值，输出结果保留两位小数。注意：使用math库
#
# f(x) = 根号x + e的x次方  （x>=3）
# f(x) = sin(x) + log2(1+x)  (0<x<=3)
# f(x) = -1 (x<=0)
#
# 输入格式:
# 在一行中输入x的值。
#
# 输出格式:
# 计算结果保留两位小数输出。
#
# 输入样例1:
# 0
# 输出样例1:
# -1.00
# 输入样例2:
# 10
# 输出样例2:
# 22029.63
import math

x = eval(input())
if x >= 3:
    result = math.sqrt(x) + math.exp(x)
elif x > 0:
    result = math.sin(x) + math.log2((1+x))
else:
    result = -1
print(f'{result:.2f}')