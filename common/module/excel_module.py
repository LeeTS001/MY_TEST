import xlrd


class ReadExcel:

    def __init__(self, filename):
        """
        初始化
        获取当前excel的操作句柄
        :param filename:传入文件名
        """
        self.data = xlrd.open_workbook(filename)

    def close(self):
        self.data.close()

    def get_sheet_by_index(self, index):
        """
        通过表的索引来获取表的内容
        :param index: sheet的索引
        :return:返回sheet内容
        """
        sheet = self.data.sheet_by_index(index)
        return sheet

    def get_sheet_by_name(self, name):
        """
        通过表的名字获取表的内容
        :param name: sheet的名字
        :return: 返货sheet的内容
        """
        sheet = self.data.sheet_by_name(name)
        return sheet

    @staticmethod
    def get_row_value(sheet_obj, row_index):
        """
        获取指定行的内容
        :param sheet_obj: 接收sheet对象
        :param row_index: 接收获取行的索引
        :return: 返回指定行的内容（类型为列表）
        """
        value_list = sheet_obj.row_values(row_index)
        return value_list

    @staticmethod
    def get_rows(sheet_obj):
        """
        获取指定sheet的行数
        :param sheet_obj: 接收sheet对象
        :return: 返回当前sheet是数据行数
        """
        row = sheet_obj.nrows
        return row

    @staticmethod
    def get_cell_value(sheet_obj, row_index, col_index):
        """
        获取sheet中指定表格内的数据
        :param sheet_obj: 接收sheet对象
        :param row_index: 第几行
        :param col_index: 第几列
        :return: 返回指定行列数的表格的内容
        """
        cell_data = sheet_obj.cell_value(row_index, col_index)
        return cell_data
