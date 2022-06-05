# 求两个正整数m，n的最大公约数（Greatest Common Divisor，简称GCD）。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组测试输入2个整数m,n (0<m,n<10^9)。
#
# 输出格式:
# 对于每组测试，输出m，n的最大公约数。
#
# 输入样例:
# 2
# 63 36
# 20 15
# 输出样例:
# 9
# 5
# def get_GCD(a, b):  # 法一： 枚举法，运行会超时
#     a, b = max(a, b), min(a, b)
#     for i in range(b, 0, -1):
#         if a % i == 0 and b % i == 0:
#             return i

def get_GCD(a, b):  # 法二： 辗转相除法法，又成欧几里得算法
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    return b


t = int(input())
for i in range(t):
    m, n = map(int, input().split())
    gcd = get_GCD(m, n)
    print(gcd)