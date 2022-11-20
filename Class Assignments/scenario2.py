# Initialisation
balance = 2000.0
transactionAmount = 0.0
amountShort = 0.0
penalty = 0.0
choice = ""

# Looping to keep the program running until the user chooses to exit
while True:
    # Input
    transactionAmount = float(input("How much would you like to transact? "))

    # 1. Debit account must not exceed the account balance
    if transactionAmount > balance:
        print("Insufficient funds!")
    else:
        # 2. Debit amount must not exceed the daily transaction limit of 800 rupees
        if transactionAmount > 800:
            print("Transaction amount exceeds daily limit of 800 rupees!")
        else:
            balance = balance - transactionAmount
            
            # 3. Leftover balance must not be less than 500 rupees. If it is, a penalty of 2% of amount short is charged.
            if balance < 500 and transactionAmount > 0:
                amountShort = 500 - balance
                penalty = amountShort * 0.02
                balance = balance - penalty
                print("You have been charged a penalty of", penalty, "rupees!")
            else:
                print("Transaction has been successfully completed!")
    
    print("Balance: ", balance)

    # User can choose to exit the program
    choice = input("Enter N to exit or any other key to continue: ")
    if choice == 'N' or choice == 'n':
        break
