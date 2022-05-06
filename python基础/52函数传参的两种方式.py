def fun(a, b, c):
    print(f'a:{a}')
    print(f'b:{b}')
    print(f'c:{c}')


# 位置传参，按照形参的位置顺序将实参的值传递给形参
fun(1, 2, 3)
print('='*30)
fun(3, 2, 1)
print('='*30)
# 关键字传参，指定实参传给那个形参，注意：关键字必须是函数的形参名
fun(b=2, a=1, c=3)
print('='*30)
# 混合使用，先写位置传参，再写关键字传参
fun(10, c=30, b=20)
# fun(10, a=10,c=20)  # fun() got multiple values for argument 'a'
# fun(a=10, 20, 30) #  positional argument follows keyword argument
# 位置参数放在关键字参数的后面