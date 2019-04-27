import sys
from common.service import suite_report


from test_case import test_case_myself
test_module = [test_case_myself]
run = suite_report.SuiteAndReport()
run.run_and_report(
    test_module=test_module,
    report_file_name='Api_Test',
    title='接口自动化测试',
    description='create by lee'
)
