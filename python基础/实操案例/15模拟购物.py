shop_dict = {}
for i in range(5):
    name = input(f'请输入第{i+1}个商品名称：')
    shop_dict[i+1001] = name
print(shop_dict)

cart = []
while True:
    num = input('请输入购买的商品编号：')
    for item, value in shop_dict.items():
        if num == str(item):
            cart.append(value)
            break
    if num == '0':
        break
print(cart)
