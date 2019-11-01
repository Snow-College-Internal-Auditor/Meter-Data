import webbrowser

#--------------------------------------gets date range date-------------------------------#
#test!!!!!
def getStartDate():
    startDate = input("Enter the start date:" )
    return startDate

def getEndDate():
    endDate = input("Enter the end date: ")
    return endDate

#--------------------------------------gets date range date-------------------------------#

#--------------------------------------calls api---------------------------------------#
def callApi(startDate, endDate):

    meters = ['300001306', '350000381']

    for i in meters:
        webbrowser.open('https://summary.ekmmetering.com/summary?key=NjUyMjA2ODE6R2JXZEluYWw&meters=' + i + 
                        '&format=html&report=mo&limit=10&offset=0&timezone=America~Denver&start_date=' + startDate + '&end_date=' + endDate)  

#--------------------------------------calls api---------------------------------------#

def main():
    print("Please enter a start and end date for the summary.")
    print("Enter date as YYYYMMDDhhmm")
    print("Example: 201910310930 is 10/31/2019 at 9:30am")

    startDate = getStartDate()
    endDate = getStartDate()

    callApi(startDate, endDate)
main()  