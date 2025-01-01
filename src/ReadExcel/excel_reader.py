# エクセルからデータを読みます。
import pandas as pd


class ExcelReader:
    def __init__(self, path):
        self.path = path

    # 一列目が名前、二列目以降が日付の希望シフト
    def read(self, sheet_name):
        df = pd.read_excel(self.path, sheet_name=sheet_name, index_col=0)
        return df
