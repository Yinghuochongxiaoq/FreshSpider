# -*- coding:utf-8 -*-

import requests
import os
import time
import pymysql
import re

from bs4 import BeautifulSoup


# 抓取job
class SpiderList:

    # 页面初始化
    def __init__(self):
        self.siteURL = 'http://www.huibo.com/jobsearch/?params=pPAGENUMBER&key=KEY&timestamp=TIMESTAMP#list'

    # 获取请求的URL地址
    def get_page_url(self, page, key):
        url = self.siteURL.replace("PAGENUMBER", str(page)).replace("KEY", key).replace("TIMESTAMP",
                                                                                        str(int(time.time())))
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
        post_info = soup.select('.postIntro')

        for item in post_info:
            job_list = item.select('.postIntroList .postIntroLx')
            title_dic = item.select('.title a')
            for job in job_list:
                money_array = job.select('.money')[0].text.strip().replace('￥', '').split('-')
                if money_array.__len__() < 2:
                    min_money = money_array[0].strip().split('(')[0]
                    max_money = min_money
                else:
                    min_money = money_array[0].strip()
                    max_money = money_array[1].strip().split('(')[0]
                min_money = re.sub('[^0-9]', '', min_money)
                max_money = re.sub('[^0-9]', '', max_money)
                yield (
                    # "title": title_dic[0].text.strip(),
                    # "description": title_dic[1].text.strip(),
                    # "name": job.select('.name a')[0].text.strip(),
                    # "href": job.select('.name a')[0].get("href").strip(),
                    # "min_money": min_money,
                    # "max_money": max_money,
                    # "address": job.select('.address')[0].text.strip()
                    title_dic[0].text.strip(),
                    title_dic[1].text.strip(),
                    job.select('.name a')[0].text.strip(),
                    job.select('.name a')[0].get("href").strip(),
                    min_money,
                    max_money,
                    job.select('.address')[0].text.strip()
                )

    # 创建新目录
    def mk_dir(self, path):
        path = path.strip()
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        is_exists = os.path.exists(path)
        # 判断结果
        if not is_exists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            return False

    # 保存数据到数据库中
    def search_data(self):
        db = pymysql.connect(host="localhost", user="root",
                             password="xxxxx", db="costnote", port=3306)

        # 使用cursor()方法获取操作游标
        cur = db.cursor()

        # 1.查询操作
        # 编写sql 查询语句  user 对应我的表名
        sql = "select * from user"
        try:
            cur.execute(sql)  # 执行sql语句

            results = cur.fetchall()  # 获取查询的所有记录
            print("id", "name", "password")
            # 遍历结果
            for row in results:
                id = row[0]
                name = row[1]
                password = row[2]
                print(id, name, password)
        except Exception as e:
            raise e
        finally:
            # 关闭连接
            db.close()

    # 保存数据到数据库中
    def save_data(self, params):
        db = pymysql.connect(host="localhost", user="root",
                             password="xxxxx", db="costnote", port=3306)

        # 使用cursor()方法获取操作游标
        cur = db.cursor()

        # 1.查询操作
        # 编写sql 查询语句  user 对应我的表名
        sql = "INSERT into hui_bo_job(title,description,name,href,minmoney,maxmoney,address)VALUES(%s,%s,%s,%s,%s,%s,%s)"
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
        job_list = self.parse_one_page(contents)
        jobs = []
        for item in job_list:
            jobs.append(item)
        self.save_data(jobs)

    # 传入起止页码
    def save_pages_info(self, start, end, key):
        for i in range(start, end + 1):
            print("正在爬取第", i, "页数据")
            self.save_page_info(i, key)


if __name__ == '__main__':
    spider = SpiderList()
    spider.save_pages_info(1, 42, "会计")
