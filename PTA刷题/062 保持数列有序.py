# 有n个整数，已经按照从小到大顺序排列好，现在另外给一个整数x，请将该数插入到序列中，并使新的序列仍然有序。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试先输入两个整数n（1≤n≤100）和x，再输入n个从小到大有序的整数。
#
# 输出格式:
# 对于每组测试，输出插入新元素x后的数列（元素之间留一个空格）。
#
# 输入样例:
# 3 3 1 2 4
# 输出样例:
# 1 2 3 4

def print_list(lst):
    for i in range(len(lst)):
        if i != len(lst) - 1:
            print(lst[i], end=' ')
        else:
            print(lst[i])


# 两种思路，1.直接插末尾，再排序 2.插到应该有的位置
# try:
#     while True:
#         n, x, *lst = map(int, input().split())
#         lst.append(x)
#         lst.sort()
#         print_list(lst)
# except EOFError:
#     pass
try:
    while True:
        n, x, *lst = map(int, input().split())
        lst.append(x)  # 为什么要这样，因为不这样会超出索引返回，不可以直接lst[n](会提示超出索引范围)
        start = n  # 因为可能存在这个要插入的数是最大值
        for i in range(n):
            if x < lst[i]:
                start = i
                break
        for j in range(n, start, -1):
            lst[j] = lst[j-1]
        lst[start] = x
        print_list(lst)
except EOFError:
    pass
