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
    def play(self):
        print('子类重写play方法，调用子类自己的方法')
        # 调用指定父类中的方法
        # 方法一  类名.方法名（self，参数）
        # Dog.play(self)
        # God.play(self)

        # 方法二 super(类A，self).方法名（参数） 类A的父亲（继承顺序链的下一个类）中的方法
        # (<class '__main__.XTQ'>, <class '__main__.God'>, <class '__main__.Dog'>, <class 'object'>)
        # super(XTQ, self).play()  # 调用God的方法
        super(God, self).play()  # 调用Dog类的方法
        # super(Dog, self).play()  # 调用object中的方法，object没有这个方法，报错

# 类名.__mro__可以查看当前类的继承顺序链，也叫方法的调用顺序
print(XTQ.__mro__)  # (<class '__main__.XTQ'>, <class '__main__.God'>, <class '__main__.Dog'>, <class 'object'>)

xtq = XTQ()
xtq.play()