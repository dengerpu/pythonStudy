class Dog(object):
    # self 作为类中方法的第一个形参，在通过对象调用方法的时候，不需要手动传递室实参值
    # 是python解释器自动将调用该方法的对象传给self,所以self这个形参代表的是对象
    def play(self):
        print(f'self:{id(self)}')
        print(f'{self.name}正在拆家....')


dog = Dog()
dog.name = '小黄'
print(f'dog:{id(dog)}')
dog.play()

dog1 = Dog()
dog1.name = '小白'
dog1.play()