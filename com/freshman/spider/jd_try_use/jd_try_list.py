# -*- coding:utf-8 -*-

import requests
import pymysql

from bs4 import BeautifulSoup


# 抓取job
class SpiderList:

    # 页面初始化
    def __init__(self):
        # self.siteURL = 'http://try.jd.com/activity/getActivityList?page=PAGENUMBER&activityType=ACTIVITYTYPE'
        # self.siteURL = 'http://try.jd.com/activity/getActivityList?page=PAGENUMBER&activityType=1&cids=1620,6728,9847,9855,6196,15248'

        # 饮食
        # self.siteURL = 'http://try.jd.com/activity/getActivityList?page=PAGENUMBER&activityType=1&cids=12218'
        # 食品饮料
        # self.siteURL = 'http://try.jd.com/activity/getActivityList?page=PAGENUMBER&activityType=1&cids=1320,12259'
        # 电脑办公
        # self.siteURL = 'http://try.jd.com/activity/getActivityList?page=PAGENUMBER&activityType=1&cids=670'
        # self.siteURL='http://try.jd.com/activity/getActivityList?page=PAGENUMBER&cids=652,9987'
        # self.siteURL='http://try.jd.com/activity/getActivityList?page=PAGENUMBER&cids=5025,6144'
        self.siteURL = 'http://try.jd.com/activity/getActivityList?page=PAGENUMBER'

    # 获取请求的URL地址
    def get_page_url(self, page, key):
        url = self.siteURL.replace("PAGENUMBER", str(page)).replace("ACTIVITYTYPE", str(key))
        return url

    # 获取索引页面的内容
    def get_page_content(self, page, key):
        current_url = self.get_page_url(page, key)
        response = requests.get(current_url)
        response.encoding = 'utf-8'
        return response.text

    # 解析每一页数据
    def parse_one_page(self, html):
        soup = BeautifulSoup(html, "html.parser")
        post_info = soup.find_all("li", {"activity_id": True});

        for item in post_info:
            yield (
                item['activity_id']
            )

    # 保存数据到数据库中
    def save_data(self, params):
        db = pymysql.connect(host="localhost", user="root",
                             password="xxxxx", db="costnote", port=3306)

        # 使用cursor()方法获取操作游标
        cur = db.cursor()

        # 1.查询操作
        # 编写sql 查询语句  user 对应我的表名
        sql = "INSERT into jdtrydata(ActivityId,Isvalid,CreateTime) VALUES(%s,1,SYSDATE());"
        try:
            cur.executemany(sql, params)  # 执行sql语句
            db.commit()
        except Exception as e:
            raise e
        finally:
            # 关闭连接
            cur.close()
            db.close()

    # 将一页的信息保存起来
    def save_page_info(self, pageindex, key):
        # 获取第一页淘宝MM列表
        contents = self.get_page_content(pageindex, key)
        activity_list = self.parse_one_page(contents)
        activitys = []
        for item in activity_list:
            activitys.append(item)
        # self.save_data(activitys)
        return activitys

    # 传入起止页码
    def save_pages_info(self, start, end, key):
        activitys = []
        for i in range(start, end + 1):
            print("正在爬取第", i, "页数据")
            activitys += self.save_page_info(i, key)
        print(activitys)


if __name__ == '__main__':
    # 传入起止页码即可，在此传入了1,10,表示抓取第2到10页
    spider = SpiderList()
    spider.save_pages_info(1, 20, "1")
