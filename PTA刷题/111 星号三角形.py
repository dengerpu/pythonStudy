# 输入整数n，显示星号构成的三角形。例如，n=6时，显示输出的三角形如样例输出所示。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试输入一个正整数n（0<n<41）。
#
# 输出格式:
# 对于每组测试，输出n行构成的三角形。
#
# 输入样例:
# 6
# 输出样例:
#      *
#     ***
#    *****
#   *******
#  *********
# ***********
try:
    while True:
        n = int(input())
        for i in range(1, n+1):
            for j in range(n-i):
                print(end=' ')
            for k in range(2*i-1):
                print(end='*')
            print()
except EOFError:
    pass