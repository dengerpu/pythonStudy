def compute(a, b, option):
    if option == '+':
        return a+b
    elif option == '-':
        return a-b
    elif option == '*':
        return a*b
    elif option == '/':
        if b==0:
            raise Exception('除数不能为0')
        return a/b
    else:
        return '非法操作'


def my_calc(a, b , fun):
    result = fun(a, b)
    print(result)


try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    c = input('请输入运算符:')
    print(compute(a, b, c))
except Exception as e:
    print(e)

print('-'*30)
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    my_calc(a, b, lambda a, b: a + b)
    my_calc(a, b, lambda a, b: a - b)
    my_calc(a, b, lambda a, b: a * b)
    my_calc(a, b, lambda a, b: a / b)
except Exception as e:
    print(e)
