import requests

def getpayloads():
    payloads = [{'path': '/WEB-INF/web.xml', 'tag': '<?xml', 'content-type': 'xml', 'content-type_no': ''},
    {'path': '/WEB-INF/web.xml.bak', 'tag': '<?xml', 'content-type': '', 'content-type_no': ''},
    {'path': '/WEB-INF/applicationContext.xml', 'tag': '<?xml', 'content-type': 'xml',
     'content-type_no': ''},
    {'path': '/WEB-INF/config.xml', 'tag': '<?xml', 'content-type': 'xml', 'content-type_no': ''},
    {'path': '/WEB-INF/spring.xml', 'tag': '<?xml', 'content-type': 'xml', 'content-type_no': ''},
    {'path': '/WEB-INF/struts-config.xml', 'tag': '<?xml', 'content-type': 'xml',
     'content-type_no': ''},
    {'path': '/WEB-INF/struts-front-config.xml', 'tag': '<?xml', 'content-type': 'xml',
     'content-type_no': ''},
    {'path': '/WEB-INF/struts/struts-config.xml', 'tag': '<?xml', 'content-type': 'xml',
     'content-type_no': ''},
    {'path': '/WEB-INF/classes/spring.xml', 'tag': '<?xml', 'content-type': 'xml',
     'content-type_no': ''},
    {'path': '/WEB-INF/classes/struts.xml', 'tag': '<?xml', 'content-type': 'xml',
     'content-type_no': ''},
    {'path': '/WEB-INF/classes/struts_manager.xml', 'tag': '<?xml', 'content-type': 'xml',
     'content-type_no': ''},
    {'path': '/WEB-INF/classes/conf/datasource.xml', 'tag': '<?xml', 'content-type': 'xml',
     'content-type_no': ''},
    {'path': '/WEB-INF/classes/data.xml', 'tag': '<?xml', 'content-type': 'xml', 'content-type_no': ''},
    {'path': '/WEB-INF/classes/config/applicationContext.xml', 'tag': '<?xml', 'content-type': 'xml',
     'content-type_no': ''},
    {'path': '/WEB-INF/classes/applicationContext.xml', 'tag': '<?xml', 'content-type': 'xml',
     'content-type_no': ''},
    {'path': '/WEB-INF/classes/conf/spring/applicationContext-datasource.xml', 'tag': '<?xml',
     'content-type': 'xml', 'content-type_no': ''},
    {'path': '/WEB-INF/config/db/dataSource.xml', 'tag': '<?xml', 'content-type': 'xml',
     'content-type_no': ''},
    {'path': '/WEB-INF/spring-cfg/applicationContext.xml', 'tag': '<?xml', 'content-type': 'xml',
     'content-type_no': ''},
    {'path': '/WEB-INF/dwr.xml', 'tag': '<?xml', 'content-type': 'xml', 'content-type_no': ''},
    {'path': '/WEB-INF/classes/hibernate.cfg.xml', 'tag': '<?xml', 'content-type': 'xml',
     'content-type_no': ''},
    {'path': '/WEB-INF/classes/rabbitmq.xml', 'tag': '<?xml', 'content-type': 'xml',
     'content-type_no': ''},
    {'path': '/WEB-INF/conf/activemq.xml', 'tag': '<?xml', 'content-type': 'xml',
     'content-type_no': ''},
    {'path': '/server.xml', 'tag': '<?xml', 'content-type': 'xml', 'content-type_no': ''},
    {'path': '/config/database.yml', 'tag': '', 'content-type': '', 'content-type_no': 'html'},
    {'path': '/configprops', 'tag': 'serverProperties', 'content-type': '', 'content-type_no': ''},
    {'path': '/WEB-INF/database.properties', 'tag': '', 'content-type': '', 'content-type_no': 'html'},
    {'path': '/WEB-INF/web.properties', 'tag': '', 'content-type': '', 'content-type_no': 'html'},
    {'path': '/WEB-INF/log4j.properties', 'tag': '', 'content-type': '', 'content-type_no': 'html'},
    {'path': '/WEB-INF/classes/dataBase.properties', 'tag': '', 'content-type': '',
     'content-type_no': 'html'},
    {'path': '/WEB-INF/classes/application.properties', 'tag': '', 'content-type': '',
     'content-type_no': 'html'},
    {'path': '/WEB-INF/classes/jdbc.properties', 'tag': '', 'content-type': '',
     'content-type_no': 'html'},
    {'path': '/WEB-INF/classes/db.properties', 'tag': '', 'content-type': '',
     'content-type_no': 'html'},
    {'path': '/WEB-INF/classes/conf/jdbc.properties', 'tag': '', 'content-type': '',
     'content-type_no': 'html'},
    {'path': '/WEB-INF/classes/security.properties', 'tag': '', 'content-type': '',
     'content-type_no': 'html'},
    {'path': '/WEB-INF/conf/database_config.properties', 'tag': '', 'content-type': '',
     'content-type_no': 'html'},
    {'path': '/WEB-INF/config/dbconfig', 'tag': 'passw', 'content-type': '', 'content-type_no': 'html'}]
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
        result.append("[java web]  " + test_url)
    if result and len(result) < 5:
        return result

