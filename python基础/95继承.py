# 继承：描述的类与类之间所属关系
# class 类B（类A）：  类B继承类A
# 特点 B类的对象可以使用A类的属性和方法
# 优点：代码复用
# 名词：类A：父类    基类
#      类B：子类    派生类
class Animal(object):
    def play(self):
        print('快乐的玩耍...')


# 定义Dog类继承Animal类
class Dog(Animal):
    pass

dog = Dog()
dog.play()  # 子类调用父类的方法