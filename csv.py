import webbrowser


def setMeters():
    meter1 = ['300000477','300000842','300000844','300000849','300000852','300000856','300001124','300001131','300001133','300001136','300001138',
                '300001158','300001160','300001305','300001306','350000381','350000382','350000383','350000384','350000385','350000386','350000387','350000388','350000389',
                '350000390','350000391','350000392','350000393','350000394','350000395','350000396','350000397','350000398','350000399','350000401','350000402','350000403',
                '350000404','350000405','350000406','350000407','350000408','350000409','350000410','350000411','350000412','350000413','350000414','350000416','350000417',
                '350000418','350000419','350000420','350000501','350000502','350000503','350000504','350000505','350000506','350000507','350000508','350001462','350001463',
                '350000509','350000510','350000511','350000512','350000513','350000514','350000515','350000516','350000517','350000518','350000519','350000520','350000521',
                '350000522','350000523','350000524','350000525','350000526','350000527','350000528','350000529','350000530','350000531','350000532','350000533','350000534',
                '350000535','350000536','350000537','350000538','350000539','350000540','350000645','350000661','350000662','350000663','350000664','350000665','350000666',
                '350000667','350000668','350000669','350000670','350000671','350000672','350000673','350000674','350000675','350000676','350000677','350000678','350000679',
                '350000680','350000681','350000682','350000683','350000684','350000685','350000686','350000687','350000688','350000689','350000690','350000691','350000692',
                '350000693','350000694','350000695','350000696','350000697','350000698','350000699','350000700','350000996','350001221','350001222','350001223','350001224',
                '350001225','350001226','350001227','350001228','350001229','350001230','350001231','350001232','350001233','350001234','350001235','350001236','350001237',
                '350001238','350001239','350001240','350001241','350001242','350001243','350001244','350001245','350001246','350001247','350001248','350001249','350001250',
                '350001251','350001252','350001253','350001254','350001255','350001256','350001257','350001258','350001259','350001260','350001461']

    meter2 = ['350001465','350001466','350001467','350001468','350001469','350001470','350001471','350001472','350001473','350001474','350001475','350001476',
            '350001477','350001478','350001479','350001480','350001481','350001482','350001483','350001484','350001485','350001486','350001487','350001488','350001489',
            '350001490','350001491','350001492','350001493','350001494','350001495','350001496','350001497','350001498','350001499','350001500','350001621','350001622',
            '350001623','350001624','350001625','350001626','350001627','350001628','350001629','350001630','350001631','350001632','350001633','350001634','350001635',
            '350001636','350001637','350001638','350001639','350001640','350001641','350001642','350001643','350001644','350001645','350001646','350001649','350001650',
            '350001651','350001652','350001653','350001654','350001655','350001656','350001657','350001658','350001659','350001660','350001701','350001702','350001703',
            '350001704','350001705','350001706','350001707','350001708','350001709','350001710','350001711','350001712','350001713','350001714','350001715','350001716',
            '350001717','350001718','350001719','350001720','350001721','350001722','350001723','350001724','350001725','350001726','350001728','350001729','350001730',
            '350001731','350001732','350001733','350001734','350001736','350001737','350001738','350001739','350001740','350001902','350001905','350001906','350001908',
            '350001910','350001912','350001913','350001915','350001919','350001924','350001925','350001926','350002101','350002102','350002103','350002104','350002105',
            '350002106','350002107','350002108','350002109','350002110','350002111','350002112','350002113','350002114','350002115','350002116','350002117','350002118',
            '350002119','350002120','350002121','350002122','350002123','350002124','350002125','350002126','350002127','350002128','350002129','350002130','350002131']

    meter3 = ['350002133','350002134','350002135','350002136','350002137','350002138','350002139','350002140','350002181','350002182','350002183','350002184',
            '350002185','350002186','350002187','350002188','350002189','350002190','350002191','350002192','350002193','350002194','350002195','350002196','350002197',
            '350002198','350002199','350002200','350002201','350002202','350002203','350002205','350002206','350002207','350002208','350002209','350002211','350002212',
            '350002217','350002218','350002219','350002703','350002731']         

    meterString1 = '300000469'
    meterString2 = '350001464'
    meterString3 = '350002132'

    for i in meter1:
        meterString1 = meterString1 + '~' + i

    for i in meter2:
        meterString2 = meterString2 + '~' + i

    for i in meter3:
        meterString3 = meterString3 + '~' + i

    
    print("Select time interval")
    print("1. 15 minute intervals")
    print("2. Hour intervals")
    print("3. day intervals")
    print("4. Week intervals")
    #can set this up with billing cycle. So Sep 15 - Oct 14. Talk to wayne
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

    print("Please enter a start and end date for the summary.")
    print("Enter date as YYYYMMDDhhmm")
    print("Example: 201910310930 is 10/31/2019 at 9:30am")

    startDate = input("Enter the start date:" )
    endDate = input("Enter the end date: ")

    webbrowser.open('https://summary.ekmmetering.com/summary?key=NjUyMjA2ODE6R2JXZEluYWw&meters=' + meterString1 + 
                    '&format=html&report=' + dateRange + '&limit=1000&offset=0&timezone=America~Denver&start_date=' + startDate + 
                    '&end_date=' + endDate + '&bulk=1')
        
    webbrowser.open('https://summary.ekmmetering.com/summary?key=NjUyMjA2ODE6R2JXZEluYWw&meters=' + meterString2 + 
                    '&format=html&report=' + dateRange + '&limit=1000&offset=0&timezone=America~Denver&start_date=' + startDate + 
                    '&end_date=' + endDate + '&bulk=1')

    webbrowser.open('https://summary.ekmmetering.com/summary?key=NjUyMjA2ODE6R2JXZEluYWw&meters=' + meterString3 + 
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

    print("Please enter a start and end date for the summary.")
    print("Enter date as YYYYMMDDhhmm")
    print("Example: 201910310930 is 10/31/2019 at 9:30am")

    startDate = input("Enter the start date:" )
    endDate = input("Enter the end date: ")

    userinput = input("How many meters do you want to pull: ")
    isdigttest = userinput.isdigit()
    while isdigttest == False:
        userinput = input("Incorrect input. Can only enter digits. Please re-enter number of meters to pull: ")
        isdigttest = userinput.isdigit()

    numberOfMeters = int(userinput)

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
    #----input validation-----
    val = input("Enter number: ")
    #----input validation-----
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
        #----input validation-----
        repeat = input('Do you want to run another api call? [y/n]: ')
        #----input validation-----
main()  