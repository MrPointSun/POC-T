import requests
import re

def poc(url):
    if '://' not in url:
        url = 'http://' + url
    if not url.endswith('/'):
        url = url + "/"
    url = url.rstrip("/")

    re_list = {
        "ASPNETPathDisclosure": "<title>Invalid\sfile\sname\sfor\smonitoring:\s'([^']*)'\.\sFile\snames\sfor\smonitoring\smust\shave\sabsolute\spaths\,\sand\sno\swildcards\.<\/title>",
        "Struts2DevMod": "You are seeing this page because development mode is enabled.  Development mode, or devMode, enables extra",
        "Django DEBUG MODEL": "You're seeing this error because you have <code>DEBUG = True<\/code> in",
        "RailsDevMode": "<title>Action Controller: Exception caught<\/title>",
        "RequiredParameter": "Required\s\w+\sparameter\s'([^']+?)'\sis\snot\spresent",
        "Thinkphp3 Debug": '<p class="face">:\(</p>'
    }

    header = dict()
    header["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    try:
        r = requests.get(url + "/habsavf12.jsp", headers=header)
    except Exception:
        return None
    for k, v in re_list.items():
        if re.search(v, r.text, re.S | re.I):
            return "[errorPage] %s : %s" % (url + "/habsavf12.jsp",k)

