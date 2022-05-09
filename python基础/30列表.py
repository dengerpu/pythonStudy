# 列表是 python中的一种数据类型，可以存放多个数据，列表中的数据可以是任意类型的
# 列表list 使用[]定义

# 定义空列表
my_list = []
print(type(my_list), my_list)  # <class 'list'> []
my_list1 = list()  # 空列表
print(type(my_list1), my_list1)  # <class 'list'> []

# 定义带数据的列表，数据元素之间使用逗号隔开
my_list2 = [1,3.14,True,'itcast']
print(my_list2)  # [1, 3.14, True, 'itcast']

# 求列表中数据元素的个数，即列表的长度
print(len(my_list2))

# 列表支持下标和切片
print(my_list2[0])  # 1
print(my_list2[-1])  # itcast

print(my_list2[1:3])  # [3.14, True]
print(my_list2[::-1])  # ['itcast', True, 3.14, 1]
print(my_list2[:])  # [1, 3.14, True, 'itcast']

# 下标操作和字符串中不同的是，字符串不能使用下标修改其中的数据，但是列表可以
my_list2[0] = 'modify'
print(my_list2)

my_list = [20, 30]
def fun(a):
    a += 20, # (20,)相当于一个元组   列表，+=，extend即a.extend（20，）

fun(my_list)
print(my_list)