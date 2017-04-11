# -*- coding: utf-8 -*-
import sys
from django.http import HttpResponse, Http404
from django.views.generic.list import ListView
from django.shortcuts import render
from django.urls import reverse
import json
import urllib
import urllib2
import re
import requests
from urllib2 import urlparse
import html


# 首页
def index(request):
    return render(request, 'index.html')


def index1(request):
    if request.method == 'GET':
        return render(request, 'index1.html')
    else:
        url_name = request.POST['url_name']
        mydict = {"url_name": url_name}
        return HttpResponse(
            json.dumps(mydict),
            content_type="application/json"
        )

# 显示爬取页面
def page_item(request):
    url_name = request.POST['url_name']
    load_html = requests.get(url_name)
    load_html.encoding = 'utf-8'
    content = load_html.text
    # 标题
    title = re.findall(r'<title>(.*?)</title>', content)
    title = title[0]
    # 头部<head>
    pattern_head = re.compile('<head>.*?</head>', re.S)
    head_content = re.findall(pattern_head, load_html.text)
    head = head_content[0].replace('<head>', '')   # 去掉head
    head = head.replace('</head>', '')
    pattern_head_href = re.compile('href=\"css.*?\"', re.S)   # 匹配没有http的css
    head_href = re.findall(pattern_head_href, head)
    head_href_arr = []
    if head_href != '':
        for h_href in head_href:
            h_href = h_href.replace('href="', '')
            h_href = h_href.replace('"', '')
            head = head .replace(h_href,'')
            head_href_arr.append(h_href)
    pattern_sc_head = re.compile('<script.*?</script>', re.S)
    sc_head = re.findall(pattern_sc_head, head)   # 头部 除了js文件
    src_head_arr1 = []  # 引入的js文件
    src_head_arr2 = []  # js代码
    for s_head in sc_head:
        pattern_src = re.compile('[a-z]+:\/\/[a-zA-Z0-9_\-\/.%]+', re.L)  # 匹配js
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

    # body
    pattern_body = re.compile('<body.*?</body>', re.S)
    pattern_body1 = re.compile('<body.*?>', re.S)
    body_content = re.findall(pattern_body, load_html.text)
    b = re.findall(pattern_body1, load_html.text)
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
    # 所有<body>里面的元素
    element = re.findall(r'<([a-z]+)', body)
    element_arr = []
    for e in element:
        element_arr.append(e)

    # 根据元素获取里面所有所有的class及对应的链接
    con = re.findall(r'<(.*?)>', body)
    classes_arr = []
    urls_arr = []
    for co in con:
        classes = re.findall(r'class="(.*?)"', co)
        if len(classes) != 0:
            classes_arr.append(classes[0])
        else:
            classes_arr.append('')
        url = re.findall(r'([a-z]+:\/\/[a-zA-Z0-9_\-\/.%]+)', co)
        if len(url) != 0:
            urls_arr.append(url[0])
        else:
            urls_arr.append('')

    dic = {"url": url_name, "title_name": title, "head": head, "head_href": head_href_arr, "src_head1": src_head_arr1,
           "src_head2": src_head_arr2, "body": body,"element":element_arr,"classes": classes_arr,"urls":urls_arr}
    return render(request, 'page_item.html', {'dic':json.dumps(dic)})
    # return render(request, 'page_item.html', dic)




def test(request):
    url_name = request.POST['url_name']
    # print url_name
    # exit()
    dic = {"url_name": url_name}
    return render(request, 'test.html', dic)

# 首页视图,继承自ListVIew
class IndexView(ListView):
    # template_name属性用于指定使用哪个模板进行渲染
    template_name = "home/index1.html"
    # context_object_name属性用于给上下文变量取名（在模板中使用该名字）
    context_object_name = "home_index"
