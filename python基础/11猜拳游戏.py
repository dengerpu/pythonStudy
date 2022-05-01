import random

while True:
    user = int(input('请输入：1（拳头），2（剪刀），3（布）:'))
    if user == 1:
        print("玩家：拳头")
    elif user == 2:
        print("玩家：剪刀")
    elif user == 3:
        print("玩家：布")
    else:
        print("输入有误，请重新输入")
    # 电脑随机出
    if user == 1 or user == 2 or user == 3:
        computer = random.randint(1, 3)  # 随机产生1-3之间的随机数
        if computer == 1:
            print("电脑：拳头")
        elif computer == 2:
            print("电脑：剪刀")
        elif computer == 3:
            print("电脑：布")
        if user == computer:
            print('平局')
        elif (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
            print("玩家赢")
        else:
            print("电脑赢")
