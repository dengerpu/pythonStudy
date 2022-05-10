# 1.print(对象)，会自动调用__str__对象，打印输出的结果是 __str__方法的返回值
# 2.str(对象) 类型转换，将自定义对象转换为字符串的时候，会自动调用
# 应用：1.打印对象的时候，输出一些属性信息
#      2.需要将对象转换为字符串的时候
# 方法必须返回一个字符串，只有一个self对象

class Dog1(object):
    pass

class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        print('我是str,我被调用了')
        return f'{self.name}，年龄：{self.age}'


dog = Dog('小黄', 18)
print(dog)      # 没有定义__str__方法，print(对象)，默认输出对象的引用地址
str_dog = str(dog)  # 没有定义__str__方法，类型转换，赋值也是引用地址
print(str_dog)


dog1 = Dog1()  # <__main__.Dog1 object at 0x00000260DAA9F9B0>
print(dog1)
str_dog = str(dog1)  # 没有定义__str__方法，类型转换，赋值也是引用地址
print(str_dog)  # <__main__.Dog1 object at 0x000001ECFE78EE10>