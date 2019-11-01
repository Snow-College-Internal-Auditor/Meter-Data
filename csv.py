import webbrowser


def multipleMeters():
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
    
    meters = ['300001306', '350000381']

    for i in meters:
        webbrowser.open('https://summary.ekmmetering.com/summary?key=NjUyMjA2ODE6R2JXZEluYWw&meters=' + i + 
                        '&format=html&report=' + dateRange + '&limit=1000&offset=0&timezone=America~Denver&start_date=' + startDate + '&end_date=' + endDate)
          

def singalMeter():
    meterNumber = input("Please enter the meter number: ")

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

    startDate = input("Enter the start date: " )
    endDate = input("Enter the end date: ")
    
    webbrowser.open('https://summary.ekmmetering.com/summary?key=NjUyMjA2ODE6R2JXZEluYWw&meters=' + meterNumber + 
                    '&format=html&report=' + dateRange + '&limit=10000&offset=0&timezone=America~Denver&start_date=' + startDate + 
                    '&end_date=' + endDate)


def menu():
    print("1. One meter summary")
    print("2. multiple meter summary")
    val = input("Enter number: ")
    choice = int(val)
    return choice


def switch(choice):
    if choice == 1:
        singalMeter()
    elif choice == 2:
        multipleMeters()          


def main():
    choice = menu()
    switch(choice)
main()  
