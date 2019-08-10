import requests

def getpayloads():
    payloads = [{'path': '/core', 'tag': 'ELF', 'content-type': '', 'content-type_no': ''},
                    {'path': '/crossdomain.xml', 'tag': '<allow-access-from domain="*"', 'content-type': 'xml',
                     'content-type_no': ''},
                    {'path': '/debug.txt', 'tag': '', 'content-type': 'text/plain', 'content-type_no': ''},
                    {'path': '/.htaccess', 'tag': '', 'content-type': 'application/octet-stream',
                     'content-type_no': ''},
                    {'path': '/htaccess.bak', 'tag': '', 'content-type': 'application/octet-stream',
                     'content-type_no': ''},
                    {'path': '/.htpasswd', 'tag': '', 'content-type': 'application/octet-stream',
                     'content-type_no': ''},
                    {'path': '/.htpasswd.bak', 'tag': '', 'content-type': 'application/octet-stream',
                     'content-type_no': ''},
                    {'path': '/htpasswd.bak', 'tag': '', 'content-type': 'application/octet-stream',
                     'content-type_no': ''},
                    {'path': '/.mysql_history', 'tag': '', 'content-type': 'application/octet-stream',
                     'content-type_no': ''},
                    {'path': '/httpd.conf', 'tag': '', 'content-type': '', 'content-type_no': 'html'},
                    {'path': '/web.config', 'tag': '', 'content-type': 'application/octet-stream',
                     'content-type_no': ''},
                    {'path': '/server-status', 'tag': '<title>Apache Status</title>', 'content-type': '',
                     'content-type_no': ''},
                    {'path': '/solr/', 'tag': '<title>Solr Admin</title>', 'content-type': 'html',
                     'content-type_no': ''},
                    {'path': '/examples/', 'tag': '<TITLE>Apache Tomcat Examples</TITLE>', 'content-type': 'html',
                     'content-type_no': ''},
                    {'path': '/examples/servlets/servlet/SessionExample', 'tag': '<title>Sessions Example</title>',
                     'content-type': 'html', 'content-type_no': ''},
                    {'path': '/config/database.yml', 'tag': 'password', 'content-type': '', 'content-type_no': 'html'},
                    {'path': '/database.yml', 'tag': '', 'content-type': '', 'content-type_no': 'html'},
                    {'path': '/db.conf', 'tag': '', 'content-type': '', 'content-type_no': 'html'},
                    {'path': '/db.ini', 'tag': '[', 'content-type': '', 'content-type_no': 'html'},
                    {'path': '/jmx-console/HtmlAdaptor', 'tag': 'JBoss Management Console', 'content-type': '',
                     'content-type_no': ''},
                    {'path': '/cacti/', 'tag': '<title>Login to Cacti</title>', 'content-type': '',
                     'content-type_no': ''},
                    {'path': '/zabbix/', 'tag': '<title>Zabbix</title>', 'content-type': '', 'content-type_no': ''},
                    {'path': '/jenkins/static/f3a41d2f/css/style.css', 'tag': 'jenkins-home-link',
                     'content-type': 'text/css', 'content-type_no': ''},
                    {'path': '/static/f3a41d2f/css/style.css', 'tag': 'jenkins-home-link', 'content-type': 'text/css',
                     'content-type_no': ''},
                    {'path': '/script', 'tag': 'Type in an arbitrary', 'content-type': '', 'content-type_no': ''},
                    {'path': '/jenkins/script', 'tag': 'Type in an arbitrary', 'content-type': '',
                     'content-type_no': ''},
                    {'path': '/exit', 'tag': '<title>POST required</title>', 'content-type': '', 'content-type_no': ''},
                    {'path': '/memadmin/index.php', 'tag': '<title>Login - MemAdmin', 'content-type': '',
                     'content-type_no': ''},
                    {'path': '/phpmyadmin/index.php', 'tag': '<title>phpMyAdmin', 'content-type': '',
                     'content-type_no': ''},
                    {'path': '/phpMyAdmin/index.php', 'tag': '<title>phpMyAdmin', 'content-type': '',
                     'content-type_no': ''},
                    {'path': '/_phpmyadmin/index.php', 'tag': '<title>phpMyAdmin', 'content-type': '',
                     'content-type_no': ''},
                    {'path': '/pma/index.php', 'tag': '<title>phpMyAdmin', 'content-type': '', 'content-type_no': ''},
                    {'path': '/ganglia/', 'tag': '<title>Ganglia', 'content-type': '', 'content-type_no': ''},
                    {'path': '/resin-doc/resource/tutorial/jndi-appconfig/test?inputFile=/etc/profile',
                     'tag': '/etc/profile.d/*.sh', 'content-type': '', 'content-type_no': ''},
                    {'path': '/resin-doc/viewfile/?contextpath=/&servletpath=&file=index.jsp',
                     'tag': 'This is the default start page for the Resin server', 'content-type': '',
                     'content-type_no': ''},
                    {'path': '/resin-admin/', 'tag': '<title>Resin Admin Login for', 'content-type': '',
                     'content-type_no': ''},
                    {'path': '/data.txt', 'tag': '', 'content-type': 'text/plain', 'content-type_no': ''},
                    {'path': '/install.txt', 'tag': '', 'content-type': 'text/plain', 'content-type_no': ''},
                    {'path': '/INSTALL.TXT', 'tag': '', 'content-type': 'text/plain', 'content-type_no': ''},
                    {'path': '/upload.do', 'tag': 'type="file"', 'content-type': 'html', 'content-type_no': ''},
                    {'path': '/upload.jsp', 'tag': 'type="file"', 'content-type': 'html', 'content-type_no': ''},
                    {'path': '/upload.php', 'tag': 'type="file"', 'content-type': 'html', 'content-type_no': ''},
                    {'path': '/upfile.php', 'tag': 'type="file"', 'content-type': 'html', 'content-type_no': ''},
                    {'path': '/upload.html', 'tag': 'type="file"', 'content-type': 'html', 'content-type_no': ''}]
    if 1 == 1:
        temp = [
            {'path': '/.bash_history', 'tag': '', 'content-type': 'application/octet-stream',
                'content-type_no': ''},
            {'path': '/.rediscli_history', 'tag': '', 'content-type': 'application/octet-stream',
                'content-type_no': ''},
            {'path': '/.bashrc', 'tag': '', 'content-type': 'application/octet-stream', 'content-type_no': ''},
            {'path': '/.bash_profile', 'tag': '', 'content-type': 'application/octet-stream',
                'content-type_no': ''},
            {'path': '/.bash_logout', 'tag': '', 'content-type': 'application/octet-stream',
                'content-type_no': ''},
            {'path': '/.vimrc', 'tag': '', 'content-type': 'application/octet-stream', 'content-type_no': ''},
            {'path': '/.DS_Store', 'tag': '', 'content-type': 'application/octet-stream',
                'content-type_no': ''},
            {'path': '/.history', 'tag': '', 'content-type': 'application/octet-stream', 'content-type_no': ''},
            {'path': '/nohup.out', 'tag': '', 'content-type': 'application/octet-stream',
                'content-type_no': ''},
            {'path': '/.ssh/known_hosts', 'tag': '', 'content-type': 'application/octet-stream',
                'content-type_no': ''},
            {'path': '/.ssh/id_rsa', 'tag': 'PRIVATE KEY-', 'content-type': '', 'content-type_no': ''},
            {'path': '/id_rsa', 'tag': 'PRIVATE KEY-', 'content-type': '', 'content-type_no': ''},
            {'path': '/.ssh/id_rsa.pub', 'tag': 'ssh-rsa', 'content-type': '', 'content-type_no': ''},
            {'path': '/.ssh/id_dsa', 'tag': 'PRIVATE KEY-', 'content-type': '', 'content-type_no': ''},
            {'path': '/id_dsa', 'tag': 'PRIVATE KEY-', 'content-type': '', 'content-type_no': ''},
            {'path': '/.ssh/id_dsa.pub', 'tag': 'ssh-dss', 'content-type': '', 'content-type_no': ''},
            {'path': '/.ssh/authorized_keys', 'tag': 'ssh-rsa', 'content-type': '', 'content-type_no': ''},
        ]
        payloads.extend(temp)
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
        length = str(len(r.text))
        if length not in result:
            result[length] = []
        result[length].append(test_url)
    for k,v in result.items():
        if len(v) >= 3:
            continue
        for i in v:
            rel.append("[common set]  " + i + "  length:" + k)
    if rel:
        return rel

