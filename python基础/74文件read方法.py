# 1.打开文件
f = open('b.txt', 'r', encoding='utf-8')
# 2.读写文件 文件对象.read（n） n一次读物多少字节内容，默认不写读取全部
buf = f.read(3)
print(buf)
buf = f.read(3)  #得到的是 4\n5
print(buf)
f.close()