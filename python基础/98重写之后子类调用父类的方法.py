class Dog(object):
    def bark(self):
        print('父类的方法....')


# 子类重写父类的方法
class XTQ(Dog):
    def bark(self):
        print('子类重写父类的方法...')
    def fu(self):
        # 想要在子类中调用父类同名的方法
        #  方法一：父类名.方法名（self,其他参数），通过实例对象.方法名（）调用方法，不需要给self传递实参值
        # python解释器会自动将对象作为实参值传递给self形参，如果通过类名.方法（）调用，python解释器就
        # 不会自动传递实参值，需要手动给self传递实参值
        # Dog.bark()  # bark() missing 1 required positional argument: 'self'
        Dog.bark(self)
        Dog().bark()
        # 方法二 super(类A，self).方法名（参数），会调用类A的父类的方法
        super(XTQ, self).bark()
        # 方法三，是方法二的简写，super（）.方法名（参数）==》super(当前类， self).方法名（）
        super().bark()


xtq = XTQ()
xtq.fu()