# 输入一个整数n，输出2n-1行构成的菱形，例如，n=5时的菱形如输出样例所示。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试输入一个整数n（3≤n≤20）。
#
# 输出格式:
# 对于每组测试数据，输出一个共2n-1行的菱形，具体参看输出样例。
#
# 输入样例:
# 5
# 输出样例:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
try:
    while True:
        n = int(input())
        for i in range(1, n+1):
            for j in range(n-i):
                print(' ', end='')
            for k in range(2*i-1):
                print('*', end='')
            print()
        for i in range(1,n):
            for j in range(i):
                print(' ', end='')
            for k in range(2*(n-i)-1):
                print('*', end='')
            print()
except EOFError:
    pass