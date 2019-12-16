from bs4 import BeautifulSoup

html = '''
    <div class="panel">
        <div class="panel-heading">
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-small" id="list-2">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
    '''
soup = BeautifulSoup(html, 'html.parser')


def title_select():
    print(soup.prettify())
    print(soup.title)
    print(soup.title.name)
    print(soup.title.parent.name)
    print(soup.p)
    print(soup.p["class"])
    print(soup.a)
    print(soup.find_all('a'))
    print(soup.find(id='link3'))

    for link in soup.find_all('a'):
        print(link.get('href'))

    print(soup.p.contents)
    print(soup.p.children)
    for i, child in enumerate(soup.p.children):
        print(i, child)

    print(soup.descendants)


def css_select():
    print(soup.select('.panel .panel-heading'))
    print(soup.select('ul li'))
    print(soup.select('#list-2 .element'))
    print(type(soup.select('ul')[0]))


def get_text():
    for li in soup.select('li'):
        print(li.get_text())


def get_attr():
    for ul in soup.select('ul'):
        print(ul['id'])
        print(ul.attrs['id'])


if __name__ == "__main__":
    get_attr()
