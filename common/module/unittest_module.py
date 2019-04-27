import unittest
import logging
import HTMLTestRunner


class UnittestModule:
    def __init__(self):
        self.loader = unittest.TestLoader()


    def make_suite(self, case=None):

        suite = unittest.TestSuite(case)
        return suite

    def load_case_from_module(self, module):

        suite = self.loader.loadTestsFromModule(module)
        return suite

    def run_and_report(self, suite, stream='', title=None, verbosity=1, description=None):

        logging.info('开始执行测试套件')
        runner = HTMLTestRunner.HTMLTestRunner(stream=stream, verbosity=verbosity, title=title,
                                               description=description)
        runner.run(suite)

        logging.info('测试套件执行结束')

