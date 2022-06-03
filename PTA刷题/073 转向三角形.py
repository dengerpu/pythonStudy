# 输入一个整数n，要求用数字1到n排列出一个转向三角形。例如，n=5时，转向三角形如输出样例所示。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组测试数据输入1个整数n（1≤n≤9）。
#
# 输出格式:
# 对于每组测试数据，输出一个有2n-1行的，由数字1…n…1组成的转向三角形（参看输出样例）。
#
# 输入样例:
# 1
# 5
# 输出样例:
# 1
# 22
# 333
# 4444
# 55555
# 4444
# 333
# 22
# 1
t = int(input())
for i in range(t):
    n = int(input())
    for i in range(1, n+1):
        for j in range(i):
            print(i,end='')
        print()
    for i in range(1,n):
        for j in range(n-i):
            print(n-i, end='')
        print()