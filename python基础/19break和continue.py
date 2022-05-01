# break和continue是python的两个关键词
# break和python都用在循环中
# break是终止循环的执行，即循环代码遇到break,就不再循环了
# continue是结束本次循环，继续下一次循环，即本次循环剩下的代码就不会再进行，但会进行下一次循环
my_str = 'hello python!'

for i in my_str:
    if i == 'p':
        print('包含p这个字符')
        break
else:   # 不被break终止，才会被执行
    print('找不到')

# for x in xx:
#     if xxx:
#         xx # if判断条件成立会执行
#     else:
#         xx  # if判断条件不成立执行
# else:
#     xxx # for循环代码结束，但不是被break终止的时候会执行