' Find the count of vowels characters in an entered string separately.

Module Module1

    Sub Main()
        Dim strOrig As String
        Dim charCurr As Char
        Dim count, a, e, i, o, u As Integer

        strOrig = ""

        charCurr = ""

        count = 0

        a = 0
        e = 0
        i = 0
        o = 0
        u = 0

        Console.Write("Enter a string: ")
        strOrig = Console.ReadLine()

        strOrig = LCase(strOrig)

        For count = 1 To Len(strOrig)
            charCurr = Mid(strOrig, count, 1)
            If charCurr = "a" Then
                a = a + 1
            ElseIf charCurr = "e" Then
                e = e + 1
            ElseIf charCurr = "i" Then
                i = i + 1
            ElseIf charCurr = "o" Then
                o = o + 1
            ElseIf charCurr = "u" Then
                u = u + 1
            End If
        Next

        Console.WriteLine("The count of vowels in the string is: ")
        Console.WriteLine("a: " & a & " e: " & e & " i: " & i & " o: " & o & " u: " & u)


        Console.ReadKey()
    End Sub

End Module
