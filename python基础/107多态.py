"""
在需要使用父类对象的地方，也可以传入子类对象，得到不同的结果----多态
实现步骤：
1. 子类继承父类
2. 子类重写父类中的同名方法
3. 定义一个共同的方法，参数为父类对象，在方法中调用子类和父类同名的方法
"""


class Dog(object):
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f'这是父类的play方法，我是{self.name}')


class XTQ(Dog):
    def play(self):
        print(f'这是子类的play方法，我是{self.name}')


def play_(obj_dog):
    obj_dog.play()

dog = Dog('大黄')
play_(dog)

xtq = XTQ('大黄')
play_(xtq)

dog.play()
xtq.play()