n = int(input('请输入行数:'))
i = 0
for i in range(n):
    j = 0
    for j in range(n):
        print('*', end=' ')
    print()
print('--------------')
n = int(input('请输入行数:'))
i = 0
while i < n:
    j = 0
    while j < n:
        print('*',end=' ')
        j += 1
    i += 1
    print('')
