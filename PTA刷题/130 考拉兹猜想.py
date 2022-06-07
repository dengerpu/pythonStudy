# 考拉兹猜想（Collatz conjecture）又称奇偶归一猜想，是指对于每一个正整数，如果它是奇数，则对它乘3再加1,如果它是偶数，则对它除以2。
# 如此循环，最终都能得到1。编写一个程序，输入一个正整数，打印其考拉兹序列。
#
# 输入格式:
# 1个>1的正整数
#
# 输出格式:
# 以逗号分隔的考拉兹序列。
#
# 输入样例:
# 5
# 输出样例:
# 16,8,4,2,1
# n = int(input())
# lst = []
# while n != 1:
#     if n % 2 == 1:
#         n = 3*n+1
#     else:
#         n = int(n / 2)
#     lst.append(n)
# lst = [str(x) for x in lst]
# print(','.join(lst))
n = int(input())
while n != 1:
    if n % 2 == 1:
        n = 3*n+1
    else:
        n = int(n / 2)
    print("%d" % n, end="," if n != 1 else "")