# 输入一个整数列表，找出整数列表中最大元素的下标，如果最大元素的个数超过1，那么请打印输出所有的下标。
#
# 输入格式:
# 数字1,数字2,数字3,....,数字n
#
# 输出格式:
# 下标1
# 下标2
# ...
# 下标k
#
# 输入样例:
# 3,2,3
# 输出样例:
# 0
# 2
lst = list(map(int, input().split(',')))
max_num = max(lst)
for index,value in enumerate(lst):
    if value == max_num:
        print(index)
