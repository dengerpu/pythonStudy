import prettytable as pt

# 显示坐席
def show_ticket(row_num):
    tb = pt.PrettyTable()
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(row_num):
        lst = [f'第{i+1}行', '有票', '有票', '有票', '有票', '有票']
        tb.add_row(lst)
    print(tb)


def order_ticket(row_num, row, column):
    tb = pt.PrettyTable()
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(row_num):
        if int(row) == i+1:
            lst = [f'第{i+1}行', '有票', '有票', '有票', '有票', '有票']
            lst[int(column)] = '已售'
            tb.add_row(lst)
        else:
            lst = [f'第{i + 1}行', '有票', '有票', '有票', '有票', '有票']
            tb.add_row(lst)
    print(tb)


row_num = 13
show_ticket(row_num)
choose = input('请输入要选择的座位，例如13,5\n')
try:
    row,column = choose.split(',')
    order_ticket(row_num, row, column)
except:
    print('输入有误')