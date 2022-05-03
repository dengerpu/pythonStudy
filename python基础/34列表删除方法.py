my_list = [1, 2, 5, 7, 9, 2]
# 1.根据元素的数据值删除 remove(数据值)，直接删除原列表中的数据
my_list.remove(2)  # 只会删除第一个
print(my_list)
# my_list.remove(4)  # 程序报错，要删除的数不存在

# 2.根据下标删除
# 2.1 pop(下标)，默认删除最后一个数据，返回删除的内容
num = my_list.pop()  # 删除最后一个数据 2
print(num)
print(my_list)  # [1, 5, 7, 9]

num = my_list.pop(2)  #删除下标为2的  7
print(my_list)  # [1, 5, 9]
# 删除下标不存在的，会报错

# 2.2 del 列表[下标]
del my_list[1]  # 删除下标为1的数据 5
print(my_list)
# 删除下标不存在的，会报错
