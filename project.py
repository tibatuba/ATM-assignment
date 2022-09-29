import math
print("Welcome to the Bank of Tiba!")
checkPin = 1234 # the pin the user needs to enter to use the bank
attempts = 0 # the amount of tries user has to get access to bank
checkBalance = 1000 
while attempts < 3: #set up loop to stop when attempts are left to 0
    input_val = int(input("Enter your pin number: ")) #set up tries to allow use to try their pin
    attempts += 1
    if input_val == checkPin:
        break
    print(f"Wrong pin number you have attempted {attempts} times you get a total of 3 attempts") # Put a message to indicate that they got it wrong if they do 
while attempts != 3:
    choice1 = input("What would you like to do today? D: Deposit W: withdrawl C: Check balance E: Exit")
    if choice1 == "D":
        deposit = int(input("How much would you like to deposit?"))
        checkBalance += deposit
        print(f"new balance is {checkBalance}")
    elif choice1 == "W":
        withdrawl = int(input("How much would you like to withdrawl?"))
        checkBalance -= withdrawl
        print(f"You withdrawled {withdrawl}")
        print(f"The new balance is {checkBalance}")
    elif choice1 == "C":
        print(f"Your balance is {checkBalance}")
    elif choice1 == "E":
        print("Thank you for using the bank of Tiba!")
        break
    



     