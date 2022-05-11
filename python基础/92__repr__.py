my_list = ['hello', 'python', 'cpp']  # 列表存储了三个字符串对象
print(my_list)

class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name},{self.age}'

    def __repr__(self):
        '''repr方法和str方法，非常类似，也是必须返回一个字符串'''
        return f"我是repr方法，{self.name}，{self.age}"


my_list = [Dog('大黄', 1), Dog('小黄', 0), Dog('小白', 3)]
# print(my_list)  # 不加repr方法，打印的是地址 [<__main__.Dog object at 0x0000019D84E67780>, <__main__.Dog object at 0x0000019D84E6FE10>, <__main__.Dog object at 0x0000019D84E6F7F0>]
print(my_list)  # [我是repr方法，大黄，1, 我是repr方法，小黄，0, 我是repr方法，小白，3]

dog = Dog('小花', 1)
print(dog)