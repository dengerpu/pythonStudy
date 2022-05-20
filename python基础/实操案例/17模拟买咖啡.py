coffee_name = ('蓝山', '卡布奇诺', '拿铁', '皇家咖啡', '女五咖啡', '美丽与哀愁')
print('你好！欢迎光临小喵咖啡馆')
print('本店经营的咖啡有：')
for index,item in enumerate(coffee_name):
    print(index+1, item)

index = int(input('请输入您喜欢的咖啡编号：'))
if 0<=index<=len(coffee_name):
    print(f'您的咖啡【{coffee_name[index-1]}】好了，请您慢用')