import webbrowser


def callApi():
    print("Please enter a start and end date for the summary.")
    print("Enter date as YYYYMMDDhhmm")
    print("Example: 201910310930 is 10/31/2019 at 9:30am")

    startDate = input("Enter the start date:" )
    endDate = input("Enter the end date: ")
    
    meters = ['300001306', '350000381']

    for i in meters:
        webbrowser.open('https://summary.ekmmetering.com/summary?key=NjUyMjA2ODE6R2JXZEluYWw&meters=' + i + 
                        '&format=html&report=mo&limit=10&offset=0&timezone=America~Denver&start_date=' + startDate + '&end_date=' + endDate)
          

def test():
    print("It hit test function")
    test = input("did it work: ")


def menu():
    print("1. test")
    print("2. multiple summary")
    val = input("Enter number: ")
    choice = int(val)
    return choice


def switch(choice):
    if choice == 1:
        test()
    elif choice == 2:
        callApi()
    #switcher = {
     #   1: test(),
      #  2: callApi()
    #}          


def main():
    choice = menu()
    switch(choice)
main()  
