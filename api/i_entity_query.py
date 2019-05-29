from api.baseAPI import BaseApi
from toolkit.models.Neo4j import Neo4j
import re

# 用于实体的关系展示
class EntityQueryApi(BaseApi):
    def __init__(self, name=None):
        self.name = name
        self.result = {}

    def push(self, **kwargs):
        # send data to Invoker
        # in: entity : str
        # out: (1) 如果数据库没有此实体，请返回 {}
        #      (2) 如果有数据，返回格式：
        # self.result = {
        # 'entity': [ {
        #         name: '名称',
        #         des: '详细简略信息，<字数控制在60字左右>',
        #         symbolSize: 60,  # 查询实体大小为60, 其余取30
        #         itemStyle: {
        #             normal: {
        #                 color: 'red'  # 环状颜色填充：相同类型相同颜色，不同类型不同颜色['red','#f5a5c0', 'yellow', '#f4c89e', '#c23531', '#f2acf6', '#acf3f6', 'acf6c9']
        #             }
        #         }
        #     },...],
        # 'relation':
        # [{
        #     source: '蔡成功',    # entity1
        #     target: '欧阳菁',    # entity2
        #     name: "举报"        # 关系名
        # }...]
        # }
        entity = kwargs.get('entity', '')
        color = {'Disease':'red','Department':'#f5a5c0','Drug':'yellow','Check':'#f4c89e','Operation':'#c23531','Pathogenic_Site':'#f2acf6','Symptom':'#acf3f6'}
        #对输入查询数据名称进行正则化
        s = r"[\\\'\"\“\”\‘\’\s\:\、\。\,\.\，\;\·\！\@\#\￥\%\……\&\*\（\）\{\}\【\】\$\/\|\(\)\~\：\；\^\?\？\<\>\《\》\-\+\=\。。。\——]*"
        print('entity：',  entity)
        entity = re.sub(s,'',entity)
        match = Neo4j()
        data = match.matchByName(entity)
        """
        {'n1': (e16ba23:Department {name:"外科"}), 
        'labels(n1)': ['Department'],
         'r': (aa1c2ba) - [: BELONGS_TO{type: "Treatment_of_department"}]->(e16ba23),
         'n2': (aa1c2ba:Disease {
                    detail:"本病是因头部接触高温，电击和化学物质等所造成的头皮及颅骨损伤。可因头部接触的时间、浓度、强度、部位及范围的不同，其损伤的轻重程度也不相同。临床上并不少见，但大宗报道不多。在应用保守治疗及抗生素问世之前，常因组织变性坏死及渗出，引起细菌感染，导致疾病恶化甚而危及生命。近代采用坏死组织切除，后行伤口减张缝合，转移皮瓣及植皮术，同时应用抗菌素治疗，疗效良好沿用至今。由于显微外科技术的进步，现已有人在行坏死组织彻底切除后，应用游离大网膜将其血管与头皮血管施行吻合术，取得了新的进展。", 
                    img:"http://img.39.net/njb/2016/7/28/L/319739.jpg", 
                    info_match:"{'基本知识': {'是否属于医保': '否', '发病部位': '颅脑', '传染性': '无传染性', '多发人群': '所有人', '相关症状': '恶心与呕吐 头痛 组织液渗出 血压下降 组织坏死', '并发疾病': '颅骨缺损 癫痫 瘫痪'}, '诊疗知识': {'就诊科室': '烧伤科 外科', '治疗费用': '市三甲医院约5000-10000元', '治愈率': '60%', '治疗方法': '药物治疗、手术治疗', '相关检查': '头皮检查 体温 全身状态 细菌感染免疫检测', '常用药品': '湿润烧伤膏 长春烫伤膏'}, '去医院必看': {}}", 
                    name:"头皮及颅骨烧伤"}), 
         'labels(n2)': ['Disease']}
        """
        if data:
            relation = []
            #获取相关关系节点的节点名。
            n1 = []
            n2 = []
            for i in range(len(data)):
                di = {}
                dii = {}
                diii = {}
                for j in data[i]['n1']:
                    di[j] = data[i]['n1'][j]
                    di['labels'] = data[i]['labels(n1)'][0]
                for j in data[i]['n2']:
                    dii[j] = data[i]['n2'][j]
                    dii['labels'] = data[i]['labels(n2)'][0]
                n1.append(di)
                n2.append(dii)
                print(data[i]['r'].start_node)
                diii['source'] = data[i]['r'].start_node['name']
                diii['target'] = data[i]['r'].end_node['name']
                diii['name'] = list(set(data[i]['r'].types()))[0]
                relation.append(diii)

            sen = set()
            new_l = []
            n = n1+n2
            for i in n:
                t = tuple(i.items())
                if not t in sen:
                    sen.add(t)
                    new_l.append(i)
            ent = []
            for i in new_l:
                d1 = {}
                d1['name']=i['name']
                if 'detail'in i.keys():
                    d1['des'] = i['detail']
                else:
                    d1['des'] = ''
                if entity == i['name']:
                    d1['symbolSize'] = 60
                else:
                    d1['symbolSize'] = 30
                d1['itemStyle'] = {'normal':{'color':color[i['labels']]}}
                ent.append(d1)
            self.result = {
                'entity':ent,
                'relation':relation
            }
        else:
            self.result = {}
        return self.result

EntityQueryApi().push(entity='感冒')