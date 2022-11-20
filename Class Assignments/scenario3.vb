' Declaration
DIM stStart, stEnd, noPassengers, noStations, fare AS INTEGER
DIM choice AS STRING

' Initialisation
stStart = 0
stEnd = 0
noPassengers = 0
noStations = 0
fare = 0
choice = ""

' Looping to keep the program running until the user chooses to exit
DO WHILE choice <> "N"
    ' Input
    Console.Write("Enter the station you are starting from: ")
    stStart = Console.ReadLine()
    Console.Write("Enter the station you are getting off at: ")
    stEnd = Console.ReadLine()

    ' Checking whether stations input are in the range of 1 and 5 are not
    IF stStart < 1 OR stStart > 5 THEN
        Console.WriteLine("There are only five stations! (1 --> 5)")
    ELSEIF stEnd < 1 OR stStart > 5 THEN
        Console.WriteLine("There are only five stations! (1 --> 5)")
    ELSE
        ' Input
        Console.Write("Enter the number of passengers: ")
        noPassengers = Console.ReadLine()
    
        ' Calculating no. of stations
        IF stEnd > stStart THEN
            noStations = stEnd - stStart
        ELSE
            noStations = stStart - stEnd
        END IF
    
        ' Calculating fare
        fare = (2 * noPassengers) * noStations
    
        ' Applying discount according to conditions
        IF noPassengers >= 5 AND noPassengers <= 9 THEN
            fare = fare - 8
        ELSEIF noPassengers > 9  THEN
            fare = fare - 15
        END IF
    
        ' Fare output
        Console.WriteLine("Your fare: " & fare & " rupees")
    END IF

    ' User can choose to exit the program
    Console.Write("Enter N to exit or any other key to continue: ")
    choice = Console.ReadLine()

LOOP

Console.ReadKey()