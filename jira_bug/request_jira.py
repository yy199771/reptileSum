#coding=utf-8

import requests
import re

endpoit = {'os_username': '*******', 'os_password': '********'}
BaseUrl_login = 'http://172.16.3.139/rest/auth/1/session'


def basic_auth(endpoit=None):
    #s = requests.session()
    # login in jiranew.we.com
    r = requests.get('http://172.16.3.139/rest/auth/1/session', params=endpoit)
    #print r.text
    #print r.url
    #print r.headers['Set-Cookie']
    # 获取cookie
    jession_id = r.headers['Set-Cookie']
    #print jession_id

    # 处理JSESSIONID
    pattern = re.compile('JSESSIONID=.*?;')
    result1 = re.match(pattern, jession_id)
    str = result1.group()
    str_list = str.split(';')
    #print str_list[0]

    # 拼装headers。
    headers = {'cookie': str_list[0], 'Content-Type': 'application/json'}

    # 获取项目列表
    rr = requests.get('http://172.16.3.139/rest/api/2/project?id=10101', headers=headers)
    #print rr.text
    # 获取线上缺陷问题列表
    bug_list = requests.get('http://172.16.3.139/rest/api/2/search?jql=project=BUGSUPPORT&resolution=Unresolved', headers=headers)
    #print bug_list.text
    print bug_list.json()

    #print '\u6d4b\u8bd5\u8fc7\u7a0b\uff0c\u7ef4\u62a4\u8fc7\u7a0b\u53d1\u73b0\u5f71\u54cd\u7cfb\u7edf\u8fd0\u884c\u7684\u7f3a\u9677'.encode('utf-8')

    #resolution = Unresolved ORDER BY updated DESC
    #print s.get('http://172.16.3.139/rest/api/2/project')


def project_list():
    pass

basic_auth(endpoit)
#project_list()


