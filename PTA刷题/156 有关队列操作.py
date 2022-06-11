# 请实现一个MyQueue类，实现出队，入队，显示队列，求队列长度。
#
# 实现入队方法 push(int x); 实现出队方法 pop(); 实现求队列长度方法 size();实现显示队列方法：show() 。
#
# 输入格式:
# 每个输入包含1个测试用例。
#
# 每个测试用例第一行给出一个正整数 n (n <= 10^6) ，接下去n行每行一个数字，表示一种操作： 1 x ： 表示从队尾插入x，0<=x<=2^31-1。 2 ： 表示队首元素出队。 3 ： 表示求队列长度。4：表示显示队列中所有元素。
#
# 输出格式:
# 对于操作1，将要添加的元素添加到队列的尾部
#
# 对于操作2，若队列为空，则输出 “Invalid”,否则请输出队首元素，并将这个元素从队列中删除。
#
# 对于操作3，请输出队列长度。 每个输出项最后换行。
#
# 对于操作4，输出队列中每个元素，元素之间用空格分隔，最后一个元素后面没有空格。
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 9
# 1 23
# 1 34
# 3
# 4
# 2
# 1 56
# 2
# 3
# 1 90
# 输出样例:
# 在这里给出相应的输出。例如：
#
# 2
# 23 34
# 23
# 34
# 1
lst = []


class MyQueue(object):

    def push(self, x):  # 入队
        lst.append(x)

    @staticmethod
    def pop():  # 出队
        if len(lst) == 0:
            print('Invalid')
        else:
            print(lst.pop(0))

    @staticmethod
    def size():  # 求队列长度
        print(len(lst))

    @staticmethod
    def show():
        for i in range(len(lst)):
            if i != len(lst) - 1:
                print(lst[i], end=' ')
            else:
                print(lst[i])


queue = MyQueue()
n = int(input())
for i in range(n):
    value = list(map(int, input().split()))
    option = 0
    x = 0
    if len(value) == 1:
        option = value[0]
    elif len(value) == 2:
        x = value[1]
        option = value[0]
    if option == 1:
        queue.push(x)
    elif option == 2:
        queue.pop()
    elif option == 3:
        queue.size()
    elif option == 4:
        queue.show()


