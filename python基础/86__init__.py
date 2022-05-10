# 在python中，有一类方法，这类方法以  两个下划线开头 和 两个下划线结尾，并且 在
# 满足特定条件的情况下，会自动调用，这类方法称为魔法方法

# __init__ 在创建对象之后，会立马调用
# 作用：1.用来给对象添加属性，给对象属性一个初始值（构造函数）
#      2.代码的业务需求，每创建一个对象，都需要执行的代码可以写在里面

class Dog(object):
    def __init__(self, name):  # self是对象
        print('init方法执行了...')
        # 对象.属性名 = 属性值
        self.name = name

dog = Dog('小黄')
print(dog.name)

dog1 = Dog('小白')
print(dog1.name)

