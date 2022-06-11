# 打印出n阶的“叉”，这个叉图案由字符‘+’和‘X’构成，n越大，这个图案也就越大
#
# 输入格式:
# 一个正整数n，1<=n<=20
#
# 输出格式:
# 一个n阶叉图案
#
# 输入样例：
#
# 1
#
# 输出样例：
#
# X
#
# 输入样例：
#
# 3
#
# 输出样例：
#
# X+++X
#
# +X+X+
#
# ++X++
#
# +X+X+
#
# X+++X
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 7
# 输出样例:
# 在这里给出相应的输出。例如：
#
# X+++++++++++X
# +X+++++++++X+
# ++X+++++++X++
# +++X+++++X+++
# ++++X+++X++++
# +++++X+X+++++
# ++++++X++++++
# +++++X+X+++++
# ++++X+++X++++
# +++X+++++X+++
# ++X+++++++X++
# +X+++++++++X+
# X+++++++++++X
n = int(input())
for i in range(n-1):
    for j in range(i):
        print('+', end='')
    print('X', end='')
    for k in range(2*(n-i-1)-1):
        print('+', end='')
    print('X', end='')
    for z in range(i):
        print('+', end='')
    print()
for i in range(n):
    for j in range(n-i-1):
        print('+', end='')
    print('X', end='')
    if i != 0:
        for k in range(2 * i - 1):
            print('+', end='')
        print('X', end='')
    for z in range(n - i - 1):
        print('+', end='')
    print()
