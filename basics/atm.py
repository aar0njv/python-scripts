balance = 1000
pin = 2005


def check_balance():
    print("Your current balance is : {}".format(balance))

def deposit_amount():
    global balance, pin
    amount = int(input("Enter the amount to be deposited : "))
    num_tries = 3

    while(num_tries > 0):
        entered_pin = int(input("Enter the pin : "))

        if (entered_pin == pin):
            balance += amount
            print("Amount added successfully...")
            check_balance()
            break
        
        else:
            num_tries -= 1
            if num_tries != 0:
                print("Incorrect Pin, you have {} more tries...".format(num_tries))
    
        if (num_tries == 0):
            print("Access Denied, please try again later....")
            break
                

def withdraw_amount():
    global balance, pin
    amount = int(input("Enter the amount to be withdrawn : "))
    
    if (balance >= amount):

        num_tries = 3

        while(num_tries > 0):
            entered_pin = int(input("Enter the pin : "))

            if (entered_pin == pin):
                balance -= amount
                print("Amount withdrawn successfully...")
                check_balance()
                break
            
            else:
                num_tries -= 1
                if num_tries != 0:
                    print("Incorrect Pin, you have {} more tries...".format(num_tries))
        
            if (num_tries == 0):
                print("Access Denied, please try again later....")
                break
    
    else:
        print("Insufficient Balance, please try a different amount...")
        
    

def change_password():

    global balance, pin
    num_tries = 3
    while (num_tries > 0):
        entered_pin = int(input("Enter the current pin : "))

        if (entered_pin == pin):
            new_pin=int(input("Enter the new pin (4 digit) : "))

            if (new_pin == pin):
                print("Error: pin cannot be same...")
                break
            else:
                pin=new_pin
                print("Pin Changed Successfullyy.....")
                break
        
        else:
            num_tries -= 1
            if num_tries != 0:
                print("Incorrect Pin, you have {} more tries...".format(num_tries))
    
        if (num_tries == 0):
            print("Access Denied, please try again later....")
            break
            


print("Welcome to ATM Simulator !\n")

print("Balance Amount in your account is : 1000")
print("current pin is your birth year")



while(True):
    print("\n-------------------------------\n")
    print("1. Check Balance \n2. Deposit \n3. Withdraw \n4. Change Password \n5. Exit ")
    print("\n-------------------------------\n")
    choice = int(input("Enter your choice : \n"))

    if choice == 1:
        check_balance()
        

    elif choice == 2:
        deposit_amount()
        

    elif choice == 3:
        withdraw_amount()

    elif choice == 4:
        change_password()
        

    elif choice == 5:
        print("Exiting....")
        break

    else:
        print("Invalid Choice. Please try again....")
    