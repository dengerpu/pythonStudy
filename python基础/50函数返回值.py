# 函数想要返回一个数据值，给调用的地方，需要使用关键词 return
# return 关键词的作用 1.将return后边的数据值进行返回 2.程序代码遇到return，会终止（结束）运行
# 注意: return关键词必须写在函数中

def add(a, b):
    c = a +b
    return c
    print(f'求和的结果是{c}')  # 函数遇到return就结束了，不会执行return之后的代码


result = add(1,2)
print(result)


def fun(a, b):
    c = a + b
    d = a * b
    # 容器可以保存多个数据值，那么就可以将c和d放到容器中进行返回
    # return [c, d]
    # return (c, d)
    # return {0: c, 1: d}  # 以字典形式返回
    return c, d  # 默认是元组形式返回  (3, 2) <class 'tuple'>


result = fun(1, 2)
print(f'a+b的结果是{result[0]},a*b的结果是{result[1]}')
print(result, type(result))

# 不写return默认返回None


def func1():
    print('函数1 start...')
    print('函数1执行...')
    print('函数1 end...')
    pass


def func2():
    print('函数2 start...')
    func1()
    print('函数2 end...')
    pass


print('*'*30)
# print(func1())
func2()
