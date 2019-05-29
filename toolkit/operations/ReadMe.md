## 中关村图谱设计中心-医疗知识图谱项目



**本文件夹主要放置的是处理数据的类和方法**

illness_class.py  -------是构建所有的疾病的三元组关系， 可以生成：疾病与别名之间的三元组关系(illness_another_names.csv)，
疾病与发病部位之间的关系(illness_pathogenic_site.csv)，疾病与典型症状的三元组关系(illness_classical_symptom.csv)，
疾病与并发症之间的三元组(illness_complication.csv)，疾病与相关检查的三元组关系(illness_examination.csv)，
疾病与常用药品之间的三元组关系(illness_regular_medication.csv)，疾病与手术的三元组关系(illness_surgeries_name.csv)，
疾病与治疗科室的三元组关系(illness_Treatment_of_department.csv)。运行这个类可以获取所有的三元组关系的csv格式文件



