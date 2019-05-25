from utils import Neo4j

neo4jmodel = Neo4j.Neo4j()

#导入实体
# print('实体加载开始：')
# neo4jmodel.createNode('../../data/csvOrTxtFiles/another_names.csv','Disease') # 导入疾病别名
# neo4jmodel.createNode('../../data/csvOrTxtFiles/complication_name.csv','Symptom') # 导入并发症实体
# neo4jmodel.createNode('../../data/csvOrTxtFiles/examination_name.csv','Operation') #导入检查实体
# neo4jmodel.createNode('../../data/csvOrTxtFiles/illness_name.csv','Disease') #导入疾病实体
# neo4jmodel.createNode('../../data/csvOrTxtFiles/pathogenic_site_name.csv','Pathogenic_Site')  #导入病发部位
# neo4jmodel.createNode('../../data/csvOrTxtFiles/regular_medication_name.csv','Drug') #导入药品实体
# neo4jmodel.createNode(../../data/csvOrTxtFiles/surgeries_name.csv','Check') #导入手术实体
# neo4jmodel.createNode('../../data/csvOrTxtFiles/symptom_name.csv','Symptom') #导入症状实体
# neo4jmodel.createNode('../../data/csvOrTxtFiles/Treatment_of_department_name.csv','Department') #导入科室
# print('实体加载完毕！！')
#导入关系
# 导入病名实体和病名别名实体之间的关系
print('加载关系！！')
neo4jmodel.createRelation('../../data/csvOrTxtFiles/NLPProject/illness_another_names.csv','Disease','Disease','ALIAS')
# 导入病名实体和症状实体之间的关系
neo4jmodel.createRelation('../../data/csvOrTxtFiles/illness_classical_symptom.csv','Disease','Symptom','HAS_SYMPTOM')
# 导入病名实体和并发症实体之间的关系
neo4jmodel.createRelation('../../data/csvOrTxtFiles/illness_complication.csv','Disease','Symptom','ACOMPANY_SYMPTOM')
#导入病名实体与药物实体之间的关系
neo4jmodel.createRelation('../../data/csvOrTxtFiles/illness_regular_medication.csv','Disease','Drug','COMMON_DRUG')
# 导入病名实体与检查实体之间的关系
neo4jmodel.createRelation('../../data/csvOrTxtFiles/illness_examination.csv','Disease','Operation','NEED_CHECK')
# 导入病名实体与手术实体之间的关系
neo4jmodel.createRelation('../../data/csvOrTxtFiles/illness_surgeries_name.csv','Disease','Check','RECOMMEND_SURGERY')
# 导入病名实体与部位实体之间的关系
neo4jmodel.createRelation('../../data/csvOrTxtFiles/illness_pathogenic_site.csv','Disease','Pathogenic_Site','COMMON_DISEASE_SITE')
#导入Disease和Department之间的关系
neo4jmodel.createRelation('../../data/csvOrTxtFiles/illness_Treatment_of_department.csv','Disease','Department','BELONGS_TO')
print('关系加载完毕！！！')