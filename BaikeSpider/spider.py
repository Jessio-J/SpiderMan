import json
import re
from urllib.parse import urlencode
import requests
from requests import RequestException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pyquery import PyQuery as pq

from BaikeSpider.test import main_of_one_person

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome('D:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe',chrome_options=chrome_options)
wait = WebDriverWait(browser,10)
# 获取每页词条
def get_entry_url(offset, page):
    try:
        data = {
            'limit': 30,
            'index': page,
            'offset': offset
        }
        url = 'https://baike.baidu.com/fenlei/%E8%89%BA%E6%9C%AF%E5%AE%B6?' + urlencode(data)
        browser.get(url)
        return get_url_list()
    except TimeoutError as e:
        print(e)
        return get_entry_url(offset, page)

def get_url_list():
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#content-main > div.grid.p-container > div.g-row.p-main > div.g71 > div.g-row.p-entry.log-set-param > div.grid-list.grid-list-spot > ul > li:nth-child(1)')))
    ul = browser.find_element_by_css_selector('#content-main > div.grid.p-container > div.g-row.p-main > div.g71 > div.g-row.p-entry.log-set-param > div.grid-list.grid-list-spot > ul')
    entries = ul.find_elements_by_css_selector('.photo .pic-content')
    print(len(entries))
    for entry in entries:
        entryurl = entry.get_attribute('href')
        main_of_one_person(entryurl)




def main():
    get_entry_url(120, 5)


if __name__ == '__main__':
    main()
