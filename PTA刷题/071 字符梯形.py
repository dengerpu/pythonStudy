# 用从m到n的数字字符排列出一个字符梯形。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组测试数据输入2个整数m、n（1≤m≤n≤9）。
#
# 输出格式:
# 对于每组测试数据，输出一个有n-m+1行的，由数字m…n排列而成的梯形，每行的长度依次为：m，m+1，m+2，……，n，每行的数字依次是m，m+1，m+2，……，n。
#
# 输入样例:
# 1
# 3 6
# 输出样例:
# 333
# 4444
# 55555
# 666666
# import math
#
# t = int(input())
# for i in range(t):
#     m, n = map(int, input().split())
#     for i in range(m, n+1):
#         result = i
#         for j in range(1, i):
#             result += i*int(math.pow(10, j))
#         print(result)

t = int(input())
for i in range(t):
    m, n = map(int, input().split())
    for i in range(m, n+1):
        result = str(i)
        for j in range(1, i):
            result += str(i)
        print(result)