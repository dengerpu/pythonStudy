class Dog(object):
    def play(self):
        print('我是Dog中的play方法')

    def dog(self):
        print('汪汪汪....')


class God(object):
    def play(self):
        print('我是God中的play方法')

    def god(self):
        print('喵喵喵....')


# 定义XTQ类，继承Dog类和God类
# class XTQ(Dog, God):  # XTQ有两个父类，这个继承关系称为多继承，XTQ对象，可以调用两个父类中的属性和方法
class XTQ(God, Dog):  # XTQ有两个父类，这个继承关系称为多继承，XTQ对象，可以调用两个父类中的属性和方法
    pass

xtq = XTQ()
xtq.dog()
xtq.god()
xtq.play()  # 两个父类都存在play方法，调用的是第一个父类的方法