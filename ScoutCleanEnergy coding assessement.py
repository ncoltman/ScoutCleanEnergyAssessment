#Scout Clean Energy coding assessement
import pandas as pd
import datetime
import pytz
import csv


class TableData:

    def __init__(self, filename):
        self.filename = filename

    def excel_reader(self):
        #assuming all files run through this program follow the same format and have id column
        table = pd.read_excel(self.filename, index_col = "id")
        return table

    def missingTimeStamp(self, data):
        #if we cant assume that the data is in chronological order, use this function to sort
        #data = data.sort_values('time', ascending = True)
        
        time = data['time']
        #localized to UTC (can localize to whatever timezone is wanted)
        time_localized = pd.to_datetime(time, utc = True )
        data_localized = data
        data['time'] = time_localized
        return data_localized
        

    #def erroneousValues(self):

    #def excel_writer(self, data, path):


def main():
    file = TableData("test 2021-05-06 start.xlsx")
    data = file.excel_reader()
    #data['time'] = pd.to_datetime(data['time'])
    #data = data.set_index('time').asfreq('1H')
    #print (data)
    data_localized = file.missingTimeStamp(data)
    print(data_localized)





if __name__ == "__main__":
    main()
    print("\n")

