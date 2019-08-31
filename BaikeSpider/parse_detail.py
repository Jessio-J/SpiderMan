import json
import re

import requests
from requests.exceptions import RequestException
from pyquery import PyQuery as pq

from BaikeSpider.parser import parser_names_values


def get_one_page(url):
    """
    单词条请求
    :param url:
    :return:
    """
    headers = {"User-Agent": "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content.decode('utf8')
        return None
    except RequestException as e:
        return e


def parse_one_page(html, url):
    """
    单词条请求返回
    :param html:
    :param url:
    :return:
    """
    doc = pq(html)
    items_name = list(doc('.basic-info .basicInfo-block .name').items())
    items_value = list(doc('.basic-info .basicInfo-block .value').items())
    count = len(items_name)
    return parser_names_values(items_name, items_value, count, url)


def main_of_one_person(url):
    """
    单词条爬取主逻辑
    :param url:
    :return:
    """
    html = get_one_page(url)
    person_dict = parse_one_page(html, url)
    write_to_file(person_dict)


def write_to_file(content):
    """
    将返回的dict写文件
    :param content:
    :return:
    """
    with open('result.json', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()
