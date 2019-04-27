
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from config import settings
import logging
email_conf = settings.EMAIL_CONFIG
import time

class SendEmail:
    """
    创建邮箱实例化对象
    """
    def __init__(self, report_file):
        self.report_file = report_file
        print(report_file)

    def send_email(self):

        subject = '接口自动化测试报告'
        msg = MIMEMultipart()
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = Header(email_conf['sender'], 'utf-8')
        msg['To'] = Header(email_conf['receivers'][0], 'utf-8')
        user = ''
        pass_wd = ''
        text_msg = MIMEText(
            "<html><body><p><span style='color: red;'>&nbsp;&nbsp; hi all:</span></p><p>&nbsp;&nbsp;&nbsp;&nbsp; "
            "附件为本次接口自动化测试报告，请各位查收。<br/></p></body></html>",
            'html', "utf-8")
        text_msg['Subject'] = Header(subject, 'utf-8')
        msg.attach(text_msg)
        # 附件
        att1 = MIMEText(open(self.report_file, 'rb').read(), 'base64', 'utf-8')
        print(att1)
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="report.html"'
        msg.attach(att1)

        try:
            smtp = smtplib.SMTP_SSL(email_conf['server'], email_conf['server_port'])
            logging.info('邮件服务器链接成功')
            smtp.login(user, pass_wd)
            logging.info('邮箱登录成功')
            smtp.sendmail('', '', msg.as_string())
            logging.info('邮件发送成功')
        except Exception as e:
            logging.error('发送失败，%s' % str(e))
            print(e)

        finally:
            smtp.quit()


if __name__ == "__main__":
    report_path = '../../report/2019-04-21-19-07-54Api_Test.html'
    smt = SendEmail(report_path)
    smt.send_email()
