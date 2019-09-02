import re

# 人物属性字典
person_dict = {

}

# 人物孩子实体
children = []
# 人物父母实体
parent = []

def parser_names_values(items_name, items_value, count, url):
    """
    具体解析逻辑
    :param items_name:属性名
    :param items_value:属性值
    :param count:当前词条属性条数
    :param url:当前词条对应url
    :return:词条dict
    """

    for i in range(0, count):
        item_name_raw = items_name[i].text()
        item_name = ''.join(item_name_raw.split())
        item_value = items_value[i].text()
        if re.search(r"[中文|姓|本]名", item_name):
            person_dict['user:name'] = item_value
            if re.search(r'[0-9a-zA-Z_]', item_value):
                person_dict['user:englishName'] = item_value
            else:
                person_dict['user:chineseName'] = item_value
        elif re.search(r"[别名|艺名|别称]", item_name):
            person_dict['user:additionalName'] = item_value
        elif item_name == '外文名':
            person_dict['user:englishName'] = item_value
        elif item_name == '国籍':
            person_dict['user:nationality'] = item_value
        elif item_name == '民族':
            person_dict['user:nation'] = item_value
        elif item_name == '出生地':
            birth_place = {
                'user:key': 'user:Location',
                'user:name': item_value
            }
            person_dict['user:birthPlace'] = birth_place
        elif re.search(r"[生日|出生]", item_name):
            person_dict['user:birthDate'] = item_value
        elif re.search(r"[逝世|去世]", item_name):
            person_dict['user:deathDate'] = item_value
        elif item_name == '职业':
            if re.search(r"书法", item_value):
                person_dict['user:key'] = 'user:Calligrapher'
            elif re.search(r"雕", item_value):
                person_dict['user:key'] = 'user:Sculptor'
            elif re.search(r"画", item_value):
                person_dict['user:key'] = 'user:Painter'
            elif re.search(r"歌", item_value):
                person_dict['user:key'] = 'user:Singer'
            elif re.search(r"作曲", item_value):
                person_dict['user:key'] = 'user:Composer'
            elif re.search(r"演奏", item_value):
                person_dict['user:key'] = 'user:Performer'
            elif re.search(r"音乐", item_value):
                person_dict['user:key'] = 'user:Musician'
            elif re.search(r"设计", item_value):
                person_dict['user:key'] = 'user:Designer'
            else:
                person_dict['user:key'] = 'user:Painter'
            person_dict['user:profession'] = item_value
        elif re.search(r"毕业", item_name):
            organization_dict = {
                'user:key': 'user:Organization',
                'user:name': item_value
            }
            person_dict['user:alumniOf'] = organization_dict
        elif item_name == '代表作品':
            work_dict = {
                'user:key': 'user:CreativeWork',
                'user:name': item_value
            }
            person_dict['user:works'] = work_dict
        elif item_name == '主要成就':
            person_dict['user:achievement'] = item_value
        elif re.search(r"[所在剧团|工作单位]", item_name):
            affiliation_dict = {
                'user:key': 'user:Organization',
                'user:name': item_value
            }
            person_dict['user:affiliation'] = affiliation_dict
        elif item_name == '性别':
            person_dict['user:gender'] = item_value
        elif re.search(r"[儿子|女儿|儿女]", item_name):
            child = {
                'user:key': 'user:Person',
                'user:name': item_value
            }
            children.append(child)
        elif re.search(r"[现居|居住地]", item_name):
            address_dict = {
                'user:key': 'user:Location',
                'user:name': item_value
            }
            person_dict['user:address'] = address_dict
        elif item_name == '妻子':
            spouse = {
                'user:key': 'user:Person',
                'user:name': item_value
            }
            person_dict['user:spouse'] = spouse
        elif re.search(r"[父|母]", item_name):
            parent_dict = {
                'user:key': 'user:Person',
                'user:name': item_value
            }
            parent.append(parent_dict)
        elif re.search(r"奖", item_name):
            person_dict['user:award'] = item_value
    if len(children) > 0:
        person_dict['user:children'] = children
    if len(parent) > 0:
        person_dict['user:parent'] = parent
    if 'user:key' not in person_dict.keys():
        person_dict['user:key'] = 'Painter'
    # 返回结果
    result_dict = {
        'url': url,
        'properties': person_dict
    }
    if person_dict:
        return result_dict
    else:
        return None
