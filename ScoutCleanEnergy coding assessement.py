#Scout Clean Energy coding assessement
import pandas as pd
import datetime
import pytz


class TableData:

    def __init__(self, filename):
        self.filename = filename

    def excel_reader(self):
        #assuming all files run through this program follow the same format and have id column
        table = pd.read_excel(self.filename, index_col = "id")
        return table

    def missingTimeStamp(self, data):
        
        time = data['time']
        #localized to UTC (can localize to whatever timezone is wanted)
        time_localized = pd.to_datetime(time, utc = True )
        data_localized = data
        data_localized['time'] = time_localized

        #if we cant assume that the data is in chronological order, use this function to sort
        #data = data.sort_values('time', ascending = True)

        #find missing timeStamps and label as NaN (H = hour, we can adjust time frame if needed)
        data_alltimes = data_localized.set_index('time').asfreq('H')
        data_alltimes = data_alltimes.reset_index()

        #need to add timestamp flag column
        alltimes = data_alltimes['time']
        timestamp_flag = []

        #check if index from alltimes exists in original time list, if it doesnt add to timestamp flag column
        for i in range(len(alltimes)):
            try:
                time[i]
                timestamp_flag.append("")
            except KeyError:
                timestamp_flag.append("Missing from original input dataset")

        data_alltimes['Timestamp Flag'] = timestamp_flag
        
        return data_alltimes

    def erroneousValues(self, data):
        qc_flag = data['VTWS_AVG'].fillna("Erroneous")

        data['data qc flag VTWS_AVG'] = qc_flag

        return data

    def excel_writer(self, data):
        #timezones not supported on xlsx
        data['time'] = data['time'].dt.tz_localize(None)
        data.to_excel("output.xlsx")

def main():
    file = TableData("test 2021-05-06 start.xlsx")
    data = file.excel_reader()
    data_final = file.missingTimeStamp(data)
    #print(data_final)
    data_erroneous = file.erroneousValues(data_final)
    #print(data_erroneous.to_string())
    file.excel_writer(data_erroneous)


if __name__ == "__main__":
    main()
    print("\n")

