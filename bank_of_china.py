# -*- coding: utf-8 -*- 
# @Time : 2022/2/22 14:22 
# @Author : melon
"""
爬取中国银行财报的pdf
"""
# @File : bank_of_china.py
import requests
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/98.0.4758.102 Safari/537.36',

}


def get_html(url):
    """获取网页"""
    r = requests.get(url, headers=header)
    r.encoding = 'utf-8'
    return r.text


def get_url(html):
    """获取一级url"""
    total_url = []
    soup = BeautifulSoup(html, 'lxml')
    list_url = soup.select('body > div > div.main > div > ul>li')
    for li in list_url:
        url = li.find('a').attrs['href']
        total_url.append(url)


if __name__ == "__main__":
    url = r'https://www.boc.cn/investor/ir3/'
    html = get_html(url)
    get_url(html)
