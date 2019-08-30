import json

import requests
from requests.exceptions import RequestException
from pyquery import PyQuery as pq

all_keys_dict = {}
def get_one_page(url):
    headers = {"User-Agent": "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content.decode('utf8')
        return None
    except RequestException as e:
        return e


def parse_one_page(html):
    doc = pq(html)
    items_name = list(doc('.basic-info .basicInfo-block .name').items())

    count = len(items_name)

    person_dict = {}
    for i in range(0, count):
        item_name_raw = items_name[i].text()
        item_name = ''.join(item_name_raw.split())
        all_keys_dict[item_name]=1


def main_of_all_keys(url):
    html = get_one_page(url)
    parse_one_page(html)


def write_to_file():
    with open('keys.json', 'a', encoding='utf-8') as f:
        f.write(json.dumps(all_keys_dict, ensure_ascii=False) + '\n')
        f.close()


