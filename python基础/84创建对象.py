# 定义类
class Dog(object):
    # 在类中定义函数，称为方法。
    def play(self, name):
        print(f'{name}正在快乐的拆家....')


# 创建对象 变量 = 类名（）
dog = Dog()
print(dog, id(dog), type(dog))  # <class '__main__.Dog'>

dog.play('小黄')   # 可以使用对象调用类中的方法，对象.方法名（）

dog1 = Dog()
print(dog1, id(dog1))

# 给对象添加属性   对象.属性名 = 属性值
dog.name = '大黄'  # 给dog对象添加name属性，属性值是大黄
dog.age = 1
print(dog.name)
print(dog.age)

# 修改属性值，和添加一样。存在就是修改，不存在就是添加
dog.name = '小黄'
print(dog.name)