# 1.打开文件，将文件从磁盘读到内存中
# open(file, mode='r', encoding)
# file 要操作的文件名字，类型是str
# mode,文件打开的方式 r(read)只读打开,w(write)只写打开 a(append)追加打开
# encoding 文件的编码格式，常见的编码格式有两种，gbk和utf-8
# 返回值，文件对象，后续所有的文件操作，都需要通过这个文件对象进行

# 以只读的当时打开当前目录的文件，文件不存在会报错
f = open('text.txt', 'r')  # 当文件不存在时No such file or directory: '1.txt'
# 2.读文件  文件对象.read（）
buf = f.read()
print(buf)

# 3.关闭文件 文件.close()  将内存中文件同步到磁盘中
f.close()
