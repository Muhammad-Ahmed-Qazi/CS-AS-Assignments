' Find if the input string has all the alphabets; capital or small alike.

Module Module1

    Sub Main()
        Dim strOrig, strNew As String
        Dim charAsc As Char
        Dim total, count As Integer

        strOrig = ""
        strNew = ""

        charAsc = ""

        total = 0
        count = 0

        Console.Write("Enter a string: ")
        strOrig = Console.ReadLine()
        strOrig = LCase(strOrig)

        For count = 1 To Len(strOrig)

            charAsc = Mid(strOrig, count, 1)

            If charAsc >= "a" And charAsc <= "z" Then
                If InStr(strNew, charAsc) = 0 Then
                    strNew = strNew & charAsc
                    total = total + Asc(charAsc)
                End If
            End If
        Next

        If total = 2847 Then
            Console.WriteLine("The string has all the alphabets.")
        Else
            Console.WriteLine("The string does not have all the alphabets.")
        End If

        Console.ReadKey()
    End Sub

End Module
