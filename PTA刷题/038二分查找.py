# 7-38 二分查找
# 作者 usx程序设计类课程组
# 单位 绍兴文理学院
# 对于输入的n个整数，先进行升序排序，然后进行二分查找。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试数据的第一行是一个整数n（1≤n≤100），第二行有n个各不相同的整数待排序，第三行是查询次数m（1≤m≤100），第四行有m个整数待查找。
#
# 输出格式:
# 对于每组测试，分2行输出，第一行是升序排序后的结果，每两个数据之间留一个空格；第二行是查找的结果，若找到则输出排序后元素的位置（从1开始），否则输出0，同样要求每两个数据之间留一个空格。
#
# 输入样例:
# 9
# 4 7 2 1 8 5 9 3 6
# 5
# 10 9 8 7 -1
# 输出样例:
# 1 2 3 4 5 6 7 8 9
# 0 9 8 7 0
def bin_search(lst, num):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if lst[mid] == num:
            return mid + 1
        if lst[mid] > num:
            high = mid - 1
        if lst[mid] < num:
            low = mid + 1
    return 0


def print_list(lst):
    for i in range(len(lst)):
        if i != len(lst) - 1:
            print(lst[i], end=' ')
        else:
            print(lst[i])


try:
    while True:
        n = int(input())
        lst = list(map(int, input().split()))
        lst.sort()
        m = int(input())
        search_lst = list(map(int, input().split()))
        index_lst = []
        for item in search_lst:
            index_lst.append(bin_search(lst, item))
        print_list(lst)
        print_list(index_lst)
except EOFError:
    pass