#Scout Clean Energy coding assessement
import pandas as pd
import datetime
import pytz
import csv


class TableData:

    def __init__(self, filename):
        self.filename = filename

    def excel_reader(self):
        table = pd.read_excel(self.filename, index_col = "id")
        print(table)

    #def missingTimeStamp(self, table):

    #def erroneousValues(self, table):

    #def excel_writer(self, data, path):


def main():
    data = TableData("test 2021-05-06 start.xlsx")
    data.excel_reader()


if __name__ == "__main__":
    main()
    print("\n")

#filename = "test 2021-05-06 start.xlsx"
#table = pd.read_excel(filename, index_col = "id")
#print(table)