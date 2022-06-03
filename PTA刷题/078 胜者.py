# Sg和Gs进行乒乓球比赛，进行若干局之后，想确定最后是谁胜（赢的局数多者胜）。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试先输入一个整数n，接下来的n行中每行输入两个整数a，b（0≤a，b≤20），表示Sg与Gs的比分是a比b。
#
# 输出格式:
# 对于每组测试数据，若还不能确定胜负则输出“CONTINUE”，否则在一行上输出胜者“Sg”或“Gs”。引号不必输出。
#
# 输入样例:
# 3
# 3 11
# 13 11
# 11 9
# 输出样例:
# Sg
try:
    while True:
        n = int(input())
        count = 0
        for i in range(n):
            a, b = map(int, input().split())
            if a > b:
                count += 1
            if a < b:
                count -= 1
        if count > 0:
            print('Sg')
        elif count < 0:
            print('Gs')
        else:
            print('CONTINUE')
except EOFError:
    pass