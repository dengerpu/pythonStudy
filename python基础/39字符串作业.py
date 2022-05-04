# 如果需要使用变量保存以下字符串，我们该如何书写代码
# 鲁迅说:"我没有说过这句话"
words = '''鲁迅说:"我没有说过这句话"'''
print('鲁迅说:"我没有说过这句话"')
print(words)


# 做一个简单的用户信息管理系统：
# 提示用户依次输入姓名，年龄和爱好
# 并且在输入完成之后，一次性将用户输入的数据展示出来
# name = input('请输入姓名：')
# age = int(input('请输入年龄：'))
# hobby = input('请输入爱好：')
# print('我是:%s,今年%d岁，我的爱好是%s' % (name, age, hobby))
# print(F'我是{name}，今年{age}岁，我的爱好是{hobby}')

# 现有字符串如下，请使用切片提取出ceg
words = "abcdefghi" #  -9 -8 -7 -6 -5 -4 -3 -2 -1
print(words[2:7:2])
print(words[-7:-2:2])


# james有一个关于爬虫的项目，他需要在一个字符串中查找python这个关键字，
# 当前他通过index()函数进行查找，虽然可以实现查找的需求，但是总会在
# 没有查找到关键字的时候报错，为什么会报错，如何优化？
words = "hello pyho ,no I am python"
print(words.find('python'))
if 'python' in words:
    print('查找到')
    print(words.index('python'))
else:
    print('查找失败')
# 只需要使用find函数替换掉index函数即可，在功能上, find函数index函数完全一致,不同的是index函数在没有查找到关键字的情况下会报ValueError的异常,因此在一般开发环境下通常都会使用find函数


# 1，判断单词great是否在字符串words中，如果在，则将每一个great后面加一个s， 如果不在则输出 great不在该字符串中
# 2，将整个字符串的每一个单词都变成小写，并使每一个单词的首字母变成大写
# 3，去除首尾的空白，并输出处理过后的字符串
words = " great craTes Create great craters, But great craters Create great craters "
num = words.find('great')
if num != -1:
    print(words.replace('great', 'greats'))
else:
    print(' great不在该字符串中')
print(words.lower().title())  # 单词变成小写，再将每个单词的首字母都大写
print(words.strip())  # 去掉首尾的空白

words = " great craTes Create great craters, But great craters Create great craters "

# 判断单词great是否在这个字符串中
if 'great' in words:
    # 将每一个great替换成greats
    words = words.replace("great", "greats")
    # 将单词变成小写
    words = words.lower()
    # 将每一个单词的首字母都大写
    words = words.title()
    # 去除首尾的空白
    words = words.strip()
    # 最后进行输出
    print(words)
else:
    print("great不在该字符串中")
