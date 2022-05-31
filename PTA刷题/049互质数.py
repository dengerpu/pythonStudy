# Sg认识到互质数很有用。若两个正整数的最大公约数为1，则它们是互质数。要求编写函数判断两个整数是否互质数。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组测试先输入1个整数n（1≤n≤100），再输入n行，每行有一对整数a、b（0<a，b<10^9）。
#
# 输出格式:
# 对于每组测试数据，输出有多少对互质数。
#
# 输入样例:
# 1
# 3
# 3 11
# 5 11
# 10 12
# 输出样例:
# 2
# def max_zhishu(a, b):  #  不推荐，耗费时间
#     a, b = min(a, b), max(a, b)
#     for i in range(a, 0, -1):  # a~1
#        if b % i == 0 and a % i == 0:
#            return i
def zhishu(a, b):
    if b == 0:
        return a
    else:
        return zhishu(b, a % b)


t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    for j in range(n):
        a, b = map(int,input().split())
        if zhishu(a,b) == 1:
            count += 1
    print(count)
