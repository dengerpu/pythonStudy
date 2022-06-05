# 求下面数列的所有大于等于精度e的数据项之和，显示输出计算的结果（四舍五入保留6位小数）。
# 1/2，3/4，5/8，7/16，9/32……
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试输入一个实数e。
#
# 输出格式:
# 对于每组测试，输出数列中所有大于等于e的数据项之和。结果四舍五入保留6位小数。
#
# 输入样例:
# 0.000001
# 输出样例:
# 2.999998
import math

try:
    while True:
        e = eval(input())
        i = 1
        sum = 0
        while True:
            a = 2*i -1
            b = math.pow(2, i)
            result = a / b
            if result < e:
                break
            else:
                sum += result
                i += 1
        print('%.6f' % sum)
except EOFError:
    pass
