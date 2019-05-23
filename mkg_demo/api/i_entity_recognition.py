from mkg_demo.api.baseAPI import BaseApi

class EntityRecognitionApi(BaseApi):
    def __init__(self, name=None):
        self.name = name
        self.result = {}

    def push(self):
        # send data to Invoker
        # in : text: str
        # out : [{'name': str, 'tag': str, 'exist': bool}, ...]
        return self.result