# Initialisation
stStart = 0
stEnd = 0
noPassengers = 0
noStations = 0
fare = 0
choice = ""

# Looping to keep the program running until the user chooses to exit
while True:
    # Input
    stStart = int(input("Enter the station no. you are starting from: "))
    stEnd = int(input("Enter the station no. you are getting off at: "))

    # Checking whether stations input are in the range of 1 and 5 or not
    if stStart < 1 or stStart > 5:
        print("There are only five stations! (1 -> 5)")
    elif stEnd < 1 or stEnd > 5:
        print("There are only five stations! (1 -> 5)")
    else:
        # Input    
        noPassengers = int(input("Enter the no. of passengers: "))
        
        # Calculating no. of stations
        if stEnd > stStart:
            noStations = stEnd - stStart
        elif stStart > stEnd:
            noStations = stStart - stEnd
        
        # Calculating fare
        fare = (2 * noPassengers) * noStations

        # Applying discount according to conditions
        if noPassengers >= 5 and noPassengers <= 9:
            fare = fare - 8
        elif noPassengers > 9:
            fare = fare - 15

        # Fare output
        print("Your fare:", fare, "rupees")

    # User can choose to exit the program
    choice = input("Enter N to exit or any other key to continue: ")
    if choice == 'N' or choice == 'n':
        break