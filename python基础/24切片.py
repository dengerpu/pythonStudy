# 切片是指对操作的对象截取其中一部分的操作。字符串，列表，元祖都支持切片
# 切片可以获取一段数据，多个数据，下标（索引只能获得一个数据）
# start 开始位置的下标
# end 结束位置的下标，不包含end对应的下标
# step 步长，下标之间的间隔，默认是1
my_str = 'hello'
my_str1 = my_str[2:4:1] #ll
print(my_str1)

# step如果是1，即默认值，可以不写
my_str2 = my_str[2:4]
print(my_str2)

# end位置不写，表示是len(),即可以获取到最后一个元素
my_str3 = my_str[2:]  # llo
print(my_str3)

# start位置不写，从0开始
my_str4 = my_str[:3]    # hel
print(my_str4)

#start 和 end都不写，但是冒号需要写
my_str5 = my_str[:]  # 字符串拷贝
print(my_str5)

my_str6 = my_str[-4:-1]  # ell
print(my_str6)
print(my_str[3:1])  # 没有数据

# 步长可以是负数
print(my_str[3:1:-1])   # ll

# 字符串逆序
print(my_str[::-1])

print(my_str[::2]) # 0 2 4 6

# 常用 my_str[:]和原来一样的字符串
#       my_str[::-1]    字符串的逆置

