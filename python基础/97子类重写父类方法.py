# 重写：子类定义和父类名字相同的方法
# 为什么重写：父类中的方法，不能满足子类对象的需求，所以要重写
# 重写之后的特点：子类对象调用子类自己的方法，不再调用父类的方法，父类对象调用父类自己的方法
class Dog(object):
    def bark(self):
        print('汪汪叫....')


# 子类重写父类的方法
class XTQ(Dog):
    def bark(self):
        print('子类重写父类的方法...')


dog = Dog()
dog.bark()

xtq = XTQ()
xtq.bark()