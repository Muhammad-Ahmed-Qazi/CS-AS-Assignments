' Replace selected character with another in entered string.

Module Module1

    Sub Main()
        Dim strOrig, strNew As String
        Dim charCurr, charRepl, charNew As Char
        Dim count As Integer

        strOrig = ""
        strNew = ""

        charCurr = ""
        charRepl = ""
        charNew = ""

        count = 0

        Console.Write("Enter a string: ")
        strOrig = Console.ReadLine()
        Console.Write("Enter a character to replace: (Case sensitive) ")
        charRepl = Console.ReadLine()
        Console.Write("Enter a character to replace with: ")
        charNew = Console.ReadLine()

        For count = 1 To Len(strOrig)
            charCurr = Mid(strOrig, count, 1)
            If charCurr = charRepl Then
                strNew = strNew + charNew
            Else
                strNew = strNew + charCurr
            End If
        Next

        Console.WriteLine("The new string is: " & strNew)

        Console.ReadKey()
    End Sub

End Module
