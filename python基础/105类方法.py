'''
实例方法：类中默认定义的方法，就是实例方法，第一个参数self，标识实例对象
类方法：使用@classmethod装饰的方法，称为类方法，第一个参数是cls。代表的是类对象自己
什么情况下定义为实例方法，什么情况下定义为类方法？
1. 如果在方法中使用了实例对象，那么该方法必须定义为实例方法
2. 前提：不需要使用实例属性，需要使用类属性，可以将这个方法定义为类方法
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


dog = Dog('大黄', 2)
print(dog.class_name)
print(dog.get_class_name())
#类名.类方法（）
print(Dog.get_class_name())
