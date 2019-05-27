#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 20:42
# @Author  : 徐纪茂
# @File    : pameicijiaju.py
# @Software: PyCharm
# @Email   : jimaoxu@163.com

import requests
import random
import time
from lxml import etree
import csv

# url = 'http://www.shuoshuokong.com/juzi/index_66.html'
fenlei = 'shanggan'
page = 69
filename = '伤感'

for n in range(1, page+1):
    data = None
    try:
        if n == 1:
            data = requests.get(url='http://www.shuoshuokong.com/%s/index.html' % fenlei, params={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'})
        else:
            data = requests.get(url='http://www.shuoshuokong.com/%s/index_%s.html' % (fenlei, str(n)), params={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'})
        data.encoding = 'utf8'
        xpath_html = etree.HTML(data.text)
        img_xpath = '//ul[@class="g-list-box"]/li//img/@src'
        # 'http://www.shuoshuokong.com  /d/file/2019-05/17d991156e25920465b9cb7f6107fb96.jpg'
        title_xpath = '//ul[@class="g-list-box"]/li/a/@title'
        content_xpath = '//ul[@class="g-list-box"]/li/p/text()'
        content_url = '//ul[@class="g-list-box"]/li/a[1]/@href'
        img = xpath_html.xpath(img_xpath)
        title = xpath_html.xpath(title_xpath)
        content = xpath_html.xpath(content_url)
        img_name_list = [i.split('/')[-1] for i in img]
        for i in range(10):
            with open('static/images/%s/%s.csv' % (fenlei, filename), 'a', newline='', encoding='utf8') as w:
                resp = requests.get(url='http://www.shuoshuokong.com' + content[i], params={'User-Agent': 'Mozilla/5.0'})
                resp.encoding = 'utf8'
                e = etree.HTML(resp.text)
                juzi = e.xpath('//div[@class="g-detail-font"]/p/text()')
                # print(juzi)
                csv_w = csv.writer(w, delimiter='#')
                csv_w.writerow((title[i],' '.join(juzi), img_name_list[i]))
        for i in range(10):
            url = 'http://www.shuoshuokong.com' + img[i]
            img_data = requests.get(url=url, params={'User-Agent': 'Mozilla/5.0'})
            with open('static/images/%s/%s' % (fenlei, img_name_list[i]), 'wb') as w:
                w.write(img_data.content)
    except Exception as e:
        print(e)
    time.sleep(random.randint(1, 20) * 0.1)
    print('第%s页'%n)
