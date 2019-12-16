import requests
from requests import RequestException


def baserequests():
    """requests基础信息"""
    url = 'https://www.baidu.com'
    response = requests.get(url)
    print(type(response))
    print(response.status_code)
    print(type(response.text))
    print(response.text)
    print(response.cookies)
    print(response.content)
    print(response.content.decode('utf-8'))


def requestsencoding():
    """编码"""
    response = requests.get("https://www.baidu.com")
    response.encoding = "utf-8"
    print(response.text)

    requests.post("http://httpbin.org/post")
    requests.put("http://httpbin.org/put")
    requests.delete("http://httpbin.org/delete")
    requests.head("http://httpbin.org/get")
    requests.options("http://httpbin.org/get")


def requestswithparam():
    """带参数的请求"""
    data = {
        "name": "zhaofan",
        "age": 22
    }
    response = requests.get("http://httpbin.org/get", params=data)
    print(response.url)
    print(response.text)


def requestsgetjson():
    """获取json数据"""
    import json

    response = requests.get("http://httpbin.org/get")
    print(type(response.text))
    print(response.json())
    print(json.loads(response.text))
    print(type(response.json()))


def requestszhihu():
    """获取知乎的内容"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get('https://www.zhihu.com', headers=headers)
    print(response.text)


def requestspost():
    data = {
        "name": "zhaofan",
        "age": 23
    }
    response = requests.post("http://httpbin.org/post", data=data)
    print(response.text)
    if response.status_code == requests.codes.ok:
        print("访问成功")


def postfile():
    files = {"files": open("git.jpg", "rb")}
    response = requests.post("http://httpbin.org/post", files=files)
    print(response.text)


def getcookie():
    response = requests.get("https://www.baidu.com")
    print(response.cookies)
    for key, values in response.cookies.items():
        print(key + "=" + values)


def get_session():
    s = requests.session()
    s.get("http://httpbin.org/cookies/set/number/123456")
    response = s.get("http://httpbin.org/cookies")
    print(response.text)


def certificate():
    """删除这句会出现警告信息，如果网站证书过期"""
    requests.packages.urllib3.disable_warnings()
    # verify=False才能访问证书过期的网站
    response = requests.get("https://www.12306.cn", verify=False)
    print(response.status_code)


def base_auth():
    from requests.auth import HTTPBasicAuth
    try:
        response = requests.get("http://120.27.34.24:9001/", auth=HTTPBasicAuth("user", "123"), timeout=10)
        print(response.status_code)
    except requests.exceptions.ConnectTimeout as e:
        print(e)
    except ConnectionError:
        print("连接异常")
    except RequestException:
        print("Error")

base_auth()
