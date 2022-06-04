# 本题要求你计算A-B。不过麻烦的是，A和B都是字符串 —— 即从字符串A中把字符串B所包含的字符全删掉，剩下的字符组成的就是字符串A-B。
#
# 输入格式:
# 输入在2行中先后给出字符串A和B。每个字符串都是由可见的ASCII码组成，最后以换行符结束。
#
# 输出格式:
# 在一行中打印出A-B的结果字符串。
#
# 输入样例1:
# 在这里给出一组输入。例如：
#
# I love Python!  It's a fun game!
# aeiou
# 输出样例1:
# 在这里给出相应的输出。例如：
#
# I lv Pythn!  It's  fn gm!
# 输入样例2:
# 在这里给出一组输入。例如：
#
# good
# aeiougd
# 输出样例2:
# 在这里给出相应的输出。例如：
#
#

strA = list(input())
strB = list(input())

for item in strB:
    while item in strA:
        strA.remove(item)
print(''.join(strA))
