# 输入整数n，1<=n<=10,输出n行n列图案。
#
# 输入格式:
# 输入一个整数
#
# 输出格式:
# 输出图案，图案中的每个数所占宽度为4
#
# 输入样例:
# 5
# 输出样例:
#    1   1   1   1   1
#    1   2   2   2   2
#    1   2   3   3   3
#    1   2   3   4   4
#    1   2   3   4   5
n = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        if j <= i:
            print('%4s' % j, end='')
        else:
            print('%4s' % i, end='')
    print()
