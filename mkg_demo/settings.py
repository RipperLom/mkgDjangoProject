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
from mkg_demo.models.neo4j_model import Neo4j
NEO4J_OBJ = Neo4j()     # 创建neo4j对象
try:
    NEO4J_OBJ.connectDB(host=NEO4J_HOST, username=NEO4J_NAME, password=NEO4J_PSD)
    print(NEO4J_OBJ)
    print('初始化neo4j成功！')
except Exception as e:
    print('初始化neo4j失败！！！')

