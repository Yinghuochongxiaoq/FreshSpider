import os
import time
from concurrent.futures import ThreadPoolExecutor
from glob import iglob
from urllib.parse import urljoin
from natsort import natsorted
import m3u8 as m3u8
import requests


class CombineVideo(object):
    def __init__(self, m3u8_url, fine_name=None):
        """
        初始化函数
        """
        self.m3u8_url = m3u8_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
        self.file_name = fine_name
        self.thread_pool = ThreadPoolExecutor(max_workers=10)
        if not self.file_name:
            self.file_name = "new.mp4"

    def get_ts_url(self):
        """
        获取ts文件路径
        :return:
        """
        m3u8_obj = m3u8.load(self.m3u8_url, headers=self.headers)
        base_url = m3u8_obj.base_uri

        all_urls=[]
        for seg in m3u8_obj.segments:
            all_urls.append(urljoin(base_url, seg.uri))
        return all_urls

    def download_single_ts(self, url_info):
        """
        下载单个文件
        :param url_info:文件信息
        :return:
        """
        url, ts_name = url_info
        res = requests.get(url, headers=self.headers)
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), f"ts\\{ts_name}")
        self.mk_dir(path)
        with open(path, 'wb') as fp:
            fp.write(res.content)

    @staticmethod
    def mk_dir(path):
        """
        创建目录
        :param path:
        :return:
        """
        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")

        path = os.path.dirname(path)
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

    def download_all_ts(self):
        """
        下载全部ts文件
        :return:
        """
        ts_urls = self.get_ts_url()
        for index, ts_url in enumerate(ts_urls):
            print(f'下载文件链接：{ts_url}')
            temp_file_name = str(index) + '.ts'
            self.thread_pool.submit(self.download_single_ts, [ts_url, temp_file_name])
            # self.download_single_ts([ts_url, temp_file_name])
        # self.thread_pool.join()
        self.thread_pool.shutdown()

    def run(self):
        self.download_all_ts()
        # 相对路径
        ts_path = "ts\\*.ts"
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), f"ts\\{self.file_name}")
        with open(path, 'wb') as fn:
            for ts in natsorted(iglob(ts_path)):
                with open(ts, 'rb') as ft:
                    scline = ft.read()
                    fn.write(scline)
        # for ts in iglob(ts_path):
        #     os.remove(ts)


if __name__ == "__main__":
    start = time.time()
    m3u8_url = 'https://video.huishenghuo888888.com/putong/20200101/cMhYXApy/500kb/hls/index.m3u8'
    M3U8 = CombineVideo(m3u8_url)
    M3U8.run()

    end = time.time()
    print(f'耗时：{end-start}毫秒')
