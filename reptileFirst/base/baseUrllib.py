#coding=utf-8

import urllib2
import urllib

#response = urllib2.urlopen("http://www.baidu.com")
#print response.read()


request = urllib2.Request('http://www.baidu.com')
response = urllib2.urlopen(request)
print '页面响应码:', response.getcode()
print '页面的URL:', response.geturl()
print '页面的信息:', response.info()
print '-----------------------------'
print response.read()




'''
# POST方式
values = {'username':'yy199771','password':'XXXXXXX'}
data = urllib.urlencode(values)
url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
#print response.read()

# GET方式
values={}
values['username'] = "yy199771"
values['password']="XXXXXXX"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print geturl
print response.read()
'''