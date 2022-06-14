# 当n=5时，沙漏图形如输出样例所示。请观察并明确沙漏图形的规律。要求输入一个整数n，输出满足规律的沙漏图形。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试输入一个整数n（1<n<20）。
#
# 输出格式:
# 对于每组测试，输出满足规律的沙漏图形。
#
# 输入样例:
# 5
# 输出样例:
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********
try:
    while True:
        n = int(input())
        for i in range(n):
            for j in range(i):
                print(end=' ')
            for k in range(2*(n-i)-1):
                print('*', end='')
            print()
        for i in range(1, n):
            for j in range(n-i-1):
                print(end=' ')
            for j in range(2*i+1):
                print('*', end='')
            print()
except EOFError:
    pass