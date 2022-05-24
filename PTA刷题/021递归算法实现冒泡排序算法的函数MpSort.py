# 定义一个函数MpSort实现对一组数据的从小大排序。编写程序，实现读入若干个整数存入合适的数据结构类型的对象中。再调用MpSort函数，对该对象中的元素进行排序后输出。
#
# 输入格式:
# 一组用空格隔开的整数。
#
# 输出格式:
# 排序好一组用空格隔开的的整数。例如：尾部带空格。
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 1 3 5 7 4 2 6 8 10 9
# 输出样例:
# 在这里给出相应的输出。例如：
#
# 1 2 3 4 5 6 7 8 9 10
def MpSort(lst):
    flag = 0  # 一轮循环如果flag值没有发生变化，则说明列表已经是有序
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            flag = 1
    if flag == 1:
        MpSort(lst)


num_list = list(map(int, input().split()))
MpSort(num_list)
for i in num_list:
    print(i,end=' ')

