from mkg_demo.api.baseAPI import BaseApi

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
        entity1 = kwargs.get('entity1', '')
        entity2 = kwargs.get('entity2', '')
        relation = kwargs.get('relation', '')

        return self.result