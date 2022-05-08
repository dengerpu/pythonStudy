def my_calc(a, b, fun):
    '''
    :param a: 第一个参数
    :param b: 第二个参数
    :param fun: 函数要进行的操作
    :return: 运算结果
    '''
    print('其他代码执行....')
    num = fun(a, b)
    print(num)


def add(a, b):
    return a+b


my_calc(10, 20, add)
my_calc(10, 20, lambda a, b: a+b)
my_calc(10, 20, lambda a, b: a-b)
my_calc(10, 20, lambda a, b: a*b)
my_calc(10, 20, lambda a, b: a/b)