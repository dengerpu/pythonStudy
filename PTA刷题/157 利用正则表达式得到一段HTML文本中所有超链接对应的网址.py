# 编写程序实现以下功能：利用正则表达式得到一段HTML文本中所有超链接对应的网址，并将网址输出到屏幕上（每行输出一个网址）。
#
# 输入格式:
# 从键盘输入
# 一段HTML文本，多行输入，空行输入
# 结束。
#
# 输出格式:
# 输出从HTML文本中提取到的超链接所对应的网址，一行一个网址。
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# < h3
#
#
# class ="c-title" >
#
# < a
# href = "https://baijiahao.baidu.com/s?id=1633289774665320636&amp;wfr=spider&amp;for=pc"
# data - click = "{
# 'f0': '77A717EA',
# 'f1': '9F63F1E4',
# 'f2': '4CA6DE6E',
# 'f3': '54E5243F',
# 't': '1557660267'
# }" target="
# _blank
# ">
# 影片《周恩来回延安》在 < em > 南开大学 < / em > 点映开启全国路演
#                             < / a >
#                                 < / h3 >
#                                     < a
# href = "https://baijiahao.baidu.com/s?id=1632116753423885280&amp;wfr=spider&amp;for=pc"
# data - click = "{
#                'f0':'77A717EA',
#                     'f1': '9F73F1E4',
# 'f2': '4CA6DE6E',
# 'f3': '54E5243F',
# 't': '1557660267'
# }" target="
# _blank
# ">
# 天津“ < em > 南开大学 < / em >”——莘莘学子的梦想之地
#                            < / a >
#
#                                输出样例:
# 在这里给出相应的输出。例如：
#
# https: // baijiahao.baidu.com / s?id = 1633289774665320636 & amp;
# wfr = spider & amp; for =pc
# https: // baijiahao.baidu.com / s?id = 1632116753423885280 & amp;
# wfr = spider & amp; for =pc


# 在re模块中, 通常使用三种方法, match, search和findall, 下面对这三种方法进行简单的介绍:
#
# 1.
# match方法
# re.match
# 尝试从字符串的起始位置匹配一个模式，匹配成功则返回的是一个匹配对象（这个对象包含了我们匹配的信息），如果不是起始位置匹配成功的话，match()
# 返回的是空，
# 注意：match只能匹配到一个 **
#
# 下面来看代码理解
#
# s = 'python123python666python888'
#
# result = re.match('python', s)
# print(result)  # <re.Match object; span=(0, 6), match='python'>
# print(result.span())  # (0, 6)
# print(result.group())  # python
# 1.
# 通过span()
# 提取匹配到的字符下标
# 2.
# 通过group()
# 提取匹配到的内容
# 而s字符串中有3个python的存在, match只能匹配到一个
#
# 下面我们改变一下s, 得到不一样的结果
#
# s = '1python123python666python888'
#
# result = re.match('python', s)
# print(result)  # None
# 因为match从字符串的起始位置开始匹配, 这里起始的第一个字符为1, 所以匹配失败返回None.
# 那么我们要如何才能匹配到字符串中间我们想要的部分呢, 这个时候就用到了search函数
#
# 2.
# search方法
# re.search
# 扫描整个字符串, 匹配成功则返回的是一个匹配对象（这个对象包含了我们匹配的信息）
# 注意：search也只能匹配到一个，找到符合规则的就返回，不会一直往后找
# 同样的, search也只能匹配到一个.
# 代码如下
#
# s = '1python123python666python888'
#
# result = re.search('python', s)
# print(result)  # <re.Match object; span=(1, 7), match='python'>
# print(result.span())  # (1, 7)
# print(result.group())  # python
# 当然, 若是都找不到则返回None值
#
# s = '1python123python666python888'
#
# result = re.search('python98', s)
# print(result)  # None
# *search方法虽然解决了match的从头匹配的弊端, 但它也只能匹配到一个, 这个时候我们就可以使用findall方法了 *
#
# 3.
# findall方法：
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
#
# s = '1python123python666python888'
#
# result = re.findall('python', s)
# print(result)  # ['python', 'python', 'python']
import re
my_string = ''
try:
    while True:
        value = input()
        my_string += value
except EOFError:
    pass
web_list = re.findall('href=".*?"', my_string)
# print(web_list)
for website in web_list:
    website = website.replace('href=', '').replace('"', '')
    print(website)