from api.baseAPI import BaseApi
import thulac, os, csv
from toolkit.models.neo4jModel import Neo4j
class EntityRecognitionApi(BaseApi):
    def __init__(self, name=None):
        self.matchSize = 4  # 拼接的最大范围
        self.name = name
        self.result = {}
        try:
            self.db = Neo4j()  # 预加载neo4j
            self.db.connectDB()
        except:
            self.db = None
            print('api/EntityRecognitionApi/error: 请启动Neo4j服务')
        else:
            pass

    def get_explain(self, s):
        if s == 1:
            return '人物'
        if s == 2:
            return '地点'
        if s == 3:
            return r'机构'
        if s == 4:
            return '政治经济名词'
        if s == 5:
            return '动物学名词'
        if s == 6:
            return '植物学名词'
        if s == 7:
            return '化学名词'
        if s == 8:
            return '季节气候'
        if s == 9:
            return '动植物产品'
        if s == 10:
            return '动植物疾病'
        if s == 11:
            return '自然灾害'
        if s == 12:
            return '营养成分'
        if s == 13:
            return '生物学名词'
        if s == 14:
            return '农机具'
        if s == 15:
            return '农业技术术语'
        if s == 16:
            return '其它实体'

        if s == 21:
            return '科室'
        if s == 22:
            return '疾病'
        if s == 23:
            return '症状'
        if s == 24:
            return '药物'
        if s == 25:
            return '部位'
        if s == 26:
            return '检测项目'
        if s == 27:
            return '手术'

        if s == 'np':
            return '人物'
        if s == 'ns':
            return '地点'
        if s == 'ni':
            return '机构'
        if s == 'nz':
            return '专业名词'
        if s == 'i' or s == 'id':
            return '习语'
        if s == 'j':
            return '简称'
        if s == 'x':
            return '其它'
        if s == 't':
            return '时间日期'

        return '非实体'

    # def get_detail_explain(self, s):
    #     if s == 1:
    #         return '包括人名，职位'
    #     if s == 2:
    #         return '包括地名，区域，行政区等'
    #     if s == 3:
    #         return '包括机构名，会议名，期刊名等'
    #     if s == 4:
    #         return '包括政府政策，政治术语，经济学术语'
    #     if s == 5:
    #         return '包括动物名称，动物类别，动物学相关术语'
    #     if s == 6:
    #         return '包括植物名称，植物类别，植物学相关术语'
    #     if s == 7:
    #         return '包括化肥，农药，杀菌剂，其它化学品，以及一些化学术语'
    #     if s == 8:
    #         return '包括天气气候，季节，节气'
    #     if s == 9:
    #         return '包括肉制品，蔬菜制品，水果制品，豆制品等以动植物为原料的食品，以及一些非食物制品'
    #     if s == 10:
    #         return '包括传染病，原发性疾病，遗传病等'
    #     if s == 11:
    #         return '包括一些大型灾害，环境污染，或其它造成经济损失的自然现象'
    #     if s == 12:
    #         return '包括脂肪，矿物质，维生素，碳水化合物，无机盐等'
    #     if s == 13:
    #         return '包括人体部位，组织器官，基因相关，微生物，以及一些生物学术语'
    #     if s == 14:
    #         return '包括用于农业生产的自动化机械，手工工具'
    #     if s == 15:
    #         return '包括农学名词，农业技术措施'
    #     if s == 16:
    #         return '与农业领域没有特别直接的关系，但是也是实体'
    #
    #     if s == 21:
    #         return '科室'
    #     if s == 22:
    #         return '疾病'
    #     if s == 23:
    #         return '症状'
    #     if s == 24:
    #         return '药物'
    #     if s == 25:
    #         return '部位'
    #     if s == 26:
    #         return '检测项目'
    #     if s == 27:
    #         return '手术'
    #
    #     if s == 'np':
    #         return '包括人名，职位'
    #     if s == 'ns':
    #         return '包括地名，区域，行政区等'
    #     if s == 'ni':
    #         return '包括机构名，会议名，期刊名等'
    #     if s == 'nz':
    #         return ' '
    #     if s == 'i' or s == 'id':
    #         return ' '
    #     if s == 'j':
    #         return ' '
    #     if s == 'x':
    #         return ' '
    #     if s == 't':
    #         return ' '
    #
    #     return '非实体'

    # def preok(self, s):  # 上一个词的词性筛选
    #
    #     if s == 'n' or s == 'np' or s == 'ns' or s == 'ni' or s == 'nz':
    #         return True
    #     if s == 'v' or s == 'a' or s == 'i' or s == 'j' or s == 'x' or s == 'id' or s == 'g' or s == 'u':
    #         return True
    #     if s == 't' or s == 'm':
    #         return True
    #     return False

    def nowok(self, s):  # 当前词的词性筛选

        if s == 'n' or s == 'np' or s == 'ns' or s == 'ni' or s == 'nz':
            return True
        if s == 'a' or s == 'i' or s == 'j' or s == 'x' or s == 'id' or s == 'g' or s == 't':
            return True
        if s == 't' or s == 'm':
            return True
        return False

    # def temporaryok(self, s):  # 一些暂时确定是名词短语的（数据库中可以没有）
    #     if s == 'np' or s == 'ns' or s == 'ni' or s == 'nz':
    #         return True
    #     if s == 'j' or s == 'x' or s == 't':
    #         return True
    #     return False

    def getItem(self, txt, label, gramma):
        item = {}
        item['name'] = txt
        item['tag'] = self.get_explain(label[txt])
        item['grammar'] = gramma
        if label[txt] > 20:
            item['exist'] = True
        else:
            item['exist'] = False
        return item

    def entityExtract(self, text):
        # 拼接查找
        matchSize = self.matchSize # 拼接的最大范围
        thu1 = thulac.thulac()  # 默认模式
        TagList = thu1.cut(text, text=False)
        for i in range(matchSize):
            # 末尾加个不合法的，后面好写
            TagList.append(['===', None])
        # print(TagList)

        # 预加载实体到标注的映射字典
        predict_labels = {}  # 预加载实体到标注的映射字典
        filePath = os.getcwd()
        with open('../data/djangoWashedFiles/predict_labels.txt', 'r', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile, delimiter=' ')
            for row in reader:
                predict_labels[str(row[0])] = int(row[1])

        with open('../data/djangoWashedFiles/totalEntities.txt', 'r', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile, delimiter=' ')
            for row in reader:
                try:
                    predict_labels[str(row[0])] = int(row[1])
                except:
                    print('非法数据：', row)

        label = predict_labels
        # print(label)

        answerList = []
        length = len(TagList) - matchSize  # 扣掉多加的那个
        # print(length)
        i = 0
        while i < length:
            p1 = TagList[i][0]
            t1 = TagList[i][1]
            p12 = p1 + TagList[i + 1][0]
            p123 = p12 + TagList[i + 2][0]
            p1234 = p123 + TagList[i + 3][0]
            p12345 = p1234 + TagList[i + 4][0]

            # 不但需要txt中有实体，还需要判断数据库中有没有
            if not self.db:
                if p12345 in label:  # 组合2个词如果得到实体
                    txt = p12345
                    item = self.getItem(txt, label, t1)
                    answerList.append(item)
                    i += 5
                    continue
            else:
                flag = self.db.matchHudongItembyTitle(p12345)
                if p12345 in label and flag != None:  # 组合2个词如果得到实体
                    txt = p12345
                    item = self.getItem(txt, label, t1)
                    answerList.append(item)
                    i += 5
                    continue

            # 不但需要txt中有实体，还需要判断数据库中有没有
            if not self.db:
                if p1234 in label:  # 组合2个词如果得到实体
                    txt = p1234
                    item = self.getItem(txt, label, t1)
                    answerList.append(item)
                    i += 4
                    continue
            else:
                # 不但需要txt中有实体，还需要判断数据库中有没有
                flag = self.db.matchHudongItembyTitle(p1234)
                if p1234 in label and flag != None:  # 组合2个词如果得到实体
                    txt = p1234
                    item = self.getItem(txt, label, t1)
                    answerList.append(item)
                    i += 4
                    continue

            # 不但需要txt中有实体，还需要判断数据库中有没有
            if not self.db:
                if p123 in label:  # 组合2个词如果得到实体
                    txt = p123
                    item = self.getItem(txt, label, t1)
                    answerList.append(item)
                    i += 3
                    continue
            else:
                # 不但需要txt中有实体，还需要判断数据库中有没有
                flag = self.db.matchHudongItembyTitle(p123)
                if p123 in label and flag != None:  # 组合2个词如果得到实体
                    txt = p123
                    item = self.getItem(txt, label, t1)
                    answerList.append(item)
                    i += 3
                    continue

            # 不但需要txt中有实体，还需要判断数据库中有没有
            if not self.db:
                if p12 in label:  # 组合2个词如果得到实体
                    txt = p12
                    item = self.getItem(txt, label, t1)
                    answerList.append(item)
                    i += 2
                    continue
            else:
                # 不但需要txt中有实体，还需要判断数据库中有没有
                flag = self.db.matchHudongItembyTitle(p12)
                if p12 in label and flag != None:  # 组合2个词如果得到实体
                    txt = p12
                    item = self.getItem(txt, label, t1)
                    answerList.append(item)
                    i += 2
                    continue

            # 不但需要txt中有实体，还需要判断数据库中有没有
            if not self.db:
                if p1 in label:  # 当前词如果是实体
                    txt = p1
                    item = self.getItem(txt, label, t1)
                    answerList.append(item)
                    i += 1
                    continue
            else:
                # 不但需要txt中有实体，还需要判断数据库中有没有
                flag = self.db.matchHudongItembyTitle(p1)
                if p1 in label and flag != None and self.nowok(t1):  # 当前词如果是实体
                    txt = p1
                    item = self.getItem(txt, label, t1)
                    answerList.append(item)
                    i += 1
                    continue

            # if temporaryok(t1):
            #     txt = p1
            #     item['name'] = txt
            #     item['tag'] = get_explain(label[txt])
            #     item['exist'] = True
            #     answerList.append(item)
            #     i += 1
            #     continue

            item = {}
            item['name'] = p1
            item['tag'] = self.get_explain(t1)
            item['grammar'] = t1
            item['exist'] = False
            answerList.append(item)
            i += 1
        return answerList

    def push(self, **kwargs):
        # send data to Invoker
        # in : text: str
        # out : [{'name': str, 'tag': str, 'exist': bool}, ...]
        text = kwargs['text']
        self.result = self.entityExtract(text)
        return self.result

if __name__ == "__main__":
    text = '我觉的腹部不舒服，我想去风湿科，不知道是不是得的弗郎西丝菌肺炎'

    # text = "[{'name': str, 'tag': str, 'grammar': '', 'exist': bool}, ...]"

    # thu1 = thulac.thulac()  # 默认模式
    # TagList = thu1.cut(text, text=False)
    # print(TagList)

    # entityRecognitionApi = EntityRecognitionApi()
    # answerList = entityRecognitionApi.push(text=text)
    # for i in answerList:
    #     print(i)

    with open('../data/djangoWashedFiles/grammar_list', 'r', encoding="utf-8") as csvfile:
        line = csvfile.readline()[:-1]
        grammars = line.split(' ')
        for grammar in grammars:
            key, value = grammar.split('/')
            print(key, value)
