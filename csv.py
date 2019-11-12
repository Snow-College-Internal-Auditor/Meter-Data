import webbrowser


def setMeters():
    meters = [
    '350001723', '350001724', '350001725', '350001726', '350001728', '350001729', '350001730', '350001731', '350001732', '350001733', '350001734', '350001736', ]
    
    meterString = '350001722'

    for i in meters:
        meterString = meterString + '~' + i

    print("Select time interval")
    print("1. 15 minute intervals")
    print("2. Hour intervals")
    print("3. day intervals")
    print("4. Week intervals")
    #can set this up with billing cycle. So Sep 15 - Oct 14. Talk to wayne
    print("5. Month intervals")
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

    print("Please enter a start and end date for the summary.")
    print("Enter date as YYYYMMDDhhmm")
    print("Example: 201910310930 is 10/31/2019 at 9:30am")

    startDate = input("Enter the start date:" )
    endDate = input("Enter the end date: ")

    webbrowser.open('https://summary.ekmmetering.com/summary?key=NjUyMjA2ODE6R2JXZEluYWw&meters=' + meterString + 
                    '&format=html&report=' + dateRange + '&limit=1000&offset=0&timezone=America~Denver&start_date=' + startDate + 
                    '&end_date=' + endDate)


def Meters():
    print("Select time interval")
    print("1. 15 minute intervals")
    print("2. Hour intervals")
    print("3. day intervals")
    print("4. Week intervals")
    #can set this up with billing cycle. So Sep 15 - Oct 14. Talk to wayne
    print("5. Month intervals")
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

    print("Please enter a start and end date for the summary.")
    print("Enter date as YYYYMMDDhhmm")
    print("Example: 201910310930 is 10/31/2019 at 9:30am")

    startDate = input("Enter the start date:" )
    endDate = input("Enter the end date: ")

    unserinput = input("How many meters do you want to pull: ")
    numberOfMeters = int(unserinput)

    meterarray = []

    for i in range(numberOfMeters):
        meter = input("Meter number: ")
        meterarray.append(meter)
    
    for j in meterarray:
        webbrowser.open('https://summary.ekmmetering.com/summary?key=NjUyMjA2ODE6R2JXZEluYWw&meters=' + j + 
                        '&format=html&report=' + dateRange + '&limit=1000&offset=0&timezone=America~Denver&start_date=' + startDate + 
                        '&end_date=' + endDate)


def menu():
    print("1. set meters summary")
    print("2. Variable meters")
    val = input("Enter number: ")
    choice = int(val)
    return choice


def switch(choice):
    if choice == 1:
        setMeters()
    elif choice == 2:
        Meters()          


def main():
    repeat = 'y'

    while repeat == 'y':
        choice = menu()
        switch(choice)
        repeat = input('Do you want to run another api call? [y/n]: ')
main()  