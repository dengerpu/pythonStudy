# 本题要求计算下列分段函数f(x)的值（x为从键盘输入的一个任意实数）：
#
# f(x)= 根号下 （2-2x）  |x|<1
# f(x)= (cosx + x的平方)/ （2.5+ |x+ ln100|） x >= 1
# f(x) = e的x次方  x<=-1
#
# 输入格式:
# 直接输入一个实数x
#
# 输出格式:
# 在一行中按“f(x)=result”的格式输出，其中x与result都保留三位小数。
#
# 输入样例:
# 3.14
# 输出样例:
# f(3.140)=0.865
import math

x = float(input())
if -1 < x < 1:
    result = math.sqrt(2-2*x)
elif x >= 1:
    result = (math.cos(x) + math.pow(x, 2))/(2.5 + abs(x + math.log(100, math.e)))
else:
    result = math.exp(x)

print(f'f({x:.3f})={result:.3f}')