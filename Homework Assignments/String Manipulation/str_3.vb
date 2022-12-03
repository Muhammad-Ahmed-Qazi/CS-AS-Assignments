' Count and output the NUMBER of an entered character in a string. Also output separate counts for alphabets (cap & small together), digits and other characters in same entered string. 

Module Module1

    Sub Main()
        Dim strOrig As String
        Dim charCurr, charEntered As Char
        Dim count, charCount, alphaCount, digitCount, otherCount As Integer

        strOrig = ""

        charCurr = ""
        charEntered = ""

        count = 0

        charCount = 0
        alphaCount = 0
        digitCount = 0
        otherCount = 0

        Console.Write("Enter a string: ")
        strOrig = Console.ReadLine()
        Console.Write("Enter a character to count: (Not case sensitive) ")
        charEntered = Console.ReadLine()

        strOrig = LCase(strOrig)

        For count = 1 To Len(strOrig)
            charCurr = Mid(strOrig, count, 1)

            If charCurr = charEntered Then
                charCount = charCount + 1
            End If

            If Asc(charCurr) >= 97 And Asc(charCurr) <= 122 Then
                alphaCount = alphaCount + 1
            ElseIf Asc(charCurr) >= 48 And Asc(charCurr) <= 57 Then
                digitCount = digitCount + 1
            Else
                otherCount = otherCount + 1
            End If
        Next

        Console.WriteLine("The entered character appears " & charCount & " times.")
        Console.WriteLine("The entered string has " & alphaCount & " alphabets.")
        Console.WriteLine("The entered string has " & digitCount & " digits.")
        Console.WriteLine("The entered string has " & otherCount & " other characters.")

        Console.ReadKey()
    End Sub

End Module
