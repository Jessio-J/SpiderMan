import re


def parser_names_values(items_name, items_value, count, url):
    """
    具体解析逻辑
    :param items_name:属性名
    :param items_value:属性值
    :param count:当前词条属性条数
    :param url:当前词条对应url
    :return:词条dict
    """
    person_dict = {

    }
    children = []
    for i in range(0, count):
        item_name_raw = items_name[i].text()
        item_name = ''.join(item_name_raw.split())
        item_value = items_value[i].text()
        if re.search(r"[中文|姓|本]名", item_name):
            person_dict['user:chineseName'] = item_value
        elif re.search(r"[别名|艺名|别称]", item_name):
            person_dict['user:additionalName'] = item_value
        elif item_name == '外文名':
            person_dict['user:EnglishName'] = item_value
        elif item_name == '国籍':
            person_dict['user:nationality'] = item_value
        elif item_name == '民族':
            person_dict['user:nation'] = item_value
        elif item_name == '出生地':
            person_dict['user:birthPlace'] = item_value
        elif re.search(r"[生日|出生]", item_name):
            person_dict['user:birthDate'] = item_value
        elif re.search(r"[逝世|去世]", item_name):
            person_dict['user:deathDate'] = item_value
        elif item_name == '职业':
            if re.search(r"书法", item_value):
                person_dict['user:key'] = 'Calligrapher'
            elif re.search(r"雕", item_value):
                person_dict['user:key'] = 'Sculptor'
            elif re.search(r"画", item_value):
                person_dict['user:key'] = 'Painter'
            elif re.search(r"歌", item_value):
                person_dict['user:key'] = 'Singer'
            elif re.search(r"作曲", item_value):
                person_dict['user:key'] = 'Composer'
            elif re.search(r"演奏", item_value):
                person_dict['user:key'] = 'Performer'
            elif re.search(r"音乐", item_value):
                person_dict['user:key'] = 'Musician'
            elif re.search(r"设计", item_value):
                person_dict['user:key'] = 'Designer'
            # elif re.search(r"演员", item_name):
            #     person_dict['user:key'] = 'Actor'
            else:
                person_dict['user:key'] = 'Artist'
            person_dict['user:profession'] = item_value
        elif re.search(r"毕业", item_name):
            person_dict['user:alumniOf'] = item_value
        elif item_name == '代表作品':
            person_dict['user:CreativeWork'] = item_value
        elif item_name == '主要成就':
            person_dict['user:achievement'] = item_value
        elif re.search(r"[所在剧团|工作单位]", item_name):
            person_dict['user:affiliation'] = item_value
        elif item_name == '性别':
            person_dict['user:gender'] = item_value
        elif re.search(r"[儿子|女儿|儿女]", item_name):
            child = {
                'user:key': 'Person',
                'user:name': item_value
            }
            children.append(child)
        elif re.search(r"[现居|居住地]", item_name):
            person_dict['user:address'] = item_value
        elif item_name == '妻子':
            spouse = {
                'user:key': 'Person',
                'user:name': item_value
            }
            person_dict['user:spouse'] = spouse
        elif re.search(r"[父|母]亲", item_name):
            parent = {
                'user:key': 'Person',
                'user:name': item_value
            }
            person_dict['user:parent'] = parent
        elif re.search(r"奖项", item_name):
            person_dict['user:award'] = item_value
    if len(children) > 0:
        person_dict['user:children'] = children
    # 返回结果
    result_dict = {
        'url': url,
        'properties': person_dict
    }
    if person_dict:
        return result_dict
    else:
        return None
