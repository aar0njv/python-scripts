#input : Number of electricity units consumed (integer)
#output : total bill with explanation
#rules : first 100 units 5/- per unit, 101-200 units 7/- per unit,
#        beyond 200units 10/- per unit


def calculate_bill(units):

    total_bill = 0

    if (units <= 100):
        total_bill = units*5

    elif (units <= 200):
        total_bill = (100*5) + ((units - 100)*7)
    
    else:
        total_bill = (100*5) + (100*7) + ((units - 200)*10)

    print("\nYour electricity bill is {}/-".format(total_bill))
    print("\n.....Bill Breakdown.....\n")
    print("Total number of units : {} \n".format(units))

    if (units <= 100):
        print("{}*5".format(units))

    elif (units <= 200):
        print("(100*5) + (({} - 100)*7)".format(units))
    
    else:
        print("(100*5) + (100*7) + (({} - 200)*10)".format(units))
    
    



units = int(input("Enter the number of electricity units consumed : "))
calculate_bill(units)