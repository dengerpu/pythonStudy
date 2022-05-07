# 在形参前边加一个*，该形参变为不定长元组形参，可以接收所有的位置实参，类型是元组
# 在形参前边加两个**，该形参变为不定长字典形参，可以接收所有关键字实参，类型是字典

def fun(*args, **kwargs):
    print(args)
    print(kwargs)


fun(1, 2, 3, 4)  # (1, 2, 3, 4) {}
fun(1, 2, a=1, b=2)  # (1, 2) {'a': 1, 'b': 2}
fun(a=1, b=2, c=3)  # () {'a': 1, 'b': 2, 'c': 3}
# fun(a=1, b=2, 1, 2)   #  positional argument follows keyword argument
# #位置参数必须在关键字参数前边


def add(*args, **kwargs):
    num = 0
    for i in args:
        num += i
        print(f'{i}+',end='')
    k = 0
    for j in kwargs.values():
        num += j
        k += 1
        if k < len(kwargs.values()):
            print(f'{j}+', end='')
        else:
            print(f'{j}',end='')
    print(f'={num}')
    # print(f'求和的结果为{num}')


add(1, 2, a=1, b=2)
add(1, 2, 3, 4, a=1, b=2, c=5)

my_list = [1, 2, 3, 4, 5, 6]
my_dict = {'a': 7, 'c': 8, 'b': 9, 'd': 10}
# add(my_list)  # 将列表作为一个数据进行传递
add(*my_list)  # 将列表中的每一个数据作为一个位置参数进行传参，拆包

# add(my_dict)  # 将my_dict作为一个位置实参进行传递
# add(*my_dict)   # 将my_dict的key作为一个位置实参进行传递
add(**my_dict)  # 将my_dict的键值对作为关键词实参进行传递
