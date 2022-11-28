Module Module1

    Sub Main()
        Dim stringOrig, outString As String
        Dim character As Char
        Dim count As Integer

        stringOrig = ""
        character = ""
        outString = ""

        count = 0

        Console.Write("Enter a name (or string) to make an abbreviation of: ")
        stringOrig = Console.ReadLine()

        For count = 1 To Len(stringOrig)
            character = Mid(stringOrig, count, 1)
            If character = " " Then
                outString = outString & Mid(stringOrig, count + 1, 1)
            ElseIf count = 1 Then
                outString = outString & Mid(stringOrig, count, 1)
            End If
        Next

        outString = UCase(outString)

        Console.WriteLine("Abbreviation of input string: " & outString)
        Console.ReadKey()
    End Sub

End Module
