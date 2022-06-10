# 输出斐波那契数列不大于n的序列。
#
# 输入格式:
# 请在一行输入一个正整数n
#
# 输出格式:
# 在一行输出斐波那契数列不大于n的序列，并用逗号隔开。
#
# 输入样例:
# 1000
# 输出样例:
# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
import re
def fun(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fun(n-1) + fun(n-2)


n = int(input())
lst = []
for i in range(n):
    if fun(i) > n:
        break
    else:
        lst.append(fun(i))
for i in lst:
    print(i, end=',')
