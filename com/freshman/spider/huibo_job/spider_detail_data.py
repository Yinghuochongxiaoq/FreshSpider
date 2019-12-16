# -*- coding:utf-8 -*-

import requests
import pymysql

from bs4 import BeautifulSoup


# 抓取job
class SpiderDetail:

    # 页面初始化
    def __init__(self):
        self.siteURL = 'http://www.huibo.com/kuaiji/jobgnott8a.html'

    # 获取索引页面的内容
    def get_page_content(self):
        current_url = self.siteURL
        response = requests.get(current_url)
        response.encoding = 'utf-8'
        return response.text

    # 解析每一页数据
    def parse_one_page(self, html):
        soup = BeautifulSoup(html, "html.parser")
        # 获取待遇信息
        salary_str = ''
        salary_port = soup.select('.newWelfare ul li')
        for item in salary_port:
            salary_str += "," + item.get_text()
        # 获取学历信息
        degree = soup.select('.iconNew02')[0].next_sibling().text.strip()
        # 刷新时间
        flash_date = soup.select('.newDateEct')[0].text.strip()

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
    def save_detail_info(self):
        # 获取第一页
        contents = self.get_page_content()
        self.parse_one_page(contents)

    # 传入起止页码
    def save_pages_info(self):
        pass


# 传入起止页码即可，在此传入了1,10,表示抓取第2到10页
spider = SpiderDetail()
spider.save_detail_info()
