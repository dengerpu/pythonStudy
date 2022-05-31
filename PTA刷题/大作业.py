import vcf

def get_groupA(): # 获取ga中的材料，以列表形式返回
    recordA = []
    file = open("ga.lib")
    while True:
        line = file.readline();
        if not line:
            break
        recordA.append(line[0:-1])
    return recordA

def get_groupB(): #获取gb中的材料，以列表形式返回
    recordB = []
    file = open("gb.lib")
    while True:
        line = file.readline();
        if not  line:
            break
        recordB.append(line[0:-1])
    return recordB

    # 初始化 group_list 保存每段基因片段相似度，start是片段的开始位置，end是片段的结束位置，eachAVG用来保存每个特定材料在该片段上的平均相似度
def get_group_list():
    group_list = {'start': 0, 'end': 0, 'eachAVG': {}}
    vcf_reader = vcf.Reader(open('h1000.vcf', 'r'))
    for record in vcf_reader:
        for i in record:  # 初始化eachAVG
            group_list['eachAVG'].setdefault(i.sample, 0)
        break
    return group_list

def get_answer_list():

    vcf_reader = vcf.Reader(open('h1000.vcf', 'r'))

    count_record = 0    #记录执行的条数
    group_list = {}
    answer_list = []    #用来存放每一段geuop_list
    for record in vcf_reader:
        # if count_record == 20: #小量数据测试用
        #     break
        count_record += 1
        print(count_record) # 程序执行时间长，这里可以反馈执行进度
        if count_record % 100 == 1: # 100 是控制片段的长度
            group_list = get_group_list()
            group_list['start'] = record.POS

        # 计算相似度
        one_in_b = 0
        zero_in_b = 0
        for i in record:
            if i.sample in get_groupB():
                if i['GT'] == '0/1':
                    zero_in_b += 1
                    one_in_b += 1
                elif i['GT'] == '1/1':
                    one_in_b += 2
                elif i['GT'] == '0/0':
                    zero_in_b += 2
        similar_rate = one_in_b/(one_in_b+zero_in_b) # 每一条记录的相似度
        # print(1)
        # 计算每条记录每个样本的相似值 再 加和 ，每一百条再做一次平均值处理
        if count_record == 1:
            for i in record:
                if i.sample in get_groupA():
                    if i['GT'] == '0/1':
                        group_list['eachAVG'][i.sample] = similar_rate/2
                    elif i['GT'] == '1/1':
                        group_list['eachAVG'][i.sample] = similar_rate
                    elif i['GT'] == '0/0':
                        group_list['eachAVG'][i.sample] = 0
        else:
            for i in record:
                if i.sample in get_groupA():
                    if i['GT'] == '0/1':
                        group_list['eachAVG'][i.sample] = similar_rate/2 + group_list['eachAVG'][i.sample]
                    elif i['GT'] == '1/1':
                        group_list['eachAVG'][i.sample] = similar_rate + group_list['eachAVG'][i.sample]
                    elif i['GT'] == '0/0':
                        group_list['eachAVG'][i.sample] = 0 + group_list['eachAVG'][i.sample]


        # print(1)

        if count_record % 100 == 0:
            group_list['end'] = record.POS  #第100的倍数条记录时写入写入某段基于的结束位置
            for i in record:
                group_list['eachAVG'][i.sample] /= 100  #计算100长度的片段的每个材料的相似度平均值
            answer_list.append(group_list)   #将处理好的一段基因的数据存到列表answer_list种，方便使用
    return answer_list

    # print(answer_list)
if __name__ == '__main__':
    #在answer_list中检索答案
    for i in get_groupA():
        for j in get_answer_list():
            if i in j['eachAVG'] and j['eachAVG'][i] > 0.2:
                print(i + " " + str(j['start']) + " " + str(j['end']) + " " + str(j['eachAVG'][i]))
