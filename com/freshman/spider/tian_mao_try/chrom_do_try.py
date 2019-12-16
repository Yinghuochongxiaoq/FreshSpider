import random

from selenium import webdriver
import time

from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver import ActionChains

web_driver_file_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
mobile_emulation = {'deviceName': 'iPhone 8'}
options = webdriver.ChromeOptions()
options.add_experimental_option("mobileEmulation", mobile_emulation)
# browser = webdriver.Chrome(web_driver_file_path, chrome_options=options)
browser = webdriver.Chrome(web_driver_file_path)
browser.maximize_window()

tao_bao_user_name = "xxxx"
tao_bao_user_password = "xxxxxxxxx"


def show_mobile_login():
    """手机页面登录"""
    browser.get("https://login.m.taobao.com/login.htm?loginFrom=wap_tb")
    user_name = browser.find_element_by_name('TPL_username')
    pass_word = browser.find_element_by_name('TPL_password')
    if user_name is None:
        print("用户名输入框没有找到哦")
        return False
    if pass_word is None:
        print("密码输入框没有找到哦")
        return False
    user_name.send_keys(tao_bao_user_name)
    pass_word.send_keys(tao_bao_user_password)
    button = browser.find_element_by_id('submit-btn')
    button.click()
    return True


def show_black_login():
    """需要滑块验证"""
    browser.get("https://login.taobao.com/member/login.jhtml")
    switch_password = browser.find_element_by_id('J_Quick2Static')
    switch_password.click()
    user_name = browser.find_element_by_id('TPL_username_1')
    pass_word = browser.find_element_by_id('TPL_password_1')
    if user_name is None:
        print("用户名输入框没有找到哦")
        return False
    if pass_word is None:
        print("密码输入框没有找到哦")
        return False
    user_name.send_keys(tao_bao_user_name)
    pass_word.send_keys(tao_bao_user_password)
    # 处理滑块
    deal_black()
    button = browser.find_element_by_id('J_SubmitStatic')
    button.click()
    return True


def show_qc_image_login():
    """使用二维码扫描登录"""
    log_url = "https://login.taobao.com/member/login.jhtml"
    browser.get(log_url)
    while True:
        time.sleep(5)
        new_url = browser.current_url
        print(new_url)
        if new_url != log_url:
            break
    return True


def deal_black():
    """处理滑块"""
    while True:
        try:
            # 定位滑块元素
            source = browser.find_element_by_xpath("//*[@id='nc_1_n1z']")
            # 定义鼠标拖放动作
            # ActionChains(browser).drag_and_drop_by_offset(source, 258, 0).perform()
            action = ActionChains(browser)
            # 鼠标左键按下不放
            action.click_and_hold(source).perform()
            for index in range(400):
                try:
                    a = random.randint(6, 10)
                    b = random.randint(0, 5)
                    # 平行移动鼠标
                    action.move_by_offset(a, b).perform()
                except UnexpectedAlertPresentException:
                    print("拖动滑块失败~！")
                    action.reset_actions()
                    time.sleep(0.1)

            # 等待JS认证运行,如果不等待容易报错
            time.sleep(1)
            # 查看是否认证成功，获取text值

            text = browser.find_element_by_xpath("//div[@id='nc_1__scale_text']/span")
            # 目前只碰到3种情况：成功（请在在下方输入验证码,请点击图）；无响应（请按住滑块拖动)；失败（哎呀，失败了，请刷新）
            if text.text.startswith(u'请在下方'):
                print('成功滑动')
                break
            if text.text.startswith(u'请点击'):
                print('成功滑动')
                break
            if text.text.startswith(u'请按住'):
                continue
        except Exception as e:
            # 这里定位失败后的刷新按钮，重新加载滑块模块
            browser.find_element_by_xpath("//div[@id='nocaptcha']/div/span/a").click()
            print(e)
            # 退出浏览器，如果浏览器打开多个窗口，可以使用driver.close()关闭当前窗口而不是关闭浏览器


def do_action():
    # show_mobile_login()
    is_login = show_qc_image_login()
    if is_login:
        print("登录成功")
        # 进入试用页面
        new_table_open('https://pages.tmall.com/wow/baihuo/act/trial?spm=a1z0i.7764883.300.1')
    else:
        print("登录失败")

    browser.close()
    return


def new_table_open(new_url):
    browser.get(new_url)
    # 存储所有访问过的记录
    visit_history_dic = {}

    while True:
        # 处理初始化的3页数据
        js_scroll_to_bottom = "window.scrollTo(0, document.body.scrollHeight);"
        browser.execute_script(js_scroll_to_bottom)
        time.sleep(0.5)
        init_a = browser.find_elements_by_class_name('mui-itemcell__item--row')
        # list倒置
        desc_a_lists = init_a[::-1]
        if desc_a_lists is not None:
            for temp_action in desc_a_lists:
                action_url = temp_action.get_attribute("href")
                if not (action_url in visit_history_dic):
                    visit_history_dic[action_url] = action_url
                else:
                    break
                browser.execute_script('window.open()')
                browser.switch_to.window(browser.window_handles[1])
                browser.get(action_url)
                time.sleep(1)
                try:
                    # 处理
                    js_click_try='$(".h5try-ra-button")[1].click()'
                    browser.execute_script(js_click_try)
                    time.sleep(0.5)

                    js_click_try_agin='$(".btn-submit")[0].click()'
                    browser.execute_script(js_click_try_agin)
                    time.sleep(1)
                except Exception as e:
                    print(e)
                # 关闭当前页面
                browser.close()

                # 切换回到首页地址
                browser.switch_to.window(browser.window_handles[0])
        time.sleep(2)


if __name__ == "__main__":
    do_action()
