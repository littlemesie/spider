# -*- coding: utf-8 -*-
import sys
from django.http import HttpResponse, Http404
from django.views.generic.list import ListView
from django.shortcuts import render
import json

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        url_name = request.POST['url_name']
        mydict = {"url_name": url_name}
        return HttpResponse(
            json.dumps(mydict),
            content_type="application/json"
        )

def test(request):
    url_name = request.POST['url_name']
    print url_name
    exit()
    return render(request, 'test.html', url_name)

# 首页视图,继承自ListVIew
class IndexView(ListView):
    # template_name属性用于指定使用哪个模板进行渲染
    template_name = "home/index.html"
    # context_object_name属性用于给上下文变量取名（在模板中使用该名字）
    context_object_name = "home_index"
