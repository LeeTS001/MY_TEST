from common.module import unittest_module
from common.module import email_module
import datetime
import time

class SuiteAndReport:

    def make_report_name(self, test_module):
        """
        定义测试报告名称
        :param test_module: 被测模块
        :return: 返回报告名称
        """
        date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        report_name = date + test_module + '.html'
        report_file = '../report/' + report_name
        return report_file

    def run_and_report(self, test_module, report_file_name, title, description, verbosity=1):
        suite_list = []
        unittest_handle = unittest_module.UnittestModule()
        for tmp in test_module:
            test_suite = unittest_handle.load_case_from_module(tmp)
            suite_list.append(test_suite)
        final_suite = unittest_handle.make_suite(suite_list)
        report_file = self.make_report_name(report_file_name)
        stream = open(report_file, 'wb')
        unittest_handle.run_and_report(final_suite, stream=stream, title=title,
                                       verbosity=verbosity,
                                       description=description)
        time.sleep(2)
        email_hand = email_module.SendEmail(report_file)
        email_hand.send_email()




