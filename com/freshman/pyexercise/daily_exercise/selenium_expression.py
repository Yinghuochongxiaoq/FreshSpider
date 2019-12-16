from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

web_driver_file_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(web_driver_file_path)


def search_single_element():
    browser.get("http://www.taobao.com")
    input_first = browser.find_element_by_id("q")
    input_second = browser.find_element_by_css_selector("#q")
    input_third = browser.find_element_by_xpath('//*[@id="q"]')
    print(input_first)
    print(input_second)
    print(input_third)
    input_first = browser.find_element(By.ID, "q")
    print(input_first)
    browser.close()


def element_do_something():
    import time
    browser.get("http://www.taobao.com")
    input_str = browser.find_element_by_id('q')
    input_str.send_keys('ipad')
    time.sleep(1)
    input_str.clear()
    input_str.send_keys('MakBook pro')
    button = browser.find_element_by_class_name('btn-search')
    button.click()


def element_action():
    from selenium.webdriver import ActionChains
    url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    source = browser.find_element_by_css_selector('#draggable')
    target = browser.find_element_by_css_selector('#droppable')
    actions = ActionChains(browser)
    actions.drag_and_drop(source, target)
    actions.perform()


def execute_javascripte():
    browser.get("http://www.zhihu.com/explore")
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    browser.execute_script('alert("到底了")')
    logo = browser.find_element_by_id('zh-top-link-logo')
    print(logo)
    print(logo.get_attribute('class'))


def switch_frame():
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    source = browser.find_element_by_css_selector('#draggable')
    print(source)
    try:
        logo = browser.find_element_by_class_name('logo')
    except NoSuchElementException:
        print('No logo')
    browser.switch_to.parent_frame()
    logo = browser.find_element_by_class_name('logo')
    print(logo)
    print(logo.text)


def implicitly_wait():
    browser.implicitly_wait(10)
    browser.get("https://www.zhihu.com/explore")
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input)


def show_wait():
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    browser.get("http://www.taobao.com")
    wait = WebDriverWait(browser, 10)
    input = wait.until(EC.presence_of_all_elements_located((By.ID, 'q')))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
    print(input, button)


def back_forward():
    browser.get('https://www.baidu.com')
    browser.get('https://www.taobao.com')
    browser.get('https://www.python.org')
    browser.back()
    browser.forward()
    browser.close()


def cookies_action():
    browser.get("http://zhihu.com/explore")
    print(browser.get_cookies())
    browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'zhaofan'})
    print(browser.get_cookies())
    browser.delete_all_cookies()
    print(browser.get_cookies())


def new_table_open():
    import time
    browser.get('https://www.baidu.com')
    browser.execute_script('window.open()')
    print(browser.window_handles)
    browser.switch_to.window(browser.window_handles[1])
    browser.get('https://www.taobao.com')
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[0])
    browser.get('https://python.org')


if __name__ == "__main__":
    new_table_open()
