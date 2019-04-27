
import unittest
from common.service import excel_handle
from config import settings
import logging


class TestMyself001(unittest.TestCase):
    """测试一下"""
    @classmethod
    def setUpClass(cls):
        # cls.excel_hand = excel_handle.GetExcelData()
        print("setUpclass")
    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # global casenum
        #
        # casenum += 1
        logging.info('----------case Start----------')

    def tearDown(self):
        logging.info('----------case Finish----------')

    def test_data_yes(self):
        filename = 'test_001.xlsx'
        self.file_name = settings.data_path + filename

        excel_hand = excel_handle.GetExcelData()
        res = excel_hand.get_case_data(self.file_name, sheet_index=2, row_id=1)
        return res


if __name__ == "__main__":
    test = TestMyself001().test_data_yes()
    print(test)
