def print_line():
    '''
    打印横线
    :return:
    '''
    print('-'*30)


def print_lines(n):
    for i in range(n):
        print_line()


print_lines(5)


def my_sum(a, b, c):
    return a+b+c


def average(a, b, c):
    res = my_sum(a, b, c)
    return res / 3


result = average(1,2,3)
print(result)


