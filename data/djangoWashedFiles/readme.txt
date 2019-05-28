文件介绍：
本文件共有9个实体的csv文件和一个打标注的txt文件
csv文件介绍：

jkw_39_another_names.csv	代表的是别名的数据，列名为[name]，共有8347条实体数据
jkw_39_complications.csv	代表的是并发症的数据，列名为[name]，共有2861条实体数据
jkw_39_deparments.csv	代表的是科室的数据，列名为[name]，共有52条实体数据
jkw_39_drugs.csv		代表的是药品的数据，列名为[name,img,info_match]，其中每一个属性均是str格式，
			info_match格式：{key1:{k1:v1},key2:{k2:v2},key3:{k3:v3}} ，主要的键有：基本知识{可能疾病、诱因、诊断、可用药、检查项目}；
			共有6804条实体数据
jkw_39_examines.csv	代表的是检查项目的数据，列名为[name,detail,info_match]，其中每一个属性均是str格式，
			info_match格式：{key1:{k1:v1},key2:{k2:v2},key3:{k3:v3}} ，主要的键有：price、notice；
			共有2196条实体数据
jkw_39_illness.csv		代表的是疾病的数据，列名为[name,img,detail,info_match]，其中每一个属性均是str格式，
			info_match格式：{key1:{k1:v1},key2:{k2:v2},key3:{k3:v3}} ，主要的键有：基本知识、诊疗知识、去医院必看；
			共有7572条实体数据
jkw_39_positions.csv	代表的是发病部位的数据，列名为[name]，共有81条实体数据
jkw_39_surgeries.csv	代表的是手术项目的数据，列名为[name,detail,info_match]，其中每一个属性均是str格式，
			info_match格式：{key1:{k1:v1},key2:{k2:v2},key3:{k3:v3}} ，主要的键有：price；
			共有1121条实体数据
jkw_39_symptom.csv	代表的是症状的数据，列名为[name,img,detail,info_match]，其中每一个属性均是str格式，
			info_match格式：{key1:{k1:v1},key2:{k2:v2},key3:{k3:v3}} ，主要的键有：【药品名称】、【成份】、【性状】、【功能主治】、【用法用量】、【不良反应】、
			【禁忌】、【注意事项】、【药物相互作用】、【贮藏】、【包装规格】、【有效期】、【执行标准】、【批准文号】、【说明书修订日期】、【生产企业】；
			共有6305条实体数据

txt文件介绍：

total_entity.txt		这是我们将所有获取的实体数据进行达标之后的文件，共有32538条实体数据，其中格式如：实体（空格）标签
			科室 21
			部位 22
			症状 23
			手术 24
			检测 25
			药品 26
			疾病 27





