import requests
from requests.exceptions import *
from config.settings import logging
import json


class GetResponse:

    def __init__(self, url, method):
        """
        实例化，接收接口的url和请求方式
        """
        self.url = url
        self.method = method

    def get_response(self, *args, **kwargs):
        """
        根据method方法，发送不同请求，这里只做了get和post请求的处理
        :return: 响应信息
        """
        if self.method == 'get':
            try:
                result = requests.get(self.url, *args, **kwargs)
            except InvalidURL:
                logging.error('请检查url:%s是否正确' % self.url)
            except ConnectionError:
                logging.error('请检查网络或api响应超时')
            else:
                logging.info('接口调取成功，返回结果%s' % result.json())
                return result.json(encoding='utf8')
        elif self.method == 'post':
            try:
                result = requests.post(self.url, *args, **kwargs)
            except InvalidURL:
                logging.error('请检查url:%s是否正确' % self.url)
            except ConnectionError:
                logging.error('请检查网络或api响应超时')
            else:
                logging.info('接口调取成功，返回结果%s' % result.json())
                return result.json(encoding='utf8')


class AnalysisRsponse:
    """解析返回值，便于用例中做断言使用"""

    def __init__(self, response):

        self.res = response

    def status_code(self):
        status_code = self.res.status_code
        return status_code

    def get_content(self):
        content = self.res.content
        return content

    def get_cookie(self):
        cookie = self.res.cookies
        return cookie


if __name__ == "__main__":
    urls = 'http://127.0.0.1:8081/test/'
    data = {"data": "yes"}
    res = GetResponse(urls, 'get')
    ret = res.get_response(data)
    print(ret)
