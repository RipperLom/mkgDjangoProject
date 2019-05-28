
中关村图谱设计中心-医疗知识图谱项目

#  API接口调用
###测试：
1、实体识别

API  参数： text
http://127.0.0.1:8000/entity_recognition/?text=病名&api=true
输出格式：[{'name': str, 'tag': str, 'exist': bool}, ...]

2、实体查询

API请求格式：entity   api=true
http://127.0.0.1:8000/entity_query/?api=true&entity=感冒
输出格式：

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

3、关系查询

API, 请求参数： entity1, entity2, relation, api=true
http://127.0.0.1:8000/entity_query/?api=true&entity1=实体一&entity2=实体二&relation=关系名
输出格式：

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

4、详细信息查询

API: 参数： entity, api=true
http://127.0.0.1:8000/detail/?entity=实体名&api=true
输出格式：

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
