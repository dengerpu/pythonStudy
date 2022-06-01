# 变换的内容如下：
# （1）将长度为10的数组中的元素按升序进行排序；
# （2）将数组的前n个元素换到数组的最后面。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每行测试数据输入1个正整数n（0 < n < 10），然后输入10个整数。
#
# 输出格式:
# 对于每组测试数据，输出变换后的全部数组元素。元素之间以一个空格分隔（最后一个数据之后没有空格）。
#
# 输入样例:
# 1
# 2 34 37 98 23 24 45 76 89 34 68
# 输出样例:
# 34 34 37 45 68 76 89 98 23 24
def print_list(lst):
    for i in range(len(lst)):
        if i != len(lst) - 1:
            print(lst[i], end=' ')
        else:
            print(lst[i])

# 推荐第一种方法
# t = int(input())
# for i in range(t):
#     n, *lst = map(int, input().split())
#     lst.sort()
#     lstA = lst[0:n]
#     lstB = lst[n:]
#     lst = lstB + lstA
#     print_list(lst)

#  方法二，前n个数逆序，后面的数逆序，整体逆序
#  由于切片逆序是返回一个新的列表，所以不用切片
#  下面的写法，完全没有python的灵魂
def reverse_list(lst, index, legth):
    start = index
    end = index + legth - 1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1


t = int(input())
for i in range(t):
    n, *lst = map(int, input().split())
    lst.sort()
    reverse_list(lst, 0, n)
    reverse_list(lst, n, len(lst) - n)
    reverse_list(lst, 0, len(lst))
    print_list(lst)
