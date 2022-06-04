# 请编写程序，对一段文本（不带符号），统计其中所有不同单词的个数，以及词频最大的前5个词。
#
# 输入格式:
# 输入给出一段非空文本，可以是中文或者英文，词间空格或分行隔开。
#
# 输出格式:
# 输出词的总数和词频最大的前5个词。注意“不区分英文大小写，例如“PAT”和“pat”被认为是同一个词。
#
# 随后按照词频递减的顺序，按照“单词:词频”的格式输出词频最大的前5个词。若有并列，则按递增字典序输出。
#
# 输入样例1:
# 在这里给出一组输入。例如：
#
# This is a test
#  so is considered as the same as long
#
# But this_8 is different than this
# 输出样例1:
# 在这里给出相应的输出。例如：
#
# 14
# is:3
# as:2
# this:2
# a:1
# but:1
# 输入样例2:
# 在这里给出一组输入。例如：
#
# 双儿 洪七公 赵敏 赵敏 逍遥子 鳌拜 殷天正 金轮法王 乔峰 杨过 洪七公 郭靖
#        杨逍 鳌拜 殷天正 段誉 杨逍 慕容复 阿紫 慕容复 郭芙 乔峰 令狐冲 郭芙
#        金轮法王 小龙女 杨过 乔峰 杨逍 乔峰 慕容复
# 输出样例2:
# 在这里给出相应的输出。例如：
#
# 17
# 乔峰:4
# 慕容复:3
# 杨逍:3
# 杨过:2
# 殷天正:2

# stopword = ''
# str = ''
# for line in iter(input, stopword):
#     str += line
# print(str)
words_list = []
while True:
    try:
        words_list += input().strip().split()
    except EOFError:
        break
words_list = [word.lower() for word in words_list]
word_dict = {}
for word in words_list:
    if word not in word_dict:
        word_dict[word] = words_list.count(word)
print(len(word_dict))
sorted(word_dict.items(), key= lambda x: x[1])
count = 0
for key, value in word_dict.items():
    print(f'{key}:{value}')
    count += 1
    if count == 5:
        break