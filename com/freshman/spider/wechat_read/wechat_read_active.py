import requests
from bs4 import BeautifulSoup
from com.freshman.spider.common_util.logger import module_log


# 抓取job
class WeChatReadActive:

    # 页面初始化
    def __init__(self):
        self.siteURL = 'https://weread.qq.com/wrpage/act/collaboration/cdkey/promo/presentation?logogram=LOGOGRAM'
        self.log = module_log(__name__)

    # 获取请求的URL地址
    def get_page_url(self, key):
        url = self.siteURL.replace("LOGOGRAM", str(key))
        return url

    # 获取索引页面的内容
    def get_page_content(self, key):
        current_url = self.get_page_url(key)
        response = requests.get(current_url)
        response.encoding = 'utf-8'
        return response.text

    # 解析数据
    def parse_one_page(self, html):
        soup = BeautifulSoup(html, "html.parser")
        post_info = soup.find_all("div", class_='cdkey_text')

        for item in post_info:
            yield (item.text)

    # 将一页的信息保存起来
    def save_page_info(self, key):
        contents = self.get_page_content(key)
        activity_list = self.parse_one_page(contents)
        activitys = []
        for item in activity_list:
            activitys.append(item)
        return activitys

    # 传入关键字
    def save_pages_info(self):
        string = "QAZWSXEDCRFVTGBYHNUJMIKOLP"
        for x in string:
            for y in string:
                key = "".join((x, y))
                try:
                    print("开始处理关键字：" + key)
                    activity_keys = self.save_page_info(key)
                    if activity_keys is not None and len(activity_keys) > 0:
                        content = "关键字：" + key + "\t优惠码：" + activity_keys[0] + "\n"
                        self.log.info(content)
                except Exception as e:
                    print("\t出现异常：" + e)


if __name__ == '__main__':
    spider = WeChatReadActive()
    spider.save_pages_info()
