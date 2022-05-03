# python 元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号

my_tuple = tuple()  # 定义一个空元组
print(my_tuple, type(my_tuple ))  # () <class 'tuple'>
my_tuple1 = ()
print(my_tuple1, type(my_tuple1))  # () <class 'tuple'>

my_list = ['123',12,3.14]  # 列表是【】
my_tuple = ('123',12,3.14)  # 元组是 （）
print(my_tuple, type(my_tuple))  # ('123', 12, 3.14) <class 'tuple'>
print(my_tuple[1])

# 定义一个数据元素的元组，数据元素后面必须有一个逗号
my_tuple = (3)
print(my_tuple, type(my_tuple))  # 3 <class 'int'>

my_tuple = (3,)
print(my_tuple, type(my_tuple))  # (3,) <class 'tuple'>
