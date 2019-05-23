class BaseApi(object):
    def __init__(self, name=None):
        self.name = name
        self.result = {}

    def push(self):
        # send data to Invoker
        return self.result