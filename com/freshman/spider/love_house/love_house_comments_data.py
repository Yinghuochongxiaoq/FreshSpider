import requests
import time
import json

stop_flag = False


# 获取每一页数据
def get_one_page(url):
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.text
    return None


# 解析每一页数据
def parse_one_page(html):
    json_data = json.loads(html)
    if json_data['total'] < 1:
        global stop_flag
        stop_flag = True
        return None
    data = json.loads(html)['cmts']  # 获取评论内容
    for item in data:
        yield {
            'date': item['time'].split(' ')[0],
            'nickname': item['nickName'],
            'city': item['cityName'],
            'rate': item['score'],
            'conment': item['content']
        }


# 保存到文本文档中
def save_to_txt():
    for i in range(1, 1001):

        print("开始保存第%d页" % i)
        url = 'http://m.maoyan.com/mmdb/comments/movie/1175253.json?_v_=yes&offset=' + str(i)
        html = get_one_page(url)
        back_data = parse_one_page(html)
        write_data_to_file = ""
        for item in back_data:
            write_data_to_file += item['date'] + ',' + item['nickname'] + ',' + item['city'] + ',' + str(
                item['rate']) + ',' + item['conment'] + '\n'
        if stop_flag:
            return
        with open('爱情公寓.txt', 'a', encoding='utf-8') as f:
            f.write(write_data_to_file)
            # time.sleep(random.randint(1,100)/20)
            time.sleep(0.5)


# 去重重复的评论内容
def delete_repeat(old, new):
    oldfile = open(old, 'r', encoding='utf-8')
    newfile = open(new, 'w', encoding='utf-8')
    content_list = oldfile.readlines()  # 获取所有评论数据集
    content_alread = []  # 存储去重后的评论数据集

    for line in content_list:
        if line not in content_alread:
            newfile.write(line + '')
            content_alread.append(line)


if __name__ == '__main__':
    save_to_txt()
    delete_repeat(r'爱情公寓.txt', r'爱情公寓_new.txt')
