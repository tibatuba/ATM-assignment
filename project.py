print("Welcome to the Bank of Tiba!")
checkPin = 1234 # the pin the user needs to enter to use the bank
attempts = 0 # the initializer
checkBalance = 1000 # starting balance
while attempts < 3: #set up loop to stop when attempts come to the number 3
    input_val = int(input("Enter your pin number: ")) # allow user to input pin
    attempts += 1 # attempts go up by 1 every time they get pin wrong
    if input_val == checkPin:# if users input is correct it will break into the next while loop
        break
    print(f"Wrong pin number you have attempted {attempts} times you get a total of 3 attempts") # if users input is incorrect user will get this message and loop back to put another input
while attempts != 3:# If user gets their pin pass word before attempts equals to 3 we go into a new loop
    choice1 = input("What would you like to do today? D: Deposit W: withdrawl C: Check balance E: Exit") # user needs to input what they would like to do
    if choice1 == "D":
        deposit = int(input("How much would you like to deposit?"))
        checkBalance += deposit # new deposits are stored in the variable checkBalance 
        print(f"You deposited {deposit}") # display what was deposited
        print(f"new balance is {checkBalance}") # display new balance
    elif choice1 == "W":
        withdrawl = int(input("How much would you like to withdrawl?"))
        checkBalance -= withdrawl # new withdrawls will be accounted for and stored in the variable checkBalance
        print(f"You withdrawled {withdrawl}")
        print(f"The new balance is {checkBalance}")
    elif choice1 == "C":
        print(f"Your balance is {checkBalance}") # show balance
    elif choice1 == "E": # end the program
        print("Thank you for using the bank of Tiba!")
        break # program ended after break was used as there is no new loop to enter
    



     
