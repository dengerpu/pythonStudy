# 显示菱形图形，每行的宽度是11。
#
# 输入格式:
# 输入显示的行数，行数在1,3,5,7,9,11中取值
#
# 输出格式:
# 菱形图形，每行的宽度是11
#
# 输入样例1:
# 在这里给出一组输入。例如：
#
# 5
# 输出样例1:
# 在这里给出相应的输出。例如：
#
#      *
#     ***
#    *****
#     ***
#      *
# 输入样例2:
# 在这里给出一组输入。例如：
#
# 11
# 输出样例2:
# 在这里给出相应的输出。例如：
#
#      *
#     ***
#    *****
#   *******
#  *********
# ***********
#  *********
#   *******
#    *****
#     ***
#      *
n = int(input())
n = int(n/2+1)
for i in range(1, n+1):
    for j in range(int((11-(2*i-1))/2)):
        print(end=' ')
    for k in range(2*i-1):
        print('*', end='')
    for z in range(int((11 - (2 * i - 1)) / 2)):
        print(end=' ')
    print()
for i in range(1, n):
    for j in range(int((11-(2*(n-i)-1))/2)):
        print(end=' ')
    for k in range(2*(n-i)-1):
        print('*', end='')
    for z in range(int((11 - (2 * (n - i) - 1)) / 2)):
        print(end=' ')
    print()