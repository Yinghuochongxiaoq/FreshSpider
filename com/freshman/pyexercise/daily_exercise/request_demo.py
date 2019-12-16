import urllib.request
import socket
import urllib.error
import urllib.parse
import http.cookiejar
from urllib.parse import urlparse
from urllib.parse import urlunparse


def urllibrequesturl():
    url = "https://www.baidu.com/index.html;user?id=5#comment"

    dict = {
        "name": "zhaofan"
    }

    data = bytes(urllib.parse.urlencode(dict), encoding='utf8')

    try:

        '''添加请求头的第一种方式 Start'''
        headers = {
            "User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)", "Host": "baidu.com"
        }
        request = urllib.request.Request(url=url, data=data, headers=headers, method="GET")
        '''添加请求头的第一种方式 End'''

        '''添加请求头的第二种方式 Start'''
        # request.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
        '''添加请求头的第二种方式 End'''

        response = urllib.request.urlopen(request)
        print(response.read())
    except urllib.error.URLError as e:
        print(e.reason + "超时")

    try:

        '''设置代理 Start'''
        proxy_handler = urllib.request.ProxyHandler({
            'http': 'http://127.0.0.1:9734',
            'https': 'https://127.0.0.1:9734'
        })
        opener = urllib.request.build_opener(proxy_handler)
        response = opener.open('http://www.baidu.com')
        print(response.read())
        '''设置代理 End'''
    except urllib.error.HTTPError as e:
        print(e.reason)
        print(e.code)
        print(e.headers)
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print("time out")
        print(e.reason)

    '''http.cookiejar.MozillaCookieJar()方式 Start'''
    try:

        filename = 'cookie.txt'
        cookie = http.cookiejar.MozillaCookieJar(filename)
        handler = urllib.request.HTTPCookieProcessor(cookie)
        opener = urllib.request.build_opener(handler)
        response = opener.open(url)
        cookie.save(ignore_discard=True, ignore_expires=True)
    except urllib.error.URLError as e:
        print(e.reason)
    '''http.cookiejar.MozillaCookieJar()方式 End'''

    '''http.cookiejar.LWPCookieJar()方式 Start'''
    try:
        cookie = http.cookiejar.LWPCookieJar(filename)
        handler = urllib.request.HTTPCookieProcessor(cookie)
        opener = urllib.request.build_opener(handler)
        response = opener.open(url)
        cookie.save(ignore_expires=True, ignore_discard=True)
    except urllib.error.URLError as e:
        print(e.reason)
    '''http.cookiejar.LWPCookieJar()方式 End'''

    '''urlparse Start'''
    result = urlparse(url)
    print(result)
    '''urlparse End'''

    '''urlunparse Start'''
    data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=123', 'commit']
    print(urlunparse(data))
    '''urlunparse End'''

    '''urlencode将字典转换为url参数 Start'''
    params = {
        "name": "zhangshanfeng",
        "age": 123
    }
    base_url = "http://www.baidu.com?"
    url = base_url + urllib.parse.urlencode(params)
    print(url)
    '''urlencode将字典转换为url参数 End'''
