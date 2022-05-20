scoress = [
    {'name': '广州恒大', 'score': 72},
    {'name': '北京国安', 'score': 70},
    {'name': '上海上港', 'score': 76},
    {'name': '江苏江宁', 'score':53} ]


def show(scoress):
    for index, item in enumerate(scoress):
        print(index+1, end=' ')
        for score in item.values():
            print(score, end=' ')
        print()


print('-'*30)
scoress.sort(key=lambda x: x['score'],reverse= True)
show(scoress)