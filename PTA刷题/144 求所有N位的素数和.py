# 输入一个正整数n(n>=2)，输出所有n位的素数和，如n=2，即输出的是10-99之间的所有素数的和。
#
# 输入格式:
# 一个正整数n(n>=2)
#
# 输出格式:
# 输出所有n位的素数和
#
# 输入样例:
# 2
# 输出样例:
# 10-99之间所有的素数和=1043
import math


def is_sushu(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


n = int(input())
sum = 0
for i in range(10**(n-1),10**n):
    if is_sushu(i):
        sum += i
print(f'{10**(n-1)}-{10**n-1}之间所有的素数和={sum}')
