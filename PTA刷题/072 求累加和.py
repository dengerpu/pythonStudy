# 输入两个整数n和a，求累加和S=a+aa+aaa+…+aa…a（n个a）之值。
# 例如，当n=5，a=2时，S=2+22+222+2222+22222=24690。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试输入两个整数n和a（1≤n，a<10）。
#
# 输出格式:
# 对于每组测试，输出a+aa+aaa+…+aa…a（n个a）之值。
#
# 输入样例:
# 5 3
# 8 6
# 输出样例:
# 37035
# 74074068
import math

try:
    while True:
        n, a = map(int,input().split())
        result = 0
        k = 0
        for i in range(n):
            k += a*int(math.pow(10, i))
            result += k
        print(result)
except EOFError:
    pass