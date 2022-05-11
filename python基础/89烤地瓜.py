class Potato(object):
    def __init__(self):
        self.status = '生的'
        self.total_time = 0
        self.name_list = []  # 保存调料

    def cook(self, time):
        # 计算总时间
        self.total_time += time
        # 修改地瓜的状态
        if self.total_time < 3:
            self.status = '生的'
        elif self.total_time < 6:
            self.status = '半生不熟的'
        elif self.total_time < 8:
            self.status = '熟了'
        else:
            self.status = '糊了'

    def add(self, name):
        self.name_list.append(name)

    def __str__(self):
        # 字符串.join(列表)，将字符串添加到列表中的每个元素之间，组成新的字符串
        if self.name_list:
            return f'地瓜的状态《{self.status}》，烧烤总时间:<<{self.total_time}>> ，调料有:{",".join(self.name_list)}'
        else:
            return f'地瓜的状态《{self.status}》，烧烤总时间:<<{self.total_time}>> ,无添加调料'

potato = Potato()
print(potato)
potato.cook(2)
potato.add('油')
print(potato)
potato.cook(3)
potato.add('芝麻')
print(potato)
potato.cook(1)
potato.add('辣椒')
print(potato)
potato.cook(2)
print(potato)
