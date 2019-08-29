import json
from urllib.parse import urlencode
import requests
from requests import RequestException
import datetime
import time


def get_page_index(offset, keyword, ts):
    data = {
        'aid': 24,
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 10,
        'cur_tab': 1
    }
    headers = {
        'cookie': 'tt_webid=6730187751457211907; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6730187751457211907; '
                  'csrftoken=2d7a6ea0a54caa46a35c83d2a5e97411; s_v_web_id=05bf9bc061f31c1ee4d3a86a2291b533 '
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(data)
    print(url)
    try:
        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求失败')
        return None


def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')


def get_page_detail(url):
    headers = {
        'cookie': 'tt_webid=6730187751457211907; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6730187751457211907; '
                  'csrftoken=2d7a6ea0a54caa46a35c83d2a5e97411; s_v_web_id=05bf9bc061f31c1ee4d3a86a2291b533 '
    }
    try:
        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情失败')
        return None


def main():
    t = time.time()
    ts = int(round(t * 1000))
    html = get_page_index(0, '街拍', ts)
    for url in parse_page_index(html):
        print('url:'+str(url))
        if url:
            detail = get_page_detail(url)
            print(detail)

# def parse_page_detail(detail):


if __name__ == '__main__':
    main()
