# -*- coding: utf-8 -*-
import sys
from django.http import HttpResponse, Http404
from django.views.generic.list import ListView
from django.shortcuts import render
from django.urls import reverse
import json
import urllib2


# 首页
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        url_name = request.POST['url_name']
        # response = urllib2.urlopen(url_name)
        # html = response.read()

        # dic = {"url_name": urllib2.quote(url_name)}
        dic = {"url_name": url_name}
        return HttpResponse(
            json.dumps(dic),
            content_type="application/json"
        )

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
    # url = request.GET['url']
    # response = urllib2.urlopen(urllib2.unquote(url))
    # html = response.read()
    return render(request, 'page_item.html')


def test(request):
    url_name = request.POST['url_name']
    print url_name
    exit()
    return render(request, 'test.html', url_name)

# 首页视图,继承自ListVIew
class IndexView(ListView):
    # template_name属性用于指定使用哪个模板进行渲染
    template_name = "home/index1.html"
    # context_object_name属性用于给上下文变量取名（在模板中使用该名字）
    context_object_name = "home_index"
