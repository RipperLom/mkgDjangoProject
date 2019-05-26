import neo4j
from py2neo import Graph, Node, Relationship, cypher,Path
#创建Neo4j类
class Neo4j():
    graph = None
    #初始化类，连接Neo4j数据库，保证数据库已启动
    def __init__(self):
        print('create neo4j class ...')
        self.graph = Graph("http://localhost:7474", username="neo4j", password="123456")

    #依据病名去查找实体，返回的是一个列表，列表中有字典，字典中有节点，数据提取如下：
    '''
    例：
    ss = model.matchDiseaseByName('糖尿病')
    print(ss)       [{'n': (c7d06cd:Disease {cost:"市三甲医院约1000-3000元",cure_rate:"药物可控制，不易根治",infectivity:"无传染性",medical_insurance:"是",name:"糖尿病",online_to_buy_medicine:"健客大药房康德乐大药房阿康大药房",therapy:"药物治疗、饮食疗法、运动治...",throng:"四十岁以上的中年人",treatment_cycle:">120天(需要终身治疗)"})}]
    print(ss[0]['n']['cost'])      市三甲医院约1000-3000元
    print(type(ss[0]['n']['cost']))    <class 'str'>
    '''
    def matchDiseaseByName(self,value):
        sql = "MATCH (n:Disease { name: '" + str(value) + "' })-[ra]-(na)-[rb]->(nb) return n,ra,na,rb,nb;"
        answer = self.graph.run(sql).data()
        return answer

    #查找疾病及其对应的关系
    def findRelationByEntity(self,entity1, entity2):
        sql = "match (n{name:'"+entity1+"'})-[r]-(m{name:'"+entity2+"'}) return r"
        answer = self.graph.run(sql).data()
        return answer

    #查找指定的实体和关系
    def findRelationByEntityAndRelation(self,entity1, entity2,relation):
        sql = "match (n{name:'" + entity1 + "'})-[r:"+relation+"]-(m{name:'" + entity2 + "'}) return r"
        answer = self.graph.run(sql).data()
        return answer
    #添加节点到graph中
    def createNode(self,filename,labelname):
        with open(filename, 'r', encoding='utf-8') as fr:
            msg = fr.readlines()
            propotynamelist = msg[0].strip().split(',')
            if len(propotynamelist)==1:
                # print(len(msg))
                for i in range(1, len(msg)):
                    sql = 'MERGE(p: '+labelname+'{name:"'+msg[i].strip().replace('\\','').replace('"','')+'"})'
                    # print(sql)
                    self.graph.run(sql)
                    print(labelname+'导入完成比例：{:.2f}%'.format((i / len(msg))*100))
            else:
                for i in range(1, len(msg)):
                    onemesg = msg[i].strip().split(',')
                    sql ="MERGE(p: "+labelname+"{"
                    onemesglist = []
                    if len(propotynamelist)==len(onemesg):
                       onemesglist = onemesg
                    else:
                        interim = msg[i].strip().split('"')
                        onemesglist=interim[0].split(',')[:-1] + [interim[1]] + interim[2].split(',')[1:]
                    for j in range(len(onemesglist)):
                        sql += propotynamelist[j]+':"'+onemesglist[j].strip().replace('\\','').replace('"','')+'",'
                    sql = sql[:-1]+"})"
                # print(sql)
                    self.graph.run(sql)
                    print(labelname+'导入完成比例：{:.2f}%'.format(((i+1) / len(msg)) * 100))
        self.graph.run('CREATE CONSTRAINT ON (c:'+labelname+') ASSERT c.name IS UNIQUE')
                # CREATE(p: Disease
                # {name: line.name, medical_insurance: line.medical_insurance, infectivity: line.infectivity,
                #  therapy: line.therapy, cure_rate: line.cure_rate, treatment_cycle: line.treatment_cycle,
                #  throng: line.throng, cost: line.cost, online_to_buy_medicine: line.online_to_buy_medicine})
    def createRelation(self,filename,entity1label,entity2label,relationname):
        with open(filename, 'r', encoding='utf-8') as fr:
            msg = fr.readlines()
            for i in range(1, len(msg)):
                onemesg = msg[i].strip().split(',')
                sql ='MATCH (n:'+entity1label+'{name:"'+onemesg[0]+'"}),(m:'+entity2label+'{name:"'+onemesg[2].strip().replace('\\','').replace('"','')+'"}) CREATE (n)-[r:'+relationname+'{type:"'+onemesg[1]+'"}]->(m) RETURN r'
                self.graph.run(sql)
                print(relationname + '导入完成比例：{:.2f}%'.format((i / len(msg)) * 100))
            # MATCH(entity1: Disease
            # {name: line.illness_name}), (entity2:Symptom{name:line.symptom_name})
            # CREATE(entity1) - [r: HAS_SYMPTOM
            # {type: line.classical_symptom}]->(entity2)
            # RETURN r


if __name__ == '__main__':
    model = Neo4j()
    # print(len(model.matchDiseaseByName('桃花病')))
    # for i in model.matchDiseaseByName('桃花病'):
    #     print(i)
    # print(model.findRelationByEntity('现代病','心理咨询'))
    # print(model.findRelationByEntity('血压测量','老年人高血压'))
        # print(str(model.findRelationByEntity('血压测量','老年人高血压')).replace(':', " ").split(" ")[1])
    # model.createNode('illness_name.csv','Disease')
    # print(model.findRelationByEntityAndRelation('现代病','心理咨询','BELONG_TO'))
    # model.createRelation('illness_another_names.csv', 'Disease', 'Disease', 'Alias')

























































