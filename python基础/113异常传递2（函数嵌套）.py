def fun1():
    print('---------1---------')
    num = input('请输入数字')
    num = 10 / int(num)
    print(num)
    print('---------2---------')


def fun2():
    print('---------3---------')
    fun1()
    print('---------4---------')

try:
    print('---------5---------')
    fun2()
    print('---------6---------')
except Exception as e:
    print('---------7---------')
    print(e)