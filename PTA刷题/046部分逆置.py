# 输入n个整数，把第i到j之间的全部元素进行逆置（1 ≤ i < j ≤ n），输出逆置后的n个数。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。
# 每组测试数据首先输入n，i，j（含义如上描述），然后再输入n个整数。
#
# 输出格式:
# 对于每组测试数据，输出逆置后的n个整数。每两个数据之间留1个空格。
#
# 输入样例:
# 2
# 7 2 6 11 22 33 44 55 66 77
# 5 1 5 11 22 33 44 55
# 输出样例:
# 11 66 55 44 33 22 77
# 55 44 33 22 11
def print_lst(lst):
    for i in range(len(lst)):
        if i != len(lst) - 1:
            print(lst[i], end=' ')
        else:
            print(lst[i])
#
#
# def reverse(lst, i, j):
#     while i < j:
#         lst[i-1], lst[j-1] = lst[j-1], lst[i-1]
#         i += 1
#         j -= 1
#
#
# t = int(input())
# for k in range(t):
#     my_lst = list(map(int,input().split()))
#     n = my_lst[0]
#     i = my_lst[1]
#     j = my_lst[2]
#     lst = my_lst[3:]
#     reverse(lst, i, j)
#     print_lst(lst)
t = int(input())
for k in range(t):
    n, i, j, *nums = map(int, input().split())
    i -= 1
    nums[i:j] = reversed(nums[i:j])
    print_lst(nums)
