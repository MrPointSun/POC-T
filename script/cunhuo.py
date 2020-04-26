#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = w8ay
import requests
import re
import urlparse


def poc(url):
    if "." not in url:
        return False
    if '://' not in url:
        url = 'http://' + url
    if not url.endswith('/'):
        url = url + "/"
    
    try:
        header = dict()
        header["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        header["Referer"] = url
        r = requests.get(url, headers=header, timeout=20)
        if r.status_code == 200:
            parse = urlparse.urlparse(r.url)
            new_url = "%s://%s/" % (parse.scheme,parse.netloc)
            return new_url
        else:
            return False
    except Exception:
        return False

# print poc("http://virtual.glxy.sdu.edu.cn/")