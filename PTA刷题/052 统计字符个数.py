# 输入若干的字符串，每个字符串中只包含数字字符和大小写英文字母，统计字符串中有出现的不同字符的出现次数。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试输入一个字符串（不超过80个字符）。
#
# 输出格式:
# 对于每组测试，按字符串中有出现的字符的ASCII码升序逐行输出不同的字符及其个数（两个数据之间留一个空格），每两组测试数据之间留一空行，输出格式参照输出样例。
#
# 输入样例:
# 12123
# A1c1B
# 输出样例:
# 1 2
# 2 2
# 3 1
#
# 1 2
# A 1
# B 1
# c 1
try:
    flag = 0
    while True:
        str_list = list(input())
        str_list.sort()
        if flag:
            print()  # 用于控制两组数据之间一个空格
        my_dict = {}
        for item in str_list:
            my_dict[item] = str_list.count(item)
        for key,value in my_dict.items():
            print(key, value)
        flag = 1
except EOFError:
    pass
