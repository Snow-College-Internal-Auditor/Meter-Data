import webbrowser
#import win32com.client as win32comclient


def setMeters():
    meter = ['300000477','300000842','300000844','300000849','300000852']

    meterString = '300000469'

    for i in meter:
        meterString = meterString + '~' + i

    print("Select time interval")
    print("1. 15 minute intervals")
    print("2. Hour intervals")
    print("3. day intervals")
    print("4. Week intervals")
    print("5. Month intervals")
    userinput = input("Enter: ")
    while userinput != '1' and userinput != '2' and userinput != '3' and userinput !='4' and userinput !='5':
        print(userinput + ' is not one of the options. Please select again.')
        userinput = input("Enter: ")
    interval = int(userinput)

    if interval == 1:
        dateRange = "15"
    elif interval == 2:
        dateRange = "hr"
    elif interval == 3:
        dateRange = "dy"
    elif interval == 4:
        dateRange = "wk"
    elif interval == 5:
        dateRange = "mo"

    #if user does not want month summary just go by specific date
    if interval != 5:
        print("Please enter a start and end date for the summary.")
        print("Enter date as YYYYMMDDhhmm")
        print("Example: 201910310930 is 10/31/2019 at 9:30am")
        startDate = input("Enter the start date:" )
        endDate = input("Enter the end date: ")

    #If user wantes month does billing cycle
    if interval == 5:
        print("Please enter a start and end date for the summary.")

        print("Please enter a start date for the summary.")
        startYear = input('Enter year: ')
        startMonth = input('Enter month: ')
        print('Enter time of day in HHMM. Example 0830 for 8:30am')
        startTime = input('Enter time: ')
        startDate = startYear + startMonth + '15' + startTime

        print("Please enter a end date for the summary.")
        endYear = input('Enter year: ')
        #----check input----#
        endMonth = input('Enter month: ')
        #----check input----#
        endTime = input('Enter time of day: ')
        endDate = endYear + endMonth + '14' + endTime



    webbrowser.open('https://summary.ekmmetering.com/summary?key=NjUyMjA2ODE6R2JXZEluYWw&meters=' + meterString + 
                    '&format=csv&report=' + dateRange + '&limit=1000&offset=0&timezone=America~Denver&start_date=' + startDate + 
                    '&end_date=' + endDate + '&bulk=1')         


def main():
    repeat = 'y'

    while repeat == 'y':
        setMeters()
        repeat = input('Do you want to run another api call? [y/n]: ')
        while repeat != 'y' and repeat != 'n':
            print('can only enter y or n')
            repeat = input('Do you want to run another api call? [y/n]: ')
    
main()  