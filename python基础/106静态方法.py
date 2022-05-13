'''
实例方法：类中默认定义的方法，就是实例方法，第一个参数self，标识实例对象
类方法：使用@classmethod装饰的方法，称为类方法，第一个参数是cls。代表的是类对象自己
静态方法：使用@staticmethod装饰的方法，称为静态方法，对参数没有特殊要求，可以有可以没有
什么情况下定义为实例方法，什么情况下定义为类方法，什么情况下定义为静态方法？
1. 如果在方法中使用了实例对象，那么该方法必须定义为实例方法
2. 前提：不需要使用实例属性，需要使用类属性，可以将这个方法定义为类方法
3. 前提：不需要使用实例属性，同时也不需要使用类属性，此时可以将这个方法定义为静态方法
'''

class Dog(object):
    class_name = '狗类'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play(self):  # 实例方法
        print(f'小狗{self.name}正在快乐的玩耍...')

    # def get_class_name(self):  # 是实例方法，因为没有使用实例属性，所以可以定义为类方法
    #     return Dog.class_name
    @classmethod
    def get_class_name(cls):
        return cls.class_name

    @staticmethod
    def show_info():  # 定义一个静态方法
        print('这是一个静态方法')


dog = Dog('大黄', 2)
dog.show_info()
Dog.show_info()
