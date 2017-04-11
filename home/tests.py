# -*- coding:utf-8 -*-
from django.test import TestCase

# Create your tests here.
# from  crawler.scrapy_crawler import main
# test = main.test()
# main.a()

import urllib
import urllib2
import requests
import re

headers={
    "Host":"www.baidu.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
}
url = 'http://hhb.cbi360.net/'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# headers = {'User-Agent': user_agent}
html = requests.get(url)
html.encoding = 'utf-8'

# response = urllib2.urlopen(url)
# load_html = response.read()
# request = urllib2.Request(url, headers=headers)
# response = urllib2.urlopen(request)
# content = response.read().decode('utf-8')

content = html.text
# 获取title
def get_title():
    title = re.findall(r'<title>(.*?)</title>', content)
    title = title[0]
    return title
# t = get_title()
# print t

# 获取head
def get_head():
    pattern_head = re.compile('<head>.*?</head>', re.S)
    head_content = re.findall(pattern_head, html.text)
    head = head_content[0].replace('<head>', '')  # 去掉head
    head = head.replace('</head>', '')
    pattern_head_href = re.compile('href=\"css.*?\"', re.S)  # 匹配没有http的css
    head_href = re.findall(pattern_head_href, head)
    head_href_arr = []
    if head_href != '':
        for h_href in head_href:
            h_href = h_href.replace('href="', '')
            h_href = h_href.replace('"', '')
            head = head.replace(h_href, '')
            head_href_arr.append(h_href)
    pattern_sc_head = re.compile('<script.*?</script>', re.S)
    sc_head = re.findall(pattern_sc_head, head)  # 头部 除了js文件
    src_head_arr1 = []  # 引入的js文件
    src_head_arr2 = []  # js代码
    for s_head in sc_head:
        pattern_src = re.compile('[a-z]+:\/\/[a-zA-Z0-9_\-\/.%]+', re.S)  # 匹配js
        src = re.findall(pattern_src, s_head)
        if len(src) == 1:
            src_head_arr1.append(src[0])  # 保存到一个数组 js文件
        pattern_sc_ = re.compile('<script.*?>', re.S)  # 匹配script开头
        s_ = re.findall(pattern_sc_, s_head)
        s_head_ = s_head.replace(s_[0], '')
        s_head_ = s_head_.replace('</script>', '')
        s_head_ = s_head_.replace('\r\n', '')
        if s_head_ != '':
            src_head_arr2.append(s_head_)  # 保存到一个数组 js代码
        head = head.replace(s_head, '')
    return head,src_head_arr1,src_head_arr2

# 获取body
def get_body():
    pattern_body = re.compile('<body.*?</body>', re.S)
    pattern_body1 = re.compile('<body.*?>', re.S)
    body_content = re.findall(pattern_body, html.text)
    b = re.findall(pattern_body1, html.text)
    body = body_content[0].replace(b[0], '')
    body = body.replace('</body>', '')
    pattern_script1 = re.compile('<script>.*?</script>', re.S)
    script1 = re.findall(pattern_script1, body)
    for sc1 in script1:
        body = body.replace(sc1, '')
    pattern_script2 = re.compile('<script.*?</script>', re.S)
    script2 = re.findall(pattern_script2, body)
    for sc2 in script2:
        body = body.replace(sc2, '')
    return body

# bo = get_body()
# print bo

# 所有<body>里面的元素
def get_element():
    # pattern_element = re.compile('<[a-z]+', re.S)
    bo = get_body()
    element = re.findall(r'<([a-z]+)',bo)
    element_arr = []
    for e in element:
        element_arr.append(e)
    # element_set = set()  # 去重
    # for e in elemet:
    #     element_set.add(e)
    # element_arr = []
    # for es in element_set:
    #     element_arr.append(es)
    # print len(elemet)
    return element_arr
# get_element()

# 获取所有的class
def get_classes():
    bo = get_body()
    classes = re.findall(r'class="(.*?)"', bo)
    classes_set = set()
    for cla in classes:
        c_split = cla.split(' ')
        # if c_split[0] != '':
        #     classes_set.add(c_split[0])
        for cl in c_split:
            if cl != '':
                classes_set.add(cl)
    classes_arr = []
    for c in classes_set:
        print c
        classes_arr.append(c)

# get_classes()
# 根据元素获取里面所有所有的class及对应的链接
def get_class_url():
    bo = get_body()
    con = re.findall(r'<(.*?)>',bo)
    classes_arr = []
    urls_arr = []
    for co in con:
        classes = re.findall(r'class="(.*?)"', co)
        if len(classes) != 0:
            classes_arr.append(classes[0])
        else:
            classes_arr.append('')
        url = re.findall(r'([a-z]+:\/\/[a-zA-Z0-9_\-\/.%]+)',co)

        if len(url) != 0:
            urls_arr.append(url[0])
        else:
            urls_arr.append('')
    # dic = dict(zip(classes_arr,urls_arr))  # 用字典保存
    # dic.pop('')    # 删除key是空值
    print classes_arr
    # print classes_arr
    # print urls_arr

get_class_url()

