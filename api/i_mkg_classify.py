from api.baseAPI import BaseApi

# 用于实体的关系展示
class EntityQueryApi(BaseApi):
    def __init__(self, name=None):
        self.name = name
        self.result = {}
        self.relation = self.get_relation()

    def get_relation(self):
        with open('micropedia_tree.txt', 'r', encoding='utf-8') as fr:
            data = fr.readlines()
            data = [i.replace('\n', '') for i in data]
        print(data)
        print(len(data))

        relation = {}
        for d in data:
            k, v = d.split(' ')
            # if v not in ['手术', '疾病', '症状', '检查']:
            if not relation.get(k, None):
                print(v)
                relation[k] = [v, ]
            else:
                relation[k].append(v)

        self.relation = relation
        return relation

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
        self.result = self.get_result(self.relation, query)
        return self.result


if __name__ == '__main__':
    obj = EntityQueryApi().push(query='科室')
    print(obj)

