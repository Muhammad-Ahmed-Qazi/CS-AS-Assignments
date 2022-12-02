' Declaration
DIM balance, transactionAmount, amountShort, penalty AS DOUBLE
DIM choice AS STRING

' Initialisation
balance = 2000
transactionAmount = 0
amountShort = 0
penalty = 0.0
choice = ""

' Looping to keep the program running until the user chooses to exit
DO WHILE choice <> "N" 
    ' Input
    Console.Write("How much would you like to transact? ")
    transactionAmount = Console.ReadLine()
    
    ' 1. Debit account must not exceed the account balance
    IF transactionAmount > balance THEN
        Console.WriteLine("Insufficient funds!")
        EXIT DO
    ELSE
        ' 2. Debit account must not exceed the daily transaction limit of 800 rupees
        IF transactionAmount > 800 THEN
            Console.WriteLine("Transaction amount exceeds daily limit of 800 rupees!")
        ELSE
            balance = balance - transactionAmount

            ' 3. Leftover balance must not be less than 500 rupees. If it is, a penalty of 2% of amount short is charged.
            IF balance < 500 AND transactionAmount > 0 THEN
                amountShort = 500 - balance
                penalty = amountShort * 0.02
                Console.WriteLine("You have been charged a penalty of " & penalty & " rupees!")
                balance = balance - penalty
            ELSE
                Console.WriteLine("Transaction successful!")
            END IF
        END IF
    END IF

    Console.WriteLine("Balance: " & balance)

    ' User can choose to exit the program
    Console.Write("Enter N to exit or any other key to continue: ")
    choice = Console.ReadLine()

LOOP

Console.ReadKey()