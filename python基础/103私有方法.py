'''
私有方法：在方法的前边加上两个__,就为私有方法
私有方法，不能再类外部使用
作用：一般作为类内部使用，不让在外部直接调用，保证业务逻辑不被破坏
'''


class Dog(object):
    def born(self):
        print('生了一只小狗...')
        self.__sleep()

    def __sleep(self):
        print('休息30天')

class XTQ(Dog):
    pass

xtq = XTQ()
xtq.born()

dog = Dog()
dog.born()
# dog.__sleep()  #  'Dog' object has no attribute '__sleep'