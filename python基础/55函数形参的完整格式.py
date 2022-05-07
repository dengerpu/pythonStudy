# 普通形参 缺省形参 不定长元组形参 不定长字典形参
def func(a, b=1):  # 先普通在缺省
    print(a, b)


# def func1(a, b=1, *args):  #语法上不会报错，但是缺省参数不能使用默认值
#     print(f'a:{a}')
#     print(f'b:{b}')
#     print(args)

def func2(a, *args, b=1):  #普通形参，不定长元组形参 缺省形参
    print(f'a:{a}')
    print(f'b:{b}')
    print(args)

# func1(1, 2, 3, 4)
func2(1, 2, 3, 4)   # a = 1 ,b=1 (2, 3, 4)
func2(1, 2, 3, 4, b=5)  # a:1 b:5 (2, 3, 4)


def fun3(a, *args, b=1, **kwargs):
    print(f'a:{a}')
    print(f'b:{b}')
    print(args)
    print(kwargs)


fun3(1, 2, 3, b=4, c=1, d=5)  # a:1 b:4 (2, 3) {'c': 1, 'd': 5}
fun3(1, 2, 3,  c=1, d=5)




