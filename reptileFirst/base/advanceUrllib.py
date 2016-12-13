#coding=utf-8

import urllib
import urllib2


# 'http://www.test.we.com/loginPage.action'
# {"username": '18312341234', "password": "111111"}
url = 'http://www.test.we.com/loginPage.action'
values = {"username": '18312341234', "password": "111111"}
data = urllib.urlencode(values)
request = urllib2.Request(url, data)
try:
    response = urllib2.urlopen(request)
except urllib2.URLError,e:
    if hasattr(e, 'code'):
        print e.code
    if hasattr(e, 'reason'):
        print e.reason
else:
    print "OK"

print response.geturl()
print response.getcode()
print response.read()
print 'abc'

