from api.baseAPI import BaseApi
from django.conf import settings

# 用于实体的关系展示
class ClassifyApi(BaseApi):
    def __init__(self, name=None):
        self.name = name
        self.result = {}
        self.relation = settings.RELATION

    def get_result(self, relation, currentnode):
        nodes_text = relation.get(currentnode.get('text'))
        if nodes_text:
            for node in nodes_text:
                if not currentnode.get('nodes'):
                    currentnode['nodes'] = []
                currentnode['nodes'].append(self.get_result(relation, {'text': node}))
        else:
            currentnode['nodes'] = []
        return currentnode

    def push(self, **kwargs):
        # send data to Invoker
        # in: query : str
        # out: []
        query = kwargs.get('query', '')
        if not query:
            query = '科室'
        query = {'text': query}
        self.result = self.get_result(self.relation, query)
        print('结果为：', self.result)
        return self.result


if __name__ == '__main__':
    # obj = EntityQueryApi().push(query='科室')
    # print(obj)
    pass
