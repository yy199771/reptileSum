#coding=utf-8

import urllib2
import cookielib

'''
将cookie保存到了cookie这个变量中。
'''


# 声明一个cookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = urllib2.build_opener(handler)
# 此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = ' + item.name
    print 'Value = ' + item.value


'''
将cookie保存到文件中
FileCookieJar这个对象了，在这里我们使用它的子类MozillaCookieJar来实现Cookie的保存。

该模块主要的对象有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar。
它们的关系：CookieJar —-派生—->FileCookieJar  —-派生—–>MozillaCookieJar和LWPCookieJar
'''

# 设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件.
cookieTxt = cookielib.MozillaCookieJar(filename)
# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handlerTxt = urllib2.HTTPCookieProcessor(cookieTxt)
# 通过handler来构建opener
openerTxt = urllib2.build_opener(handlerTxt)
# 创建一个请求,原理同urllib2的urlopen
responseTxt = openerTxt.open('http://www.baidu.com')
# 保存cookie到文件
cookieTxt.save(ignore_discard=True, ignore_expires=True)


'''
从文件中读取cookie
'''
# 创建MozillaCookieJar实例对象
getCookie = cookielib.MozillaCookieJar()
# 从文件中读取cookie内容到变量
getCookie.load('cookie.txt', ignore_expires=True, ignore_discard=True)
# 创建request请求
req = urllib2.Request('http://wwww.baidu.com')
# 利用urllib2的build_opener方法创建一个opener
getOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(getCookie))
res = getOpener.open(req)

print res.read()
