# 使用递归求1-100累加和
def add(num):
    if num == 1:
        return 1
    else:
        return add(num-1)+num;


print(add(100))

# 编程实现向文件a.txt中书写`好好学习，天天向上`的内容。
f = open('a.txt', 'w', encoding='utf-8')
f.write('好好学习，天天向上')
f.close()

f = open('a.txt', 'r',encoding='utf-8')
buf = f.read()
print(buf)
f.close()
