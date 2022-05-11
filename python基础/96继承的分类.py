class Animal(object):
    def play(self):
        print('快乐的玩耍...')


# 定义Dog类继承Animal类
class Dog(Animal):  # Dog-->Animal单继承  Dog-->Animal-->object这种称为多层继承
    def bark(self):
        print('汪汪叫...')

class XTQ(Dog):  # XTQ-->Dog单继承  XTQ-->Dog-->Animal 多层继承
    pass

xtq = XTQ()
xtq.play()
xtq.bark()

# 单继承：如果一个类只有一个父类，把这种继承关系称为单继承
# 多继承：如果一个类有多个父亲，那么这种继承关系称为多继承


