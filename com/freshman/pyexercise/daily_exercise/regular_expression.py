import re

import requests


def base_regular_match():
    content = "hello 123 4567 World_This is a regex Demo"
    result = re.match('^hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$', content)
    print(result)
    print(result.group())
    print(result.span())


def base_regular_search():
    content = "extra things hello 123455 world_this is a Re Extra things"

    result = re.search("hello.*?(\d+).*?Re", content)
    print(result)
    print(result.group())
    print(result.group(1))


def regular_douban():
    content = requests.get('https://book.douban.com/').text
    pattern = re.compile(
        '<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',
        re.S)
    results = re.findall(pattern, content)
    print(results)

    for result in results:
        url, name, author, date = result
        author = re.sub('\s', '', author)
        date = re.sub('\s', '', date)
        print(url, name, author, date)
