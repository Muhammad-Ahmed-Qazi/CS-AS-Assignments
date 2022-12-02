Module Module1

    Sub Main()
        Dim stringOrig As String
        Dim character As Char
        Dim count, countVowl As Integer
        Dim vowels(4) As String

        stringOrig = ""
        character = ""

        count = 0
        countVowl = 0

        vowels = {"a", "e", "i", "o", "u"}

        Console.Write("Enter a string to count vowels in: ")
        stringOrig = Console.ReadLine
        stringOrig = stringOrig.ToLower()

        For count = 1 To Len(stringOrig)
            character = Mid(stringOrig, count, 1)
            If vowels.Contains(character) Then
                countVowl = countVowl + 1
            End If
        Next

        Console.WriteLine("Number of vowels in the string: " & countVowl)
        Console.ReadKey()
    End Sub

End Module
