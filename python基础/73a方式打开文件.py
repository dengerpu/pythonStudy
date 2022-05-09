# a 方式打开文件，追加内容，在文件的末尾加入内容
# 文件不存在，会创建文件
# 注意点，不管是a方式打开软件还是w方式打开文件，写内容用的都是write()函数
f = open('b.txt', 'a', encoding='utf-8')
f.write('我是第一行\n')
f.write('我是第二行\n')
f.close()