import pymysql
import requests
import json


class JdTryActivity:

    def __init__(self):
        pass

    """查询数据"""

    def search_data(self):
        db = pymysql.connect(host="localhost", user="root",
                             password="xxxxx", db="costnote", port=3306)

        # 使用cursor()方法获取操作游标
        cur = db.cursor()

        # 1.查询操作
        # 编写sql 查询语句  user 对应我的表名
        sql = "select Id,ActivityId,Isvalid from jdtrydata where Isvalid=1 order BY Id LIMIT 0,5000;"
        try:
            cur.execute(sql)  # 执行sql语句

            results = cur.fetchall()  # 获取查询的所有记录
            # 遍历结果
            for row in results:
                yield (row[0], row[1])
        except Exception as e:
            raise e
        finally:
            # 关闭连接
            db.close()

    """更新后数据"""

    def update_date(self, params):
        db = pymysql.connect(host="localhost", user="root",
                             password="xxxxx", db="costnote", port=3306)

        # 使用cursor()方法获取操作游标
        cur = db.cursor()

        # 1.查询操作
        # 编写sql 查询语句  user 对应我的表名
        sql = "update jdtrydata set Isvalid=0,UpdateTime=SYSDATE() where Id=%s;"
        try:
            cur.executemany(sql, params)
            db.commit()
        except Exception as e:
            raise e
        finally:
            # 关闭连接
            cur.close()
            db.close()

    """执行活动请求"""

    def do_activity(self, activity_id):
        cookies = self.get_cookie()
        apply_url = 'http://try.jd.com/migrate/apply?activityId=' + str(activity_id) + '&source=0'
        res = requests.get(apply_url, cookies=cookies)
        json_str = json.dumps(res.content)
        print(json_str)

    """获取cookie信息"""

    def get_cookie(self):
        f = open(r'userCookie.txt', 'r')  # 打开所保存的cookies内容文件
        cookies = {}  # 初始化cookies字典变量
        for line in f.read().split(';'):  # 按照字符：进行划分读取
            # 其设置为1就会把字符串拆分成2份
            name, value = line.strip().split('=', 1)
            cookies[name] = value  # 为字典cookies添加内容
        return cookies


if __name__ == "__main__":
    jd_obj = JdTryActivity()
    jd_activity_list = jd_obj.search_data()
    jd_activitys = []
    jd_id = []
    for item in jd_activity_list:
        # jd_obj.do_activity(item[1])
        # jd_activitys.append(item)
        # jd_id.append(item[0])
        jd_id.append(item[1])
    # jd_obj.update_date(jd_id)
    print("处理完成\n")
    print(jd_id)
