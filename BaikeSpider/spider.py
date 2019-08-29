import json
from urllib.parse import urlencode
import requests
from requests import RequestException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq

browser = webdriver.Chrome('D:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')
wait = WebDriverWait(browser,10)

def get_list(offset, page):
    try:
        data = {
            'limit': 30,
            'index': page,
            'offset': offset
        }
        url = 'http://baike.baidu.com/fenlei/%E8%89%BA%E6%9C%AF%E5%AE%B6?' + urlencode(data)
        browser.get(url)
        return get_products()
    except TimeoutError as e:
        print(e)
        return get_list(offset, page)

def get_products():
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#content-main > div.grid.p-container > div.g-row.p-main > div.g71 > div.g-row.p-entry.log-set-param > div.grid-list.grid-list-spot > ul > li:nth-child(1)')))
    html = browser.page_source
    doc = pq(html)
    ul = doc('#content-main > div.grid.p-container > div.g-row.p-main > div.g71 > div.g-row.p-entry.log-set-param > div.grid-list.grid-list-spot > ul').items()
    for li in ul:
        product = {
            'detail': li.find('')
        }


def main():
    html = get_list(120, 5)
    print(html)
    # for url in parse_page_index(html):
    #     print('url:' + str(url))
    #     if url:
    #         detail = get_page_detail(url)
    #         print(detail)


# def parse_page_detail(detail):


if __name__ == '__main__':
    main()
