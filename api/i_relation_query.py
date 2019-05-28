from api.baseAPI import BaseApi
from toolkit.models.Neo4j import Neo4j
from api.i_entity_query import EntityQueryApi
import re

class RelationQueryApi(BaseApi):
    def __init__(self, name=None):
        self.name = name
        self.result = {}

    def push(self, **kwargs):
        # send data to Invoker
        # in : entity1: str, entity2: str, relation: str
        # out: (1) 如果数据库没有此实体，请返回 {}
        #      (2) 如果有数据，返回格式：
        # self.result = {
        # 'entity': [ {
        #         name: '名称',
        #         des: '详细简略信息，<字数控制在60字左右>',
        #         symbolSize: 60,  # 查询实体大小为60, 其余取30
        #         itemStyle: {
        #             normal: {
        #                 color: 'red'  # 环状颜色填充：相同类型相同颜色，不同类型不同颜色['#f5a5c0', 'yellow', '#f4c89e', '#c23531', '#f2acf6', '#acf3f6', 'acf6c9']
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
        entity1 = kwargs.get('entity1','')
        entity2 = kwargs.get('entity2','')
        relation = kwargs.get('relation','')
        color = {'Disease': 'red', 'Department': '#f5a5c0', 'Drug': 'yellow', 'Check': '#f4c89e',
                 'Operation': '#c23531', 'Pathogenic_Site': '#f2acf6', 'Symptom': '#acf3f6'}
        s = r"[\\\'\"\“\”\‘\’\s\:\、\。\,\.\，\;\·\！\@\#\￥\%\……\&\*\（\）\{\}\【\】\$\/\|\(\)\~\：\；\^\?\？\<\>\《\》\-\+\=\。。。\——]*"
        if (entity1 or entity2) and relation:
            if entity1 and entity2:
                # 对输入查询数据名称进行正则化
                entity1 = re.sub(s, '', entity1)
                entity2 = re.sub(s, '', entity2)
                match = Neo4j()
                data = match.findRelationByEntityAndRelation(entity1=entity1,entity2=entity2,relation=relation)
                if data:
                    relation = []
                    # 获取相关关系节点的节点名。
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
                    n = n1 + n2
                    for i in n:
                        t = tuple(i.items())
                        if not t in sen:
                            sen.add(t)
                            new_l.append(i)
                    ent = []
                    for i in new_l:
                        d1 = {}
                        d1['name'] = i['name']
                        if 'detail' in i.keys():
                            d1['des'] = i['detail']
                        else:
                            d1['des'] = ''
                        if entity1 == i['name']:
                            d1['symbolSize'] = 60
                        else:
                            d1['symbolSize'] = 30
                        d1['itemStyle'] = {'normal': {'color': color[i['labels']]}}
                        ent.append(d1)
                    self.result = {
                        'entity': ent,
                        'relation': relation
                    }
                else:
                    self.result = {}
            elif entity1:
                entity1 = re.sub(s, '', entity1)
                print(55555)

            else:
                entity2 = re.sub(s, '', entity2)
                print(66666)


        elif entity1 and entity2:
            entity1 = re.sub(s, '', entity1)
            entity2 = re.sub(s, '', entity2)
            match = Neo4j()
            data = match.findRelationByEntity(entity1=entity1,entity2=entity2)
            if data:
                relation = []
                # 获取相关关系节点的节点名。
                n1 = []
                n2 = []
                for i in range(len(data)):
                    di = {}
                    dii = {}
                    diii = {}
                    for j in data[i]['n1']:
                        di[j] = data[i]['n1'][j]
                        di['labels'] = list(data[i]['n1'].labels)[0]

                    for j in data[i]['n2']:
                        dii[j] = data[i]['n2'][j]
                        dii['labels'] = list(data[i]['n2'].labels)[0]

                    diii['source'] = data[i]['n1']['name']
                    diii['target'] = data[i]['n2']['name']
                    diii['name'] = data[i]['rel']

                    n1.append(di)
                    n2.append(dii)
                    relation.append(diii)

                sen = set()
                new_l = []
                n = n1 + n2
                for i in n:
                    t = tuple(i.items())
                    if not t in sen:
                        sen.add(t)
                        new_l.append(i)
                ent = []
                for i in new_l:
                    d1 = {}
                    d1['name'] = i['name']
                    if 'detail' in i.keys():
                        d1['des'] = i['detail']
                    else:
                        d1['des'] = ''
                    if entity1 == i['name']:
                        d1['symbolSize'] = 60
                    else:
                        d1['symbolSize'] = 30
                    d1['itemStyle'] = {'normal': {'color': color[i['labels']]}}
                    ent.append(d1)
                self.result = {
                    'entity': ent,
                    'relation': relation
                }
            else:
                self.result = {}
        elif entity1:
            ent = EntityQueryApi()
            self.result = ent.push(entity=entity1)
        elif entity2:
            ent = EntityQueryApi()
            self.result = ent.push(entity=entity2)
        else:
            self.result = {}
        return self.result
r = RelationQueryApi()
b = r.push(entity1='易性病',entity2='青春期强迫症',relation='')
print(b)