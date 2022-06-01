# 求两个集合的差集。注意，同一个集合中不能有两个相同的元素。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组测试数据输入1行，每行数据的开始是2个整数n（0 < n ≤ 100）和m（0 < m ≤ 100），分别表示集合A和集合B的元素个数，然后紧跟着n+m个元素，前面n个元素属于集合A，其余的属于集合B。每两个元素之间以一个空格分隔。
#
# 输出格式:
# 针对每组测试数据输出一行数据，表示集合A-B的结果，如果结果为空集合，则输出“NULL”（引号不必输出），否则从小到大输出结果，每两个元素之间以一个空格分隔。
#
# 输入样例:
# 2
# 3 3 1 3 2 1 4 7
# 3 7 2 5 8 2 3 4 5 6 7 8
# 输出样例:
# 2 3
# NULL
def print_list(lst):
    for i in range(len(lst)):
        if i != len(lst) - 1:
            print(lst[i], end=' ')
        else:
            print(lst[i])


t = int(input())
for i in range(t):
    n, m, *lst = list(map(int, input().split()))
    setA = set(lst[:n])
    setB = set(lst[n:n+m])
    setC = setA - setB
    if len(setC):
        sorted(setC)
        print_list(list(setC))
    else:
        print('NULL')

