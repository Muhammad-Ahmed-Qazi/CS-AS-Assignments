' Verbing:
'  - Given a string, if its length is at least 3, add 'ing' to its end.
'  - Unless it already ends in 'ing', in which case add 'ly' instead.
'  - If the string length is less than 3, leave it unchanged.
'  - Return the resulting string.
'  - Examples: input 'end' --> 'ending', input 'ending' --> 'endingly', input 'go' --> 'go'

Module Module1

    Sub Main()
        Dim strOrig, strNew As String

        strOrig = ""
        strNew = ""

        Console.Write("Enter a string: ")
        strOrig = Console.ReadLine()

        If Len(strOrig) >= 3 Then
            If Right(strOrig, 3) = "ing" Then
                strNew = strOrig & "ly"
            Else
                strNew = strOrig + "ing"
            End If
        Else
            strNew = strOrig
        End If

        Console.WriteLine("Altered string: " & strNew)

        Console.ReadKey()
    End Sub

End Module
