import webbrowser


def setMeters():
    meters = ['300000469','300000477','300000842','300000844','300000849','300000852','300000856','300001124','300001131','300001133','300001136','300001138',
                '300001158','300001160','300001305','300001306','350000381','350000382','350000383','350000384','350000385','350000386','350000387','350000388','350000389',
                '350000390','350000391','350000392','350000393','350000394','350000395','350000396','350000397','350000398','350000399','350000401','350000402','350000403',
                '350000404','350000405','350000406','350000407','350000408','350000409','350000410','350000411','350000412','350000413','350000414','350000416','350000417',
                '350000418','350000419','350000420','350000501','350000502','350000503','350000504','350000505','350000506','350000507','350000508',
                '350000509','350000510','350000511','350000512','350000513','350000514','350000515','350000516','350000517','350000518','350000519','350000520','350000521',
                '350000522','350000523','350000524','350000525','350000526','350000527','350000528','350000529','350000530','350000531','350000532','350000533','350000534',
                '350000535','350000536','350000537','350000538','350000539','350000540','350000645','350000661','350000662','350000663','350000664','350000665','350000666',
                '350000667','350000668','350000669','350000670','350000671','350000672','350000673','350000674','350000675','350000676','350000677','350000678','350000679',
                '350000680','350000681','350000682','350000683','350000684','350000685','350000686','350000687','350000688','350000689','350000690','350000691','350000692',
                '350000693','350000694','350000695','350000696','350000697','350000698','350000699','350000700','350000996','350001221','350001222','350001223','350001224',
                '350001225','350001226','350001227','350001228','350001229','350001230','350001231','350001232','350001233','350001234','350001235','350001236','350001237',
                '350001238','350001239','350001240','350001241','350001242','350001243','350001244','350001245','350001246','350001247','350001248','350001249','350001250',
                '350001251','350001252','350001253','350001254','350001255','350001256','350001257','350001258','350001259','350001260','350001461','350001462','350001463']

    meterString = '350001722'

    #'350000415'
    #'350000400'

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
                    '&end_date=' + endDate + '&bulk=1')


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
                        '&end_date=' + endDate + '&bulk=1')


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