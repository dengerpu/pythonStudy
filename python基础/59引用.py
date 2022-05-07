# 可以使用id()查看变量的引用，可以将id值认为是内存地址的别名
# python中数据值的传递的是引用
# 赋值运算符可以改变变量的引用

# 将数据10，存储到变量a中。本质是将数据10所在内存的引用地址保存到变量a中
a = 10
# 将变量a保存的引用地址给b
b = a
print(a, b)
print(id(a) == id(b))  # True
print(id(a))  # 140704208966976
print(id(b))  # 140704208966976
a = 20
print(a, b)
print(id(a), id(b))
print('='*30)
my_list = [1, 2, 3]  # 将列表的引用地址保存到变量my_list中
my_list1 = my_list  # 将变量my_list变量存储的引用地址给到my_list1
print(my_list, my_list1)
print(id(my_list), id(my_list1))
print(id(my_list) == id(my_list1))  # True

print('='*30)
my_list.append(4)
print(my_list, my_list1)
print(id(my_list), id(my_list1))
print(id(my_list) == id(my_list1))  # True

print('='*30)
my_list[2] = 5
print(my_list, my_list1)
print(id(my_list), id(my_list1))
print(id(my_list) == id(my_list1))  # True.

# 交互终端中，小整数的概念。小整数默认范围是-5~255 如果是小整数使用相同的引用地址