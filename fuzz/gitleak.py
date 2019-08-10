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
    flag = {
            ".svn/all-wcprops": "svn:wc:ra_dav:version-url",
            ".git/config": 'repositoryformatversion[\s\S]*',
            ".bzr/README": 'This\sis\sa\sBazaar[\s\S]',
            'CVS/Root': ':pserver:[\s\S]*?:[\s\S]*',
            '.hg/requires': '^revlogv1.*'
    }
    for k,v in flag.items():
        vul_url = url + k
        try:
            header = dict()
            header["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
            r = requests.get(vul_url, headers=header)
            if re.search(v, r.text, re.I | re.S | re.M):
                return "[Leak]" + vul_url
        except Exception:
            pass
    return False
        