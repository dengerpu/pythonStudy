# 匿名函数和普通函数的区别
# 1.匿名函数中不能呢个使用if语句，while循环，for循环，只能那个编写单上的表达式
# 2.匿名函数不需要返回结果，不需要使用return,表达式的运行结果就是返回结果，普通函数返回结果必须return
# 3.匿名函数也可以不返回结果。例如 lambda：print('hello')

# lambda 参数列表：表达式
# 1.无参无返回值
def fun1():
    print('hello')


(lambda :print('hello'))()
f1 = lambda :print('hello')
fun1()
f1()


# 2.无参有返回值
def fun2():
    return 1+2

f2 = lambda : 1+2
print(f2())


# 3.有参无返回值
def fun3(n):
    print(n)


f3 = lambda x: print(x)
f3('参数')


# 4.有参有返回值
def fun4(*args):
    return args

f4 = lambda *args : args
print(f4(1, 2, 3, 4))
