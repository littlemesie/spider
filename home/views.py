# -*- coding: UTF-8 -*-
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello world ! ")
    context = {}
    context['hello'] = 'Hello World!123'
    return render(request, 'index.html', context)