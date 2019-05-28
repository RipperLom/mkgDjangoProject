from api.baseAPI import BaseApi
from toolkit.models.Neo4j import Neo4j
import re
import json
# 用于实体的详细介绍
class EntityDetailyApi(BaseApi):
    def __init__(self, name=None):
        self.name = name
        self.result = {}

    def push(self, **kwargs):
        # send data to Invoker
        # in: entity : str
        # out: （1） 如果实体不存在，返回{error:'实体不存在'}
        #       (2)  如果实体存在，返回
        # {
        # name: '',
        # detail: '',
        #  url: '',
        #  'little_propreties:' {'key':{'key': 'content'},...},
        #  large_propreties: {'key':{'key': 'content'},...} ,
        # 'type': '',
        # 'relation_name', ['','',...],
        #  error: ''
        # }
        #对输入查询数据名称进行正则化
        entity = kwargs.get('entity', [''])[0]
        s = r"[\\\'\"\“\”\‘\’\s\:\、\。\,\.\，\;\·\！\@\#\￥\%\……\&\*\（\）\{\}\【\】\$\/\|\(\)\~\：\；\^\?\？\<\>\《\》\-\+\=\。。。\——]*"
        entity = re.sub(s,'',entity)
        match = Neo4j()
        data = match.matchByName(entity)
        #判断数据是否存在
        if data:
            L = []
            for j in range(len(data)):
                di = {}
                for i in data[j]['n1']:
                    di[i] = data[j]['n1'][i]
                L.append(di)

            sen = set()
            new_l = []
            for i in L:
                t = tuple(i.items())
                if not t in sen:
                    sen.add(t)
                    new_l.append(i)
            if len(new_l) > 1:
                max_index = 0
                max_len = len(new_l[0])
                for i in range(len(new_l)):
                    if len(new_l[i]) >= max_len:
                        max_len = len(new_l[i])
                        max_index = i
                dI = new_l[max_index]
            else:
                dI = new_l[0]
            if 'info_match' in dI.keys():
                info_match_str = str.replace(dI['info_match'], "'", '"')
                info_match_dict = json.loads(info_match_str)
                # 删除'info_match'字典中值为空的键值对
                for key in list(info_match_dict.keys()):
                    if not info_match_dict.get(key):
                        info_match_dict.pop(key)
            else:
                info_match_dict = ''

            #获取相关关系节点的节点名。
            rel_na = []
            for i in range(len(data)):
                dii={}
                for j in data[i]['n2']:
                    dii[j] = data[i]['n2'][j]
                rel_na.append(dii['name'])

            if 'detail' in dI.keys():
                detail = dI['detail']
            else:
                detail = ''
            if 'img' in dI.keys():
                img = dI['img']
            else:
                img = ''

            #按照格式返回数据
            self.result = {
                'name':dI['name'],
                'detail':detail,
                'url':img,
                'little_propreties':info_match_dict,
                'type': data[0]['labels(n1)'][0],
                'relation_name':rel_na,
                'error':''
            }
        else:
            self.result = {
                'name':'',
                'detail':'',
                'url':'',
                'little_propreties':'',
                'type': '',
                'error':'实体不存在！！！',
            }
        return self.result
a = EntityDetailyApi()
b = a.push(entity=['口炎'])
print(b)