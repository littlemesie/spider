# -*- coding: utf-8 -*-
'''
    页面解析
'''
import urllib
import urllib2
import requests
import re
class ParseHtml():
    def get_html(self):
        headers = {
            "Host": "www.baidu.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
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
        return content

    con = get_html()
    print con