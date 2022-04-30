name = "邓二浦"
print("我的名字是%s,哈哈哈"% name)

age = 18
print("我的年龄：%d" % age)

# %n.f保留n位小数
height = 175.5
print("我的身高%.2f cm" % height)

print("我的名字是：%s,年龄：%d,身高:%.2f" % (name,age,height))

# 输出50%，使用格式化输出的时候，想要输出一个%,需要使用两个%%
print("及格人数占比为%d%%" % 50)

# python3.6版本开始支持f-string，占位符统一使用{}，填充的数据直接写{}
print(f"我的名字是{name}，年龄：{age}，身高：{height}")

# print()函数输出以后默认会添加一个换行，如果不要换行可以去掉
print('hello',end='')  # hello
print('world')      # 两个合起来输出 helloworld
print('hello',end='_*_')
print('\nhelloworld')

