my_str = 'hello world itcast and itcastcpp'

# 字符串的所有方法都不会改变原字符串
# strip不能去掉中间的空格

# <1>capitalize
# 把字符串的第一个字符大写
print(my_str.capitalize())  # Hello world itcast and itcastcpp

# <2>title
# 把字符串的每个单词首字母大写
print(my_str.title())  # Hello World Itcast And Itcastcpp

# <3>startswith
# 检查字符串是否是以 hello 开头, 是则返回 True，否则返回 False
print(my_str.startswith('hello'))  # True
print(my_str.startswith('hello', 1))  # False 从1号下标开始

# <4>endswith
# 检查字符串是否以obj结束，如果是返回True,否则返回 False.
print(my_str.endswith('hello'))  # False
print(my_str.endswith('cpp'))  # True

# <5>lower
# 转换 mystr 中所有大写字符为小写
my_str1 = my_str.upper()
print(my_str1)  # HELLO WORLD ITCAST AND ITCASTCPP
print(my_str1.lower())  # 又变回小写

# <6>upper
# 转换 mystr 中的小写字母为大写
print(my_str.upper())  # HELLO WORLD ITCAST AND ITCASTCPP

name = 'hello'
# <7>ljust
# 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
print(name.ljust(30), end='|\n')  # hello                         |

# <8>rjust
# 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
print(name.rjust(30), end='|\n')  #                          hello|

# <9>center
# 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
print(name.center(30), end='|\n')  #             hello             |

mystr = '           hello'
mystr1 = '           hello          '
mystr2 = 'hello              '
# <10>lstrip
# 删除 mystr 左边的空白字符
print(mystr.lstrip())

# <11>rstrip
# 删除 mystr 字符串末尾的空白字符
print(mystr2.rstrip())

# <12>strip
# 删除mystr字符串两端的空白字符
print(mystr1.strip())

# <13>rfind
#  类似于 find()函数，不过是从右边开始查找.
print(my_str.rfind('itcast'))

# <14>rindex
# 类似于 index()，不过是从右边开始.
print(my_str.rindex('itcast'))

# <15>partition
# 把mystr以str分割成三部分,str前，str和str后
print(my_str.partition('itcast'))  # ('hello world ', 'itcast', ' and itcastcpp')

# <16>rpartition
# 类似于 partition()函数,不过是从右边开始.
print(my_str.rpartition('itcast'))   # ('hello world itcast and ', 'itcast', 'cpp')

# <17>splitlines
# 按照行分隔，返回一个包含各行作为元素的列表
name = '''
123
456
'''
print(name.splitlines())  # ['', '123', '456']

# <18>isalpha
# 如果 mystr 所有字符都是字母 则返回 True,否则返回 False
print(name.isalpha())  # False

# <19>isdigit
# 如果 mystr 只包含数字则返回 True 否则返回 False.
print('123456'.isdigit())  # True
print('123a'.isdigit())   # False

# <20>isalnum
# 如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False
print('123a'.isalnum())   # True

# <21>isspace
# 如果 mystr 中只包含空格，则返回 True，否则返回 False.
print('  '.isspace())  # True