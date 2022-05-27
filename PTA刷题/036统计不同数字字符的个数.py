# 输入只包含数字字符的字符串，统计串中不同字符的出现次数。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。对于每组测试，输入一个字符串（不超过80个字符）。
#
# 输出格式:
# 对于每组测试，按字符串中出现字符的ASCII码升序逐个输出不同的字符及其个数（两者之间留一个空格），每组输出之后空一行，输出格式参照输出样例。
#
# 输入样例:
# 12123
# 输出样例:
# 1 2
# 2 2
# 3 1
# str = input()
# my_dict = {}
# for i in str:
#     if i not in my_dict:
#         my_dict[i] = str.count(i)
# for k in sorted(my_dict):
#     print(k, my_dict[k])
# for i in range(len(my_dict)):
#     print()

lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
while True:
    st = input()
    if st.strip() == '':
        break
    for i in lst:
        if st.count(i) == 0:
            continue
        else:
            print("%c %d" % (i,st.count(i)))
    print()

