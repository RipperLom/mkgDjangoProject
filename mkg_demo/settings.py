import os
import json
import sys

# 当前目录文件路径
MKGDEMO_BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 配置文件路径
MKGDEMO_CONFIG_DIR = os.path.join(MKGDEMO_BASE_DIR, 'config_file')

# -- 读取MKG菜单栏配置
mkg_configMenu_path = os.path.join(MKGDEMO_CONFIG_DIR, 'mkg_menu.json')
MKG_MENU = []
with open(mkg_configMenu_path, 'r', encoding='utf-8') as fr:
    MKG_MENU = json.load(fr)    # MKG菜单栏内容
    print('MKG_MENU: ', MKG_MENU, '-->type: ', type(MKG_MENU))


# 添加api路径，防止找不到
API_DIR = os.path.join(os.path.dirname(MKGDEMO_BASE_DIR), 'api')
sys.path.append(API_DIR)

# --读取MKG关系配置
mkg_configRel_path = os.path.join(MKGDEMO_CONFIG_DIR, 'mkg_relationname.json')
MKG_REL = []
with open(mkg_configRel_path, 'r', encoding='utf-8') as fr:
    MKG_REL = json.load(fr)    # MKG关系内容
    print('MKG_REL: ', MKG_REL, '-->type: ', type(MKG_REL))

# --读取GRAMMARS关系配置
grm_configRel_path = os.path.join(MKGDEMO_CONFIG_DIR, 'grammars.json')
MKG_GRM = []
with open(grm_configRel_path, 'r', encoding='utf-8') as fr:
    MKG_GRM = json.load(fr)    # MKG关系内容
    print('MKG_GRM: ', MKG_GRM, '-->type: ', type(MKG_GRM))


# 连接neo4j数据库, 并初始化Neo4j对象
NEO4J_HOST = "http://localhost:7474"
NEO4J_NAME = "neo4j"
NEO4J_PSD = "123456"
from toolkit.models.neo4j_model import Neo4j
NEO4J_OBJ = Neo4j()     # 创建neo4j对象
try:
    NEO4J_OBJ.connectDB(host=NEO4J_HOST, username=NEO4J_NAME, password=NEO4J_PSD)
    print(NEO4J_OBJ)
    print('初始化neo4j成功！')
except Exception as e:
    print('初始化neo4j失败！！！')


# 获取实体类型内容
entity_type_en2cn_path = os.path.join(MKGDEMO_CONFIG_DIR, 'entity_type_en2cn.json')
MKG_ENTYPE = {}
with open(entity_type_en2cn_path, 'r', encoding='utf-8') as fr:
    MKG_ENTYPE_LIST = json.load(fr)    # MKG关系内容
    print('MKG_ENTYPE: ', MKG_ENTYPE, '-->type: ', type(MKG_ENTYPE))
for line in MKG_ENTYPE_LIST:
    MKG_ENTYPE[line['type']] = line

# 树结构关系数据文本
tree_path = os.path.join(os.path.dirname(MKGDEMO_BASE_DIR), 'data', 'djangoWashedFiles', 'micropedia_tree.txt')
with open(tree_path, 'r', encoding='utf-8') as fr:
    data = fr.readlines()
    data = [i.replace('\n', '') for i in data]
    print('读取树结构成功。。，')
RELATION = {}   # 树结构内容保存
for d in data:
    k, v = d.split(' ')
    if not RELATION.get(k, None):
        RELATION[k] = [v, ]
    else:
        RELATION[k].append(v)


