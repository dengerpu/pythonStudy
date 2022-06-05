# 输入一个列表，删除其中的重复值，再输出。
#
# 要求
# 假设列表中存在k个值为a的元素，删除前k-1个元素，保留最后一个。
# 不同元素在列表中的相对位置不应被改变。
#
# 输入格式:
# [元素1， 元素2, ... , 元素n]
#
# 输出格式:
# [元素1，元素2, ... , 元素k]
#
# 输入样例:
# [4,3,2,3,2,4,True]
# 输出样例:
# [3, 2, 4, True]
# 提示：将形如"[1,3,5]"的字符串转换成列表可以使用eval()函数。
#
# 注意：不要在遍历列表的同时对列表进行增删改操作，这样会引起混乱，导致不正确的结果！
#
# 注意，输出格式应与输出样例一致，涉及空格，逗号等。
#
#
# 请接着往下看：你的程序真的对了吗？
# 多数读者的解题思路是制造一个v列表的复制品以避免在遍历v的同时删除v中的元素。该解决方案可以通过本题设置的全部测试。但这并不意味着该解决方案是“完全正确”的。请尝试下述输入：
#
# [1,7,6,7,7,True,'a',9.8,'a',True]
#
# 很遗憾，程序将产生错误的输出：
# [6, 7, 9.8, 'a', True]
# 产生这种意外结果的原因是：在Python里1和True是相等的！ 0和False也是相等的！ 在使用列表的count()函数，index()函数，remove()函数时，1和True, 0和False被不加区分地对待。
#
# 下述代码的执行结果证实了这一点：
#
# v = [1,True,2,True,0,False]
# print("count of 1:", v.count(1), ",count of True:", v.count(True))
# print("count of 0:", v.count(0), ",count of False:", v.count(False))
# print("index of True:",v.index(True), ",index of False",v.index(False))
# v.remove(True)
# print("after v.remove(True):",v)
# 其执行结果为：
#
# count of 1: 3 ,count of True: 3     #1,True都同时为1或True
# count of 0: 2 ,count of False: 2    #0,False都同时为0或False
# index of True: 0 ,index of False 4  #下标0的1被视为True
# after v.remove(True): [True, 2, True, 0, False]   #1被当作True移除了
# lst = eval(input())
# my_list = [x for x in lst]  # 不能直接赋值，来复制列表，因为他们的内存地址是相同的
# for i in lst:
#     while my_list.count(i) > 1:
#         my_list.remove(i)
# print(my_list)
list1 = eval(input())
list1.reverse()
list2 = ['']
for i in list1:
    if i not in list2:
        list2.insert(0, i)
list2.pop()
print(list2)
