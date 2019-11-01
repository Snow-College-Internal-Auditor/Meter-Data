import webbrowser
import datetime

#--------------------------------------gets current date-------------------------------#

from dateutil.relativedelta import relativedelta
currentdate = datetime.datetime.now()
date_formated = currentdate.strftime("%m%d%Y")

#--------------------------------------gets current date-------------------------------#

#--------------------------------------gets date range date-------------------------------#

print("Please enter a start and end date for the summary.")
print("Enter date as YYYYMMDDhhmm")
print("Example: 201910310930 is 10/31/2019 at 9:30am")
startDate = input("Enter the start date:" )
endDate = input("Enter the end date: ")

#--------------------------------------gets date range date-------------------------------#


#--------------------------------------calls api---------------------------------------#

meters = ['300001306', '350000381']

for i in meters:
    webbrowser.open('https://summary.ekmmetering.com/summary?key=NjUyMjA2ODE6R2JXZEluYWw&meters=' + i + 
                    '&format=csv&report=mo&limit=10&offset=0&timezone=America~Denver&start_date=' + startDate + '&end_date=' + endDate)  
    print("h")

#--------------------------------------calls api---------------------------------------#

