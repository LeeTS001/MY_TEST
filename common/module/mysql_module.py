import pymysql
from config import settings
log = settings.logging


class MysqlModule:

    def __init__(self, *args, **kwargs):
        """
        初始化类，创建数据库链接，创建游标
        """
        try:
            self.conn = pymysql.connect(*args, **kwargs)
            log.info('数据库链接成功，已创建链接')
            self.cur = self.conn.cursor()
        except Exception as e:
            log.error(e, '请检查链接数据的参数是否正确')

    """获取查询结果第一行值"""
    def get_first_data(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

    """获取查询所有结果"""
    def get_all_data(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    """执行删除语句"""
    def execute(self, sql):

        self.cur.execute(sql)
        self.conn.commit()

    def close_db(self):
        self.cur.close()
        self.conn.close()
        log.info('游标与数据库链接已经关闭')
