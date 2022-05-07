# 函数传参传递的也是引用
my_list = [1, 2, 3]


def fun(a):
    a.append(4)


def fun1():
    # 为啥不加global,因为没有修改my_list的引用值
    my_list.append(5)


def fun2():
    global my_list
    my_list = [1, 2, 3]  # 修改全局变量的值


def fun3(a):
    # += 对于列表来说,类似列表的extend方法,不会改变变量的引用地址
    a += a  # a = a+a ,修改了变量a的引用

fun(my_list)
print(my_list)
fun1()
print(my_list)
fun3(my_list)
print(my_list)

b = 4
fun3(b)  # b的值不会发生变化
print(b)

