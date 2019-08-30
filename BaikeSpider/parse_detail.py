import json

import requests
from requests.exceptions import RequestException
from pyquery import PyQuery as pq


def get_one_page(url):
    headers = {"User-Agent": "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content.decode('utf8')
        return None
    except RequestException as e:
        return e


def parse_one_page(html,url):
    doc = pq(html)
    items_name = list(doc('.basic-info .basicInfo-block .name').items())
    items_value = list(doc('.basic-info .basicInfo-block .value').items())
    count = len(items_name)

    person_dict = {}
    for i in range(0, count):
        item_name = items_name[i].text().replace(r'\s+','')
        item_value = items_value[i].text()
        if item_name == '中文名':
            person_dict['user:chineseName'] = item_value
        elif item_name == '别    名':
            person_dict['user:additionalName'] = item_value
        elif item_name == '国    籍':
            person_dict['user:nationality'] = item_value
        elif item_name == '民    族':
            person_dict['user:Nation'] = item_value
        elif item_name == '出生地':
            person_dict['user:birthPlace'] = item_value
        elif item_name == '出生日期':
            person_dict['user:birthDate'] = item_value
        elif item_name == '逝世日期':
            person_dict['user:deathDate'] = item_value
        elif item_name == '职    业':
            person_dict['user:Profession'] = item_value
        elif item_name == '毕业院校':
            person_dict['user:alumniOf'] = item_value
        elif item_name == '代表作品':
            person_dict['user:representativeWorks'] = item_value
        elif item_name == '主要成就':
            person_dict['user:achievement'] = item_value
        elif item_name == '所在剧团':
            person_dict['user:aﬃliation'] = item_value



    result_dict = {
        'url': url,
        'properties': person_dict
    }
    return result_dict




def main_of_one_person(url):
    html = get_one_page(url)
    person_dict = parse_one_page(html,url)
    write_to_file(person_dict)



def write_to_file(content):
    with open('result.json', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


