def fun(n):
    '''
    非递归求阶乘
    :param n:
    :return:
    '''
    num = 1
    for i in range(1, n+1):
        num = num*i
    print(num)


def fun1(n):
    if n == 1:
        return 1
    else:
        return n*fun1(n-1)


fun(5)
print(fun1(5))
print(fun1(1))