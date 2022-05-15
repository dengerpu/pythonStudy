def add(a, b):
    print(f'add函数中的结果：{a + b}')
    # print(__name__)


if __name__ == '__main__':
    print('__name__执行了....')
    add(10, 20)
    # __name__变量，在每个模块即代码文件中都有，是系统自己定义的
    # 1.直接运行当前代码， 值为__main__
    # 2.把文件作为模块导入时，运行，结果是my_calc(文件名)
    print(__name__)