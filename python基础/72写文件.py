# 1.打开文件w方式打开，文件不存在会创建文件，文件存在，覆盖原文件所有内容
f = open('1.txt', 'w', encoding='utf-8')
# 2.写文件 文件对象.write(写入文件的内容)
f.write('hello world!\n')
f.write('hello python!\n')
f.write('写入文字')  # windows默认是gbk,pycharm打开是utf-8
# 3.关闭对象
f.close()


# open函数打开文件，没有指定文件的编码，windows默认是gbk
# write函数将中文写入文件中，使用gbk编码编写
# 在 pycharm中双击打开文件，默认使用的是utf-8
# 使用utf-8打开gbk编码的数据，会出现乱码