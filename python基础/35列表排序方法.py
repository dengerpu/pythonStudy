# 想要对列表的数据进行排序，前提是列表得数据类型是一样的
my_list = [1, 5, 3, 8, 6, 9, 7]

# 列表.sort() 直接在列表中进行排序
# my_list.sort() 默认是从小到大，即升序
# my_list.sort(reverse=True) #reverse=True，从大到小
# my_list.sort()  # [1, 3, 5, 6, 7, 8, 9]
# my_list.sort(reverse=True)  # [9, 8, 7, 6, 5, 3, 1]
# print(my_list)

# 补充：sorted（列表）排序，不会再原列表中进行排序，会得到一个新的列表
my_list1 = sorted(my_list)
my_list2 = sorted(my_list, reverse=True)
print(my_list)
print(my_list1)
print(my_list2)

my_list3 = ['a', 'b', 'c', 'd', 'e', 'f']

my_list4 = my_list3[::-1]
print(my_list4)

# 会在原列表直接逆置 列表.reverse()
my_list3.reverse()
print(my_list3)

