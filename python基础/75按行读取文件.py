f = open('1.txt', 'r', encoding='utf-8')
# buf = f.readline()  # 一次读取一行的内容，返回值是读取到的内容（str）
# print(buf)
buf = f.readlines()  #按行读取，一次读取所有行，返回值是列表，列表的每一项是一个字符串，即每一行的内容
print(buf)
buf = [i.strip() for i in buf]  # strip方法可以去掉\n和空格
print(buf)
f.close()