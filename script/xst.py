#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/POC-T
# author = i@cdxy.me

"""
测试用例
"""

import random
import time
import urlparse
import requests

def poc(url):
    if "." not in url:
        return False
    if '://' not in url:
        url = 'http://' + url
    if not url.endswith('/'):
        url = url + "/"
    payload = url
    header = dict()
    header["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    header["Referer"] = url
    header["fuck"] = "HelloWOrld"
    try:
        resp = requests.get(payload,headers=header,timeout=15)
    except Exception:
        return False
    if 'fuck' in resp.headers:
        print("[xst]:" + payload)
    parse = urlparse.urlparse(url)
    new_url = "%s://%s/" % (parse.scheme,parse.netloc)
    return new_url
