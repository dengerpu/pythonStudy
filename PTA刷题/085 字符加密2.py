# 字符加密：大小写字母加密规则如下表，其它字符加密前后不变。
#
# # 加密前: a b c d e f lg h i j k 1 m n o p la r s t u v w x ly z
# # 加密后:B |c D |E |F lc H I JKL M N |o P Q R
# # 加密前:A B c D E FG H I J
# # lo P lo |R ls T u lv lw x ly z
# # 加密后:b lc ld le f lg h i lj l
#
#
# 输入格式:
# 输入一行想加密的字符串。
#
# 输出格式:
# 输出加密后的字符串。
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# Zero zero seven!
# 输出样例:
# 在这里给出相应的输出。例如：
#
# aFSP AFSP TFWFO!
word = input()
encypt = ''
for i in word:
    if 97 <= ord(i) < 97+25:
        encypt += chr(ord(i)-31)
    elif i == 'z':
        encypt += 'A'
    elif 65 <= ord(i) < 65+25:
        encypt += chr(ord(i)+33)
    elif i == 'Z':
        encypt += 'a'
    else:
        encypt += i
print(encypt)