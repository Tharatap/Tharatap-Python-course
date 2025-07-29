# Complete this ATM simulation
'''
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        
else:
    print("Invalid PIN")
'''
balance = 1000
pin = "1234"
entered_pin = input("Enter Pin: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        chose = int(input("Chosse option: "))
        if(chose == 1):
            print(f"balance = {balance} THB")
        elif(chose == 2):
            withdraw = float(input("How much money will you Withdraw?: "))
            if(withdraw >= 0):
                if(balance >= withdraw):
                    balance -= withdraw
                    print(f"Withdraw = {withdraw} THB")
                else:
                    print("not enough money")
            else:
                print("The amount cannot be negative.")
        elif(chose == 3):
            Deposit = float(input("How much money will you deposit?: "))
            if(Deposit >= 0):
                balance += Deposit
                print(f"Deposit = {Deposit} THB")
            else:
                print("The amount cannot be negative.")
        elif(chose == 4):
            print("Exit")
            break
        else:
            print("Error number please select again")
else:
    print("Invalid Pin")



