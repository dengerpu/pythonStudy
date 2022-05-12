class Dog(object):
    def __init__(self, name):
        self.age = 0
        self.name = name

    def __str__(self):
        return f'名字：{self.name}，年龄：{self.age}'


class XTQ(Dog):
    # 子类重写了父类的—__init__方法，默认不再调用父类的init方法，需要手动调用父类的init方法
    def __init__(self, name, color):
        super().__init__(name)  # 子类init方法的形参，一般都先写父类的形参，再写自己独有的形参
        self.color = color

    def __str__(self):
        return f'名字：{self.name}，年龄：{self.age},颜色：{self.color}'



xtq = XTQ('大黄', '红色')
print(xtq)