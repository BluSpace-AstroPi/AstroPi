import csv
import codecs
import urllib.request
import urllib.error
import sys
import pandas

BaseURL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'

ApiKey='A2MXWCT2HR3N4RH7TQUGA6ZSV'
#UnitGroup sets the units of the output - us or metric
UnitGroup='metric'

newdf = []

with open('formatted_data_tester.txt', 'r') as data_file:
    for line_number, line in enumerate(data_file):
        if (line_number + 1) % 5 == 0:
            print(line)

            photo, day, latitude, longitude, date_time, cloud = line.split(',')

            #Location for the weather data
            Location = latitude + ',' + longitude

            #Optional start and end dates
            #If nothing is specified, the forecast is retrieved. 
            #If start date only is specified, a single historical or forecast day will be retrieved
            #If both start and and end date are specified, a date range will be retrieved
            StartDate = date_time
            EndDate = date_time

            #JSON or CSV 
            #JSON format supports daily, hourly, current conditions, weather alerts and events in a single JSON package
            #CSV format requires an 'include' parameter below to indicate which table section is required
            ContentType="csv"

            #include sections
            #values include days,hours,current,alerts
            Include="days"

            #basic query including location
            ApiQuery=BaseURL + Location

            #append the start and end date if present
            if (len(StartDate)):
                ApiQuery+="/"+StartDate
                if (len(EndDate)):
                    ApiQuery+="/"+EndDate

            #Url is completed. Now add query parameters (could be passed as GET or POST)
            ApiQuery+="?"

            #append each parameter as necessary
            if (len(UnitGroup)):
                ApiQuery+="&unitGroup="+UnitGroup

            if (len(ContentType)):
                ApiQuery+="&contentType="+ContentType

            if (len(Include)):
                ApiQuery+="&include="+Include

            ApiQuery+="&key="+ApiKey

            print(' - Running query URL: ', ApiQuery)
            print()

            try: 
                CSVBytes = urllib.request.urlopen(ApiQuery)
            except urllib.error.HTTPError  as e:
                ErrorInfo= e.read().decode() 
                print('Error code: ', e.code, ErrorInfo)
                sys.exit()
            except  urllib.error.URLError as e:
                ErrorInfo= e.read().decode() 
                print('Error code: ', e.code,ErrorInfo)
                sys.exit()

            # Parse the results as CSV
            CSVText1 = csv.reader(codecs.iterdecode(CSVBytes, 'utf-8'))

        
            newdf.append(CSVText1)

            '''
            RowIndex = 0
        
            # The first row contain the headers and the additional rows each contain the weather metrics for a single day
            # To simply our code, we use the knowledge that column 0 contains the location and column 1 contains the date.  The data starts at column 4
            for Row in CSVText:
                if RowIndex == 0:
                    FirstRow = Row
                else:
                    print('Weather in ', Row[0], ' on ', Row[1])
                    ColIndex = 0
                    for Col in Row:
                        if ColIndex >= 4:
                            print('   ', FirstRow[ColIndex], ' = ', Row[ColIndex])
                        ColIndex += 1
                RowIndex += 1
            # If there are no CSV rows then something fundamental went wrong
            if RowIndex == 0:
                print('Sorry, but it appears that there was an error connecting to the weather server.')
                print('Please check your network connection and try again..')
            # If there is only one CSV  row then we likely got an error from the server
            if RowIndex == 1:
                print('Sorry, but it appears that there was an error retrieving the weather data.')
                print('Error: ', FirstRow)
            '''

df = pandas.DataFrame(data = newdf)
data = []
headers = df[0][0]
print(headers)
for i in range(df.shape[0]):
    data1 = df[1][i]
    data.append(data1)

df2 = pandas.DataFrame(data, columns=headers)
df2.drop(columns = ['tempmax','tempmin','feelslikemax','feelslikemin','feelslike','dew','humidity','precipprob','precipcover','preciptype','snow','snowdepth','windgust','visibility','solarradiation',
                          'solarenergy','uvindex','severerisk','sunrise','sunset','moonphase','description','icon','stations'], axis = 1, inplace=True)
print(df2)

df2.to_csv('weather_data.csv')