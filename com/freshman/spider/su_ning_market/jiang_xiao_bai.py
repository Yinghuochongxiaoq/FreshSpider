import re

from selenium import webdriver
import time

web_driver_file_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(web_driver_file_path)
# browser.maximize_window()
browser.set_window_size(890, 820)


def do_action():
    """进入首页"""
    home_url = "https://jiangxiaobai.suning.com/?pcode=10059791965"
    browser.get(home_url)

    all_href = browser.find_elements_by_xpath("//a")
    # 存储所有访问过的记录
    visit_history_dic = {}
    # 产品地址前缀
    product_pre = 'product.suning.com'
    # 计算器
    product_number = 0
    if all_href is None:
        print("没有找到任何的a标签")
        browser.close()
    for url in all_href:
        action_url = None
        try:
            action_url = url.get_attribute("href")
        except Exception as e:
            print(e)
        if action_url is None or action_url == '':
            continue
        if not (action_url in visit_history_dic):
            visit_history_dic[action_url] = action_url
            if product_pre in action_url:
                product_number += 1
                print("处理第" + str(product_number) + "个当前链接：" + action_url)
                try:
                    new_table_open(action_url)
                except Exception as e:
                    print("\t出现异常：" + e)

    browser.close()
    return


def new_table_open(new_url):
    """打开新的窗口处理"""
    browser.execute_script('window.open()')
    browser.switch_to.window(browser.window_handles[1])
    browser.get(new_url)

    # # 到底部
    # js_scroll_to_bottom = "window.scrollTo(0, document.body.scrollHeight);"
    # browser.execute_script(js_scroll_to_bottom)
    # time.sleep(0.5)
    # # 回顶部
    # js_scroll_to_bottom = "window.scrollTo(0, 0);"
    # browser.execute_script(js_scroll_to_bottom)
    # time.sleep(0.5)

    # 判断产品是否存在
    try:
        element_404 = browser.find_elements_by_class_name("search404")
        if element_404 is not None and len(element_404) > 0:
            print("\t很抱歉,此商品不存在!")
            # 关闭当前页面
            browser.close()
            # 切换回到首页地址
            browser.switch_to.window(browser.window_handles[0])
            return
        element_under_shelf = browser.find_elements_by_class_name("txt-under-shelf")
        if element_under_shelf is not None and len(element_under_shelf) and element_under_shelf[0].is_displayed():
            print("\t" + element_under_shelf[0].text)
            # 关闭当前页面
            browser.close()
            # 切换回到首页地址
            browser.switch_to.window(browser.window_handles[0])
            return
    except Exception:
        pass
    # 获取标题
    display_name = browser.find_element_by_id("itemDisplayName")
    print("\t产品名称：" + display_name.text)
    # 获取价格
    main_price = browser.find_element_by_class_name("mainprice")
    print("\t价格：" + main_price.text)
    button = browser.find_element_by_id('productCommTitle')
    button.click()

    # 休眠半秒钟，等待浏览器加载
    element_comment_total = None
    time.sleep(1)
    for i in range(1, 3):
        try:
            element_comment_total = browser.find_element_by_xpath("//div[@id='rv-main']/div/div/ul/li/a/p/span")
            break
        except Exception:
            time.sleep(0.5)
    if element_comment_total is None:
        print("\t加载评论超时")
        # 关闭当前页面
        browser.close()
        # 切换回到首页地址
        browser.switch_to.window(browser.window_handles[0])
        return
    comp = re.compile('-?[1-9]\d*')
    match = comp.search(element_comment_total.text)
    if match:
        print("\t评价总数：" + match.group(0) + "条")
    else:
        print("\t评价总数：0条")

    # 关闭当前页面
    browser.close()
    # 切换回到首页地址
    browser.switch_to.window(browser.window_handles[0])


if __name__ == "__main__":
    do_action()
