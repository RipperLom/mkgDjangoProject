from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings

from api.i_entity_query import EntityQueryApi
from api.i_relation_query import RelationQueryApi

# 初始化菜单
menus = settings.MKG_MENU    # 菜单
relas = settings.MKG_REL    # 关系
for i in menus:
    print(i)

# home page
def home_page(request):
    return entity_recognition(request)

# Create your views here.
# 实体识别
def entity_recognition(request):
    # handle data
    return render(request, 'index.html', {'menus': menus})


# 实体查询
def entity_query(request):
    # get请求，第一次进入判断参数entity是否为 空，为空那么显示当前空页面
    #   否则显示查询实体后的界面
    print('entity_query: ', request.GET)
    data = request.GET
    entity = data.get('entity', '')
    if entity:
        result = EntityQueryApi().push(**data)
        isexist = False     # 判断是否存在相关实体
        if result:
            isexist = True
        return render(request, 'entity_query.html',  {'menus': menus, 'result': result, 'isexist': isexist})
    #   否则显示查询试题后的界面
    return render(request, 'entity_query.html',  {'menus': menus})


# 关系查询
def relation_query(request):
    # handle data
    # get请求，第一次进入判断参数entity是否为 空，为空那么显示当前空页面
    #   否则显示查询试题后的界面
    print('relation_query: ', request.GET)
    data = request.GET
    entity1 = data.get('entity1', '')
    entity2 = data.get('entity2', '')
    relation = data.get('relation', '')
    if len(entity1 + entity2 + relation):
        result = RelationQueryApi().push(**data)
        isexist = False     # 判断是否存在相关结果
        if result:
            isexist = True
        return render(request, 'relation_query.html',  {'menus': menus, 'relas': relas, 'result': result, 'isexist': isexist})
    return render(request, 'relation_query.html',  {'menus': menus, 'relas': relas})
# 智能咨询
def robot_conversion(request):
    # handle data
    return render(request, 'robot_conversion.html',  {'menus': menus})
#  医学知识概览
def mkg_classify(request):
    # handle data
    return render(request, 'mkg_classify.html',  {'menus': menus})