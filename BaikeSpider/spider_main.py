from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pyquery import PyQuery as pq

from BaikeSpider.constants import get_Info_list
from BaikeSpider.parse_detail import main_of_one_person

# selenium模拟网页获取渲染后的有数据页面
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome()
# 设置加载等待
wait = WebDriverWait(browser, 10)


def get_entry_url(offset, page):
    """
    获取当前页的所有词条
    :param offset: 页偏移
    :param page: 页码
    :return:
    """
    try:
        data = {
            'limit': 30,
            'index': page,
            'offset': offset
        }
        url = get_Info_list()[0] + urlencode(data)
        browser.get(url)
        get_url_list()
    except TimeoutError as e:
        print(e)
        get_entry_url(offset, page)


def get_url_list():
    """
    获取词条对应的url
    :return:
    """
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                    '#content-main > div.grid.p-container > div.g-row.p-main > div.g71 > div.g-row.p-entry.log-set-param > div.grid-list.grid-list-spot > ul > li:nth-child(1)')))
    ul = browser.find_element_by_css_selector(
        '#content-main > div.grid.p-container > div.g-row.p-main > div.g71 > div.g-row.p-entry.log-set-param > div.grid-list.grid-list-spot > ul')
    entries = ul.find_elements_by_css_selector('.list .title')
    print(len(entries))
    for entry in entries:
        entryurl = entry.get_attribute('href')
        main_of_one_person(entryurl)


def main():
    # get_Info_list()[1]+1
    for i in range(1, get_Info_list()[1]+1):
        get_entry_url((i - 1) * 30, i)


if __name__ == '__main__':
    main()
