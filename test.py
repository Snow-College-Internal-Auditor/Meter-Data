print("Select time interval")
print("1. 15 minute intervals")
print("2. Hour intervals")
print("3. day intervals")
print("4. Week intervals")
#can set this up with billing cycle. So Sep 15 - Oct 14. Talk to wayne
print("5. Month intervals")
#----input validation-----
userinput = input("Enter: ")
while userinput != '1' and userinput != '2' and userinput != '3' and userinput !='4' and userinput !='5':
    print(userinput + ' is not one of the options. Please select again.')
    userinput = input("Enter: ")
interval = int(userinput)

#----input validation-----

