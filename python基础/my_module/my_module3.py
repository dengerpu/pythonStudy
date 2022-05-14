num = 3


def fun():
    print(f'我是my_module{num}中的方法....')


class Dog(object):
    class_name = f'模块{num}'

    @classmethod
    def cls(cls):
        print(f'我是{cls.class_name}的静态方法')

    @staticmethod
    def sta():
        print('我是静态方法')

