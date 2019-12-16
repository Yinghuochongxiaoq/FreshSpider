import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor


def fetch_request(url):
    result = requests.get(url)
    # print(result.text)
    return result


def callback(future):
    print(future.result().text)


url_list = [
    'http://www.baidu.com',
    'http://www.bing.com',
    'http://www.sougou.com'
]

# 线程池
pool = ThreadPoolExecutor(10)
# 进程池
# pool = ProcessPoolExecutor(5)

for url in url_list:
    v = pool.submit(fetch_request, url)
    v.add_done_callback(callback)

pool.shutdown(True)
