lst = [['1', '电风扇', '美的', 100],
        ['2', '洗衣机', 'TCL', 2500],
        ['3', '微波炉', '老板', 900]
       ]


def show(lst):
    print('编号\t\t名称\t\t\t品牌\t\t单价')
    for item in lst:
        for i in item:
            print(i, end='\t\t')
        print()


show(lst)
print('-'*30)
for item in lst:
    item[0] = '0000'+item[0]
    item[3] = f'￥{item[3]:.2f}'
show(lst)