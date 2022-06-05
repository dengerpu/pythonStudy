# 输入一个正整数m，判断该数是否为素数。
#
# 输入格式:
# 首先输入测试组数T，然后输入T组测试数据。每组测试输入一个正整数m。
#
# 输出格式:
# 对于每组测试，若m为素数则输出“yes”；反之输出“no”。注意：引号不必输出。
#
# 输入样例:
# 3
# 9
# 3
# 7
# 输出样例:
# no
# yes
# yes
import math


def is_sushu(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    else:
        return True

t = int(input())
for i in range(t):
    n = int(input())
    if is_sushu(n):
        print('yes')
    else:
        print('no')