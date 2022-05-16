# 1.请写出单继承的格式?
class Dog(object):
    pass

# 2.什么是重写.为什么要重写?
# 重写: 子类实现父类中的同名方法
# 父类中的方法不能满足子类对象的需求

# 3.如何将一个属性变为私有的?
# 在属性名前加上两个下划线

# 4.定义类方法的语法格式?
# 使用@classmethod 装饰的方法,是类方法
class MyClass(object):
    @classmethod
    def class_method(cls):
        pass

# 5.定义静态方法的语法格式?
class MyClass(object):
    @staticmethod
    def static_method():
        pass

# 6. 请判断下面类中哪些是类属性,哪些是实例属性?
# class Car(obj):
#  	addr = "china"  # 类属性
#  	def __init__(self):
#      	self.name = 'changcheng'  # 实例属性
#      	self.money = 100000  # 实例属性


# 7.判断题
# a.一个子类可以继承多个父类  # 正确
#
# b.类中的方法可以有return，也可以没有return  # 正确
#
# c.类方法和静态方法是一样的  # 错误
#
# d.删除对象时，默认调用
# __init__
# 方法  # 错误,创建对象调用__init__ 方法,删除对象调用 __del__ 方法
#
# e.python3中object是所有类的父类  # 正确
#
# f.python中不支持多继承  # 错误
#
# g.父类中的所有方法和属性都会被继承  # 错误私有方法和属性不会继承
#
# h.一个对象可以当做一个参数来传递  # 正确
#
# i.如果类属性和实例属性名字相同，那么实例对象调用时候使用的是类属性  # 错误,实例对象,调用的是实例属性
#
# j.实例对象不可以访问类属性  # 错误
#
# k.重写方法后，父类对象默认调用重写后的方法  # 错误,子类调用重写后的方法,父类调用父类自己的方法
#
# l.类方法不可以通过实例对象来调用，只能通过类对象调用  # 错误
#
# m.一个类只能创建一个对象  # 错误


# 1. 创建一个Animal（动物）基类,其中有一个run方法,输出`跑起来....`
# 2. 创建一个Horse（马）类继承于动物类，Horse类中不仅有run方法还有eat方法
#    1. run方法输出 `跑起来....`
#    2. eat 方法输出 `吃东西...`
class Animal(object):
    def run(self):
        print('跑起来....')


class Horse(Animal):
    def eat(self):
        print('吃起来...')


horse = Horse()
horse.run()
horse.eat()

print("="*30)
# 创建一个动物(Animal)的基类,其中有一个run方法, 输出`跑起来....`
# 创建一个Horse（马）类继承于动物类，Horse类中重写run方法，增加打印输出"迈着矫健的步伐跑起来"，同时实现eat方法, 输出 `吃东西...`


class Animal(object):
    def run(self):
        print('跑起来....')


class Horse(Animal):
    def run(self):
        # Animal.run(self)
        # super(Horse,self).run()
        super().run()
        print("迈着矫健的步伐跑起来")
    def eat(self):
        print('吃起来...')


horse = Horse()
horse.run()
horse.eat()

print("="*30)
# 1. 创建一个动物(Animal)的基类,其中有一个run方法, 输出`跑起来....`
# 2. 创建一个Horse（马）类继承于动物类，Horse类中不仅有run方法还有eat方法
#    1. run方法输出 `跑起来....`
#    2. eat 方法输出 `吃东西...`
# 3. 创建一个 SwiftHorse（千里马）类继承Horse类，初始化init方法name属性为千里马
class SwiftHorse(Horse):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'我是{self.name}'


swifthorse = SwiftHorse('千里马')
swifthorse.run()
swifthorse.eat()
print(swifthorse)

print("="*30)
# 1. 创建一个动物(Animal)的基类,其中有一个run方法, 输出`跑起来....`
# 2. 创建一个Horse（马）类继承于动物类，Horse类中不仅有run方法还有eat方法
#    1. run方法输出 `跑起来....`
#    2. eat 方法输出 `马吃东西...`
# 3. 创建一个Donkey（驴）类继承于动物类，Donkey类中不仅有run方法还有eat方法
#    1. run方法输出 `跑起来....`
#    2. eat 方法输出 `驴吃东西...`
# 4. 创建一个Mule（骡子）类继承于Horse，Donkey，初始化name为 骡子。
#    问题: 创建 Mule 类的对象, 调用 eat 方法,调用的是哪个父类中的方法?


class Donkey(Animal):
    def eat(self):
        print('驴吃东西...')

class Mule(Horse, Donkey):
    def __init__(self):
        self.name = '骡子'

mule = Mule()
mule.run()
mule.eat()

print("="*30)
# 创建一个动物类(Animal),其中有一个run方法
# 创建一个Cat类继承于动物类，具有私有属性__name = "波斯猫"
# 创建一个Dog类继承于动物类,具有私有属性__name = "京巴狗"
# Cat类中不仅有run方法还有eat方法
# Dog类中方法同上
# 创建一个letRun函数，可以接收动物及其子类对象，并调用run方法 class Cat(Animal):
# 编写测试代码以验证功能正常


class Animal(object):
    def run(self):
        print('我是Animal中的run方法...')


class Cat(Animal):
    def __init__(self):
        self.__name = "波斯猫"

    def run(self):
        print('%s在跑' % self.__name)

    def eat(self):
        print(f'{self.__name}正在吃...')


class Dog(Animal):
    def __init__(self):
        self.__name = "京巴狗"

    def run(self):
        print('%s在跑' % self.__name)

    def eat(self):
        print(f'{self.__name}正在吃...')

def letRun(obj):
    obj.run()

animal = Animal()
letRun(animal)

# 猫测试
cat = Cat()
letRun(cat)
cat.eat()

# 狗测试
dog = Dog()
letRun(dog)
dog.eat()


print("="*30)
# 定义一个`Person` 类,包含初始化 init 方法:
# 实例属性: 名字, name
# 						年龄, age
# 1. 记录由该类创建的对象的个数,创建一个对象,计数+1, 删除一个对象,计数减一
# 2. 定义一个方法,可以打印当前对象的个数
# 3. 定义一个方法`show_info`, 输出以下信息
#    ```
#    这是一个 Person 类,谢谢查看!
#    ```
# 4. 打印对象的时候,可以输出打印自己的名字和年龄
#    ```python
#    我的名字是 xxx, 年龄是 xxx
#    ```
# 5. 定义一个方法 `study`, 输出以下信息
#    ```python
#    我叫 xxx, 我要好好学习
#    ```
# 6. 操作步骤
#    1.  调用`show_info `方法
#    2.  创建两个对象, 打印当前对象,并打印当前的对象个数
#    3.  分别使用两个对象调用`study`方法
#    4.  删除一个对象,打印输出当前的对象个数


class Person(object):
    # 定义类属性,count,统计该类创建的对象的个数
    __count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.__count += 1

    @classmethod
    def get_count(cls):
        return cls.__count

    @staticmethod
    def show_info():
        print('这是一个 Person 类,谢谢查看!')

    def __str__(self):
        return f'我的名字是 {self.name}, 年龄是 {self.age}'

    def study(self):
        print(f'我叫 {self.name}, 我要好好学习')

    # 定义__del__方法
    def __del__(self):
        Person.__count -= 1

# 调用 show_info 方法
Person.show_info()
print(Person.get_count())
xw = Person('小王', 18)
print(xw, xw.get_count())
xh = Person('小红', 18)
print(xh, xh.get_count())


xw.study()
xh.study()

del xw
print(Person.get_count())
