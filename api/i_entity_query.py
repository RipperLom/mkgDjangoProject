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
        #self.result = {
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
        entity = kwargs.get('entity')
        color = {'Disease':'red','Department':'#f5a5c0','Drug':'yellow','Check':'#f4c89e','Operation':'#c23531','Pathogenic_Site':'#f2acf6','Symptom':'#acf3f6'}
        #对输入查询数据名称进行正则化
        s = r"[\\\'\"\“\”\‘\’\s\:\、\。\,\.\，\;\·\！\@\#\￥\%\……\&\*\（\）\{\}\【\】\$\/\|\(\)\~\：\；\^\?\？\<\>\《\》\-\+\=\。。。\——]*"
        entity = re.sub(s,'',entity)
        match = Neo4j()
        data = match.matchByName(entity)
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
