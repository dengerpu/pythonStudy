# __del__析构函数
# 对象在内存中被销毁删的时候（引用计数为0）会自动调用__del__方法
# 1.程序代码运行结束，创建的所有对象和变量都会被删除销毁
# 2.使用 del 变量  ，将这个对象的引用计数变为0，会自动调用__del__方法
#  对象被删除销毁的时候，要书写的代码可以写在__del__中，一般很少使用


# 引用计数：是python内存管理的一种机制，是指一块内存，有多少个变量在引用
# 1.当一个变量，引用一块内存的时候，引用计数加1
# 2.当删除一个变量，或者这个变量不在引用这块内存，引用计数减1
# 3.当内存的引用计数变为0的时候，这个内存被删除，内存的数据被销毁
# my_list = [1,2,3] # 引用计数1
# my_list1 = my_list # 引用计数2
# del my_list # 引用计数1
# del  my_list1 引用计数0

class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name:{self.name},age:{self.age}'

    def __del__(self):
        print(f'我是del方法，我被调用了，{self.name}被销毁了')

# dog = Dog('大黄', 2)
# dog1 = Dog('小白', 1)

dog = Dog('小白', 1)  # 小白，引用计数1
dog2 = dog  # 小白引用计数2
print('第一次删除之前')
del dog  # 小白引用计数为1
print('第一次删除之后')
print('第二次删除之前')
del dog2  # 小白引用计数为0，引用计数为0会立即执行del方法
print('第二次删除之后')