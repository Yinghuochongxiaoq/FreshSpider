from pyquery import PyQuery

html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
</div>
'''


# 初始化的时候一般有三种传入方式：传入字符串，传入url，传入文件
def init_pyquery_html():
    doc = PyQuery(html)
    print(doc)
    print(type(doc))
    print(doc('li'))


def init_pyquery_url():
    doc = PyQuery(url="https://www.baidu.com", encoding="utf-8")
    print(doc('head'))


def css_select():
    doc = PyQuery(html)
    print(doc('#container .list li'))


def find_children():
    doc = PyQuery(html)
    items = doc('.list')
    print(type(items))
    print(items)
    li = items.find('li')
    print(type(li))
    print(li)
    li2 = items.children('.active')
    print(li2)


def find_parent():
    doc = PyQuery(html)
    items = doc('.list')
    parent = items.parents()
    print(type(parent))
    print(parent)


def find_siblings():
    doc = PyQuery(html)
    lis = doc('.list .item-0.active')
    print(lis.siblings())
    for li in lis:
        print(type(li))
        print(li)


def single_for():
    doc = PyQuery(html)
    lis = doc('li').items()
    for li in lis:
        print(type(li))
        print(li)


def get_attr():
    doc = PyQuery(html)
    a = doc('.item-0.active a')
    print(a)
    print(a.text())
    print(a.attr('href'))
    print(a.attr.href)

    b = doc('.item-0.active')
    print(b)
    print(b.html())


def remove_html():
    html = '''
    <div class="wrap">
        Hello, World
        <p>This is a paragraph.</p>
     </div>
    '''
    from pyquery import PyQuery as pq
    doc = pq(html)
    wrap = doc('.wrap')
    print(wrap.text())
    wrap.find('p').remove()
    print(wrap.text())


if __name__ == "__main__":
    remove_html()
