f = open('1.txt', 'r', encoding='utf-8')
while True:
    # buf = f.readline()
    buf = f.read(5)  # 也可以这样一次读取5个字符
    if buf:  # if len(buf)>0 容器，可以直接作为判断条件
        print(buf,end='')
    else:
        break
f.close()

# 1 byte = 8bit
# 1 KB = 1024 byte
# 1 MB = 1024 KB
# 1GB = 1024mb