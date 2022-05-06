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

