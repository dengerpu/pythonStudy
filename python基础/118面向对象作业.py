#  定义一个`Star`类(明星类)， 通过明星类创建一个zhou_xing_chi对象。
#
# ​	 明星姓名= “周星驰”
#
# ​	 明星的电影 = “功夫”
import sys


class Star(object):
    def __init__(self, name, movie):
        self.name = name
        self.movie = movie

    def __str__(self):
        return f'明星姓名="{self.name}"\n明星的电影="{self.movie}"'


zhou_xing_chi = Star('周星驰', "功夫")
print(zhou_xing_chi)

class Star1(object):
    pass


zhou_xing_chi = Star1()
zhou_xing_chi.name = '周星驰'
zhou_xing_chi.movie = '功夫'
print(zhou_xing_chi.name)
print(zhou_xing_chi.movie)

# 定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象
# 使用init方法给对象添加属性
# 定义方法playing()，打印“xxx出演了yyy，非常好看”
print("="*30)


class Star2(object):
    def __init__(self, name, movie):
        self.name = name
        self.movie = movie

    def playing(self):
        print(f'{self.name}出演了{self.movie}')


zhou_xing_chi = Star2('周星驰', '功夫')
zhou_xing_chi.playing()

# 定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象
# 使用init方法给对象添加属性
# print输出对象时打印"xxx是我的偶像，我非常喜欢他的电影yyy"
# xxx为明星姓名，yyy是电影的名字
print("="*30)


class Star3(object):
    def __init__(self, name, movie):
        self.name = name
        self.movie = movie

    def __str__(self):
        return '%s 是我的偶像，我非常喜欢他的电影%s' % (self.name, self.movie)


zhou_xing_chi = Star3('周星驰', "功夫")
print(zhou_xing_chi)


# 定义一个star类(明星类)， 通过明星类创建一个zhou_xing_chi对象
# 使用init方法给对象添加属性
# 删除创建的对象，打印“我不喜欢xxx了”
print("="*30)


class Star4(object):
    def __init__(self, name, movie):
        self.name = name
        self.movie = movie

    def playing(self):
        print(f'{self.name}出演了{self.movie}')

    def __str__(self):
        return '%s 是我的偶像，我非常喜欢他的电影%s' % (self.name, self.movie)

    def __del__(self):
        print(f'我不喜欢{self.name}了')

zhou_xing_chi = Star4('周星驰', '功夫')
print(sys.getrefcount(zhou_xing_chi))  # 查看参数的引用计数，比实际多1
del zhou_xing_chi

#  a.定义一个Star类(明星类)，包含初始化init方法：
#  成员属性：明星姓名
# ​		    明星的电影
# 成员方法：playing()
# ​	打印：“xxx出演了yyy，非常好看”
# 打印对象时显示“xxx是我的偶像，我非常喜欢他的电影yyy”
# 删除对象提示“xxx我不再喜欢了”
# xxx为明星姓名，yyy是电影的名字
print("="*30)
my_list = []
for i in range(3):
    name = input('请输入你喜欢的明星：')
    movie = input('请输入电影名：')
    zhou_xing_chi = Star4(name, movie)
    my_list.append(zhou_xing_chi)

for i in my_list:
    i.playing()
    print(i)


