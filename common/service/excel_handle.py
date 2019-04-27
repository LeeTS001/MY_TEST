
from common.module import excel_module, request_module
import logging
from config import settings
import json
environ_host = settings.Environment_Config['host']

class GetExcelData:

    def __init__(self):
        self.url = ''
        self.method = ''
        self.req_data = ''
        self.exp_resp = ''
        self.content_type = ''
        self.header = {}

    def get_case_data(self, filename, sheet_index=0, row_id=0, data=None, **kwargs):
        """
        获取对应行id的内容
        :param filename: 测试数据文件名
        :param sheet_index: 测试数据索引
        :param row_id: 测试数据行数
        :param data:
        :param kwargs:
        :return:
        """
        excel_hand = excel_module.ReadExcel(filename)
        sheetobj = excel_hand.get_sheet_by_index(sheet_index)
        case_list = excel_hand.get_row_value(sheetobj, row_id)
        self.url = environ_host+case_list[1]
        self.method = case_list[2]
        self.req_data = case_list[3]   # 请求参数
        self.exp_resp = case_list[4]   # 预期结果
        self.content_type = case_list[5]
        print('请求参数:%s' % self.req_data)
        # 根据cookie判断当前状态，若非登录状态，需先登录获取token
        # access_token = ''
        # if data is not None:
        #     self.req_data = data
        # for i in kwargs:
        #     if i == 'cookie':
        #         access_token = kwargs[i]
        # 如果token为空，则先登录获取token(还可以直接根据当前数据行数，若非首行，直接调登录接口获取cookie)
        # if access_token.strip() == '':
        #     act_resp = self.get_case_response()
        #     logging.info('登录请求，获取token，请求数据:%s' % self.req_data)
        # else:
        #     act_resp = self.get_case_response(access_token=access_token)
        #     logging.info('非首次登录，直接携带token请求接口，请求数据:%s' % self.req_data)
        # return act_resp, self.exp_resp
        act_resp = self.get_case_response()
        return act_resp

    def get_case_response(self, **kwargs):

        # self.header['content-type'] = self.content_type['content-type']
        # for i in kwargs:
        #     if i == "cookie":
        #         self.header['cookies'] = kwargs[i]

        req_handle = request_module.GetResponse(self.url, self.method)
        # print('======')
        # if self.header['content-type'] == 'application/json':
        #     resp = req_handle.get_response(data=json.dumps(self.req_data), headers=self.header)
        # else:
        # resp = req_handle.get_response(data=self.req_data, headers=self.header)
        resp = req_handle.get_response(json.loads(self.req_data))
        logging.info(resp)
        print('响应结果:%s' % resp)
        # resp_analysis = request_module.AnalysisRsponse(resp)
        # response = resp_analysis.get_content()
        # cookies = resp_analysis.get_cookie()
        # return response, cookies
        return resp

