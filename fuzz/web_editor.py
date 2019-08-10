import requests

def getpayloads():
    payloads = [{'path': '/fckeditor/_samples/default.html', 'tag': '<title>FCKeditor', 'content-type': 'html',
    'content-type_no': ''},
   {'path': '/ckeditor/samples/', 'tag': '<title>CKEditor Samples</title>', 'content-type': '',
    'content-type_no': ''},
   {'path': '/editor/ckeditor/samples/', 'tag': '<title>CKEditor Samples</title>', 'content-type': '',
    'content-type_no': ''},
   {'path': '/ckeditor/samples/sample_posteddata.php', 'tag': 'http://ckeditor.com</a>',
    'content-type': '', 'content-type_no': ''},
   {'path': '/editor/ckeditor/samples/sample_posteddata.php', 'tag': 'http://ckeditor.com</a>',
    'content-type': '', 'content-type_no': ''},
   {'path': '/fck/editor/dialog/fck_spellerpages/spellerpages/server-scripts/spellchecker.php',
    'tag': 'init_spell()', 'content-type': 'html', 'content-type_no': ''},
   {'path': '/fckeditor/editor/dialog/fck_spellerpages/spellerpages/server-scripts/spellcheckder.php',
    'tag': 'init_spell()', 'content-type': 'html', 'content-type_no': ''},
   {'path': '/ueditor/ueditor.config.js', 'tag': 'window.UEDITOR_HOME_URL', 'content-type': '',
    'content-type_no': ''},
   {'path': '/ueditor/php/getRemoteImage.php', 'tag': "'tip':'", 'content-type': '',
    'content-type_no': ''}]

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
        result.append("[web editor]  " + test_url)
    if result:
        return result

