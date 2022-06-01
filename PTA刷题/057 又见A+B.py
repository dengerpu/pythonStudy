# 某天，诺诺在做两个10以内（包含10）的加法运算时，感觉太简单。于是她想增加一点难度，同时也巩固一下英文（学好英文真的很重要！），就把数字用英文单词表示。为了验证她的答案，请根据给出的两个英文单词表示的数字，计算它们之和并以英文单词的形式输出。如果没记住这些数字的英文单词，那就先好好学学英文吧。
#
# 输入格式:
# 多组测试数据，处理到文件尾。每组测试输入两个英文单词表示的数字A、B（0≤A，B≤10）。
#
# 输出格式:
# 对于每组测试，在一行上输出A+B的结果，要求以英文单词表示。
#
# 输入样例:
# ten ten
# one two
# 输出样例:
# twenty
# three

number_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
               'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
               'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20,
               }
try:
    while True:
        a, b = input().split()
        result = number_dict[a] + number_dict[b]
        for key, value in number_dict.items():
            if value == result:
                print(key)
except EOFError:
    pass
