import requests

def getpayloads():
    payloads = [{'path': '/config.inc', 'tag': '', 'content-type': '', 'content-type_no': 'html'},
    {'path': '/config.php.bak', 'tag': '', 'content-type': 'application/octet-stream',
     'content-type_no': ''},
    {'path': '/db.php.bak', 'tag': '', 'content-type': 'application/octet-stream',
     'content-type_no': ''},
    {'path': '/conf/config.ini', 'tag': '[', 'content-type': '', 'content-type_no': 'html'},
    {'path': '/config.ini', 'tag': '[', 'content-type': '', 'content-type_no': 'html'},
    {'path': '/config/config.ini', 'tag': '[', 'content-type': '', 'content-type_no': 'html'},
    {'path': '/configuration.ini', 'tag': '[', 'content-type': '', 'content-type_no': 'html'},
    {'path': '/configs/application.ini', 'tag': '[', 'content-type': '', 'content-type_no': 'html'},
    {'path': '/settings.ini', 'tag': '[', 'content-type': '', 'content-type_no': 'html'},
    {'path': '/application.ini', 'tag': '[', 'content-type': '', 'content-type_no': 'html'},
    {'path': '/conf.ini', 'tag': '[', 'content-type': '', 'content-type_no': 'html'},
    {'path': '/app.ini', 'tag': '[', 'content-type': '', 'content-type_no': 'html'},
    {'path': '/config.json', 'tag': '', 'content-type': 'application/json', 'content-type_no': ''},
    {'path': '/a.out', 'tag': '', 'content-type': '', 'content-type_no': 'html'},
    {'path': '/key', 'tag': '', 'content-type': '', 'content-type_no': 'html'},
    {'path': '/keys', 'tag': '', 'content-type': '', 'content-type_no': 'html'},
    {'path': '/key.txt', 'tag': '', 'content-type': 'text/plain', 'content-type_no': ''},
    {'path': '/temp.txt', 'tag': '', 'content-type': 'text/plain', 'content-type_no': ''},
    {'path': '/tmp.txt', 'tag': '', 'content-type': 'text/plain', 'content-type_no': ''},
    {'path': '/php.ini', 'tag': '[', 'content-type': '', 'content-type_no': 'html'},
    {'path': '/sftp-config.json', 'tag': 'password', 'content-type': 'application/json',
     'content-type_no': ''},
    {'path': '/index.php.bak', 'tag': '<?php', 'content-type': 'application/octet-stream',
     'content-type_no': ''},
    {'path': '/.index.php.swp', 'tag': '<?php', 'content-type': 'application/octet-stream',
     'content-type_no': ''},
    {'path': '/index.cgi.bak', 'tag': '', 'content-type': 'application/octet-stream',
     'content-type_no': ''},
    {'path': '/config.inc.php.bak', 'tag': '<?php', 'content-type': 'application/octet-stream',
     'content-type_no': ''},
    {'path': '/.config.inc.php.swp', 'tag': '<?php', 'content-type': 'application/octet-stream',
     'content-type_no': ''},
    {'path': '/config/.config.php.swp', 'tag': '<?php', 'content-type': '', 'content-type_no': ''},
    {'path': '/.config.php.swp', 'tag': '<?php', 'content-type': '', 'content-type_no': ''},
    {'path': '/.settings.php.swp', 'tag': '<?php', 'content-type': 'application/octet-stream',
     'content-type_no': ''},
    {'path': '/.database.php.swp', 'tag': '<?php', 'content-type': 'application/octet-stream',
     'content-type_no': ''},
    {'path': '/.db.php.swp', 'tag': '<?php', 'content-type': 'application/octet-stream',
     'content-type_no': ''},
    {'path': '/.mysql.php.swp', 'tag': '<?php', 'content-type': 'application/octet-stream',
     'content-type_no': ''},
    {'path': '/readme', 'tag': '', 'content-type': '', 'content-type_no': 'html'},
    {'path': '/README', 'tag': '', 'content-type': '', 'content-type_no': 'html'},
    {'path': '/readme.md', 'tag': '', 'content-type': '', 'content-type_no': 'html'},
    {'path': '/changelog.txt', 'tag': '', 'content-type': 'text/plain', 'content-type_no': ''},
    {'path': '/%e6%9b%b4%e6%96%b0%e6%97%a5%e5%bf%97.txt', 'tag': '', 'content-type': 'text/plain',
     'content-type_no': ''},
    {'path': '/www.log', 'tag': '', 'content-type': 'text/plain', 'content-type_no': ''},
    {'path': '/error.log', 'tag': '', 'content-type': 'text/plain', 'content-type_no': ''},
    {'path': '/log.log', 'tag': '', 'content-type': 'text/plain', 'content-type_no': ''},
    {'path': '/sql.log', 'tag': '', 'content-type': 'text/plain', 'content-type_no': ''},
    {'path': '/errors.log', 'tag': '', 'content-type': 'text/plain', 'content-type_no': ''},
    {'path': '/db.log', 'tag': '', 'content-type': 'text/plain', 'content-type_no': ''},
    {'path': '/data.log', 'tag': '', 'content-type': 'text/plain', 'content-type_no': ''},
    {'path': '/app.log', 'tag': '', 'content-type': 'text/plain', 'content-type_no': ''},
    {'path': '/ntunnel_mysql.php', 'tag': 'Navicat HTTP Tunnel Tester', 'content-type': 'text/html',
     'content-type_no': ''},
    ]
    return payloads

def poc(url):
    if '://' not in url:
        url = 'http://' + url
    if not url.endswith('/'):
        url = url + "/"
    url = url.rstrip("/")
    payloads = getpayloads()
    result = {}
    rel = []
    header = dict()
    header["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    for payload in payloads:
        test_url = url + payload["path"]
        try:
            r = requests.get(test_url, headers=header,allow_redirects=False)
        except Exception:
            continue
        if r.status_code != 200:
            continue
        if payload["tag"]:
            if payload["tag"] not in r.text:
                continue
        if payload["content-type"]:
            if payload['content-type'] not in r.headers.get('Content-Type', ''):
                continue
        if payload["content-type_no"]:
            if payload["content-type_no"] in r.headers.get('Content-Type', ''):
                continue
        length = str(len(r.text))
        if length not in result:
            result[length] = []
        result[length].append(test_url)
    for k,v in result.items():
        if len(v) > 5:
            continue
        for i in v:
            rel.append("[filescan]  " + i + "  length:" + k)
    if rel:
        return rel

