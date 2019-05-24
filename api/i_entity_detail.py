from api.baseAPI import BaseApi

# 用于实体的详细介绍
class EntityDetailyApi(BaseApi):
    def __init__(self, name=None):
        self.name = name
        self.result = {}

    def push(self, **kwargs):
        # send data to Invoker
        # in: entity : str
        # out: （1） 如果实体不存在，返回{error:'实体不存在'}
        #       (2)  如果实体存在，返回{name: '', detail: '', little_propreties: ['key':{'key': 'content'},...], large_propreties: ['key':{'key': 'content'},...] , error: ''}
        entity = kwargs.get('entity')

        return self.result