from api.baseAPI import BaseApi

class EntityQueryApi(BaseApi):
    def __init__(self, name=None):
        self.name = name
        self.result = {}

    def push(self, **kwargs):
        # send data to Invoker
        # in: entity : str
        # out: （1） 如果实体不存在，返回{error:'实体不存在'}
        #       (2)  如果实体存在，返回{name:'', detail:'', info: [{key: value, ....}], info: [{key:value, ...}] , error: ''}
        entity = kwargs.get('entity')

        return self.result