class Car(object):
    def __init__(self, type, num):
        self.type = type
        self.num = num

    def start(self):
        pass

    def stop(self):
        pass


class Taxi(Car):
    def __init__(self, type, num ,company):
        super().__init__(type, num)
        self.company = company

    def start(self):
        print('乘客你好！')
        print(f'我是{self.company}出租车公司的，我的车牌号是{self.num}, 请问你要去哪里？')

    def stop(self):
        print('目的地到了，请付款下车，欢迎再次乘坐')


class FamilyCar(Car):
    def __init__(self, type, num, name):
        super().__init__(type, num)
        self.name = name

    def start(self):
        print(f'我是{self.name},我的车我做主')

    def stop(self):
        print('目的地到了，我们去玩把')


fc = FamilyCar('私家车', '京B12345', '张三' )
fc.start()
fc.stop()
print('-'*30)
taxi = Taxi('出租车', '京A12345', '美团')
taxi.start()
taxi.stop()
