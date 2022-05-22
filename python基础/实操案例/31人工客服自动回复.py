def find_question(question):
    with open('replay.txt', 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:  # if line == '' 文件末尾退出
                break
            keyword = line.split('|')[0]
            reply = line.split('|')[1]
            if keyword in question:
                return reply
        return False


while True:
    question = input('Hi,您好，小蜜在此等主人很久了，有什么烦恼快和小蜜说吧')
    if question == 'bye':
        break
    reply = find_question(question)
    if not reply:
        question = input('小蜜不知道你在说什么，您可以问一些关于订单、物流、账户、支付等问题，退出请输入bye')
    else:
        print(reply)
print('小主再见')


