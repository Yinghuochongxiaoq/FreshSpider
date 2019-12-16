import asyncio


@asyncio.coroutine
def func1():
    print('before ……func1……')
    # 这里必须用yield from，并且这里必须是asyncio.sleep不能是time.sleep
    yield from asyncio.sleep(2)
    print('end……func1……')


def asyncio_function():
    tasks = [func1(), func1()]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()


@asyncio.coroutine
def fetch_async(host, url='/'):
    print('----', host, url)
    reader, writer = yield from asyncio.open_connection(host, 80)

    # 构造请求头内容
    request_header_content = """GET %s HTTP/1.0\r\nHost: %s\r\n\r\n""" % (url, host,)
    request_header_content = bytes(request_header_content, encoding='utf-8')
    # 发送请求
    writer.write(request_header_content)
    yield from writer.drain()
    text = yield from reader.read()
    print(host, url, text)
    writer.close()


def fetch_async_task():
    tasks = [
        fetch_async('www.cnblogs.com', '/zhaof/'),
        fetch_async('dig.chouti.com', '/pic/show?nid=4073644713430508&lid=10273091')
    ]
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()


if __name__ == "__main__":
    asyncio_function()
