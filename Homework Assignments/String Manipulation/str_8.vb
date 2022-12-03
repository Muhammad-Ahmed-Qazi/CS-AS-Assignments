' Fix_start:
'  - Given a string s, return a string where all occurences of its first char have been changed to '*', except do not change the first char itself.
'  - E.g., 'babble' yields 'ba**le' or 'alpha' outputs 'alph*'.
'  - Assume that the string is length 1 or more.

Module Module1

    Sub Main()
        Dim s, strNew As String
        Dim charFirst As Char
        Dim count As Integer
        Dim flag As Boolean

        s = ""
        strNew = ""

        charFirst = ""

        count = 0

        flag = False

        Console.Write("Enter a string: ")
        s = Console.ReadLine()
        s = LCase(s)
        charFirst = Left(s, 1)

        For count = 1 To Len(s)
            If flag = True And Mid(s, count, 1) = charFirst Then
                strNew = strNew + "*"
            ElseIf flag = False Then
                strNew = strNew + Mid(s, count, 1)
                flag = True
            Else
                strNew = strNew + Mid(s, count, 1)
            End If
        Next

        Console.WriteLine("Altered string: " & strNew)

        Console.ReadKey()
    End Sub

End Module
