from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings

from api.i_entity_query import EntityQueryApi
from api.i_relation_query import RelationQueryApi
from api.i_entity_recognition_origin import EntityRecognitionApi
from api.i_entity_detail import EntityDetailyApi
from api.i_mkg_classify import ClassifyApi

# 初始化菜单
menus = settings.MKG_MENU    # 菜单
relas = settings.MKG_REL    # 关系
grams = settings.MKG_GRM    # 关系
for i in menus:
    print(i)

# home page
def home_page(request):
    return entity_recognition(request)

# Create your views here.
# 实体识别
def entity_recognition(request):
    # handle data
    method = request.method
    if method == 'POST':
        print('entity_recognition: ', request.POST)
        data = request.POST
        text = data.get('text', '')
        print('text:', text)     # test 110
        if text:
            result = EntityRecognitionApi().push(text=text)    # [{'name': str, 'tag': str, 'grammar': '', 'exist': bool}, ...]
            print('result: ', result)
            return render(request, 'entity_recognition.html', {'menus': menus, 'grams': grams, 'result': result})

    return render(request, 'entity_recognition.html', {'menus': menus})


# 实体查询
def entity_query(request):
    # get请求，第一次进入判断参数entity是否为 空，为空那么显示当前空页面
    #   否则显示查询实体后的界面
    print('entity_query: ', request.GET)
    data = request.GET
    entity = data.get('entity', '')
    if entity:
        result = EntityQueryApi().push(**data)
        isexist = False     # 判断是否存在相关实体, 默认需要False
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
        isexist = True    # 判断是否存在相关结果, 默认需要False
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
    data = request.GET
    classify_name = data.get('query', '')
    result = ClassifyApi().push(**data)
    import json
    print(json.dumps(result, ensure_ascii=False))
    return render(request, 'mkg_classify.html', {'menus': menus, 'result': json.dumps(result, ensure_ascii=False)})


# 详细信息查询
def detail(request):
    # handle data
    '''{
        name: '',
        detail: '',
        url: '',
        'little_propreties:' {'key':{'key': 'content', ...},...},
        large_propreties: {'key':{'key': 'content', ...},...} ,
         error: '',
    }'''
    result = {
            'name': '标题',
            'detail': '这里是内容',
            'url': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1558886937356&di=443322fe10034bc8be13e1438ccb924f&imgtype=0&src=http%3A%2F%2Fi1.bbs.fd.zol-img.com.cn%2Ft_s800x5000%2Fg5%2FM00%2F0B%2F0F%2FChMkJln10OuIHZh8AACJEEEqIzAAAhqsgBp1mIAAIko407.jpg',
            'little_propreties': {'小标题1':{'中文名称': 'ADM公司', '组织形式': '个人独资'}, '小标题2':{'中文名称': 'ADM公司', '组织形式': '个人独资'}},
            'large_propreties': {'大标题1':{'中文名称': 'ADM公司', '组织形式': '个人独资'}, '大标题2':{'中文名称': 'ADM公司', '组织形式': '个人独资'}} ,
            'type': 'Pathogenic_Site',
            'relation_name': ['中国科学研究院', '猪脑袋', '感冒1', '感冒2', '感冒3', ],
            'error': ''
        }

    # data = request.GET
    # entity = data.get('entity', '')
    # if entity:
    #     result = EntityDetailyApi().push()
    #
    #     # 先判断 error
    #     error = result.get('error', '')
    #     if not error:
    #         return  render(request, 'detail.html', {'menus': menus})
    # return redirect('/')
    mkg_entype = settings.MKG_ENTYPE
    result['entype'] = mkg_entype.get(result.get('type', ''), '')
    print(result)
    return render(request, 'detail.html', {'menus': menus, 'result': result})


def createNodes(nodes, tree_content):
    tree_content += '<ul>'
    if type(nodes) == list:
        for node in nodes:
            tree_content += '<li class="parent_li">'
            tree_content += '<span title="Collapse this branch"><i class="fa fa-minus-square" aria-hidden="true"></i>&nbsp;'+ node.get('text', '==') +'</span>'
            tree_content += '<a href="">&nbsp;&nbsp;[进入分类]</a>'




if __name__ == '__main__':
    object = {
        'text': '一级目录',
        'nodes': [
            {
                'text': '二级目录',
                'nodes': [
                    {
                        'text': '三级目录',
                        'nodes': None
                    },
                    {
                        'text': '三级目录',
                        'nodes': None
                    }
                ]},
            {
                'text': '二级目录',
                'nodes': [
                    {
                        'text': '三级目录',
                        'nodes': None
                    }
                ]}
        ]
    }
    tree_content = ""
    createNodes(object, tree_content)