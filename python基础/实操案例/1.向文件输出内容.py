#  1.使用print方式进行输出（输出的目的是文件）
fp = open('text.txt', 'w', encoding='utf-8')
print('奋斗成就更好的你', file=fp)
fp.close()

# 第二种方式，使用文件读写操作
with open('text.txt', 'a+', encoding='utf-8') as file:
    file.write('奋斗成就更好的你')
