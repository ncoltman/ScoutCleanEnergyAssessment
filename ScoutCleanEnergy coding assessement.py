#Scout Clean Energy coding assessement - Natalie Coltman
import pandas as pd
import datetime
import pytz


class TableData:

    def __init__(self, filename):
        self.filename = filename

    #Reads input file and converts it to a dataframe
    def excel_reader(self):
        #assuming all files run through this program follow the same format and have id column
        table = pd.read_excel(self.filename, index_col = "id")
        return table

    #This function switches all of the timestamps to UTC timezone and then identifies what timestamps are missing. 
    #The timestamps missing from the original data are labelled in the timestamp flag column
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

        #add timestamp flag column
        alltimes = data_alltimes['time']
        timestamp_flag = []

        #check if index from data_alltimes exists in original time list, if it doesnt add to timestamp flag column
        for i in range(len(alltimes)):
            try:
                time[i]
                timestamp_flag.append("")
            except KeyError:
                timestamp_flag.append("Missing from original input dataset")

        data_alltimes['Timestamp Flag'] = timestamp_flag
        
        return data_alltimes

    #This functions appends the data qc flag VTWS_AVG column
    #This new column replaces NaN values from the VTWS_AVG column with "Erroneous"
    def erroneousValues(self, data):
        erroneous_data = data
        qc_flag = data['VTWS_AVG'].fillna("Erroneous")
        erroneous_data['data qc flag VTWS_AVG'] = qc_flag

        return erroneous_data

    #This function outputs the analyzed dataframe to a CSV
    #Exporting to a CSV allows us to include the timezone in the timestamp
    def csv_writer(self, data):
        data.to_csv('output.csv')

    #timezones are not supported on xlsx, if output is required to be exported directly to excel we can use this function
    #def excel_writer(self, data):
        #data['time'] = data['time'].dt.tz_localize(None)
        #data.to_excel("output.xlsx")


def main():
    file = TableData("test 2021-05-06 start.xlsx")
    data = file.excel_reader()
    data_alltimes = file.missingTimeStamp(data)             #fills in missing timestamps
    data_erroneous = file.erroneousValues(data_alltimes)    #identifies erroneous values
    file.csv_writer(data_erroneous)                         #outputs DataFrame to csv 


if __name__ == "__main__":
    main()
    print("\n")

