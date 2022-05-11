# 定义房子类
class House(object):
    def __init__(self, address, area):
        self.address = address
        self.h_area = area
        self.furniture_list = []
        self.free_area = area  # 房子的剩余面积

    def add_furniture(self , obj_furniture):
        '''添加家具 obj_furniture: 家具类的对象'''
        if self.free_area > obj_furniture.area:
            self.furniture_list.append(obj_furniture)
            # 修改剩余面积
            self.free_area -= obj_furniture.area
            print(f'家具：{obj_furniture.name}添加成功')
        else:
            print('添加失败，房子太小了')

    def __str__(self):
        # 自定义家具类，将该类的对象添加到列表中（容器），直接打印列表，显示的是 自定义对象的引用地址
        # [家具对象，家具对象，...] -》 [家具类型，家具类型，...]
        buf_list = [ obj.name for obj in self.furniture_list]
        if self.furniture_list:
            return f'房子的地址为《{self.address}》，占地面积为：{self.h_area}，剩余面积为：{self.free_area}，家具有：{",".join(buf_list)}'
        else:
            return f'房子的地址为《{self.address}》，占地面积为：{self.h_area}，剩余面积为：{self.free_area},还没有家具'

# 定义家具类Furniture类
class Furniture(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f'家具类型：《{self.name}》，面积：{self.area}'


house = House('中国', 120)
print(house)
bed = Furniture('豪华双人床',15)
print(bed)
house.add_furniture(bed)
print(house)
table = Furniture('餐桌', 5)
print(table)
house.add_furniture(table)
print(house)