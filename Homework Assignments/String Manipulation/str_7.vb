' Both_ends:
'  - Input a string s, output a string made of the first 2 and the last 2 chars of the original string, so 'spring' yields 'spng'. 
'  - However, if the string length is less than 2, return string s instead the empty string.

Module Module1

    Sub Main()
        Dim s, strNew As String

        s = ""
        strNew = ""

        Console.Write("Enter a string: ")
        s = Console.ReadLine()

        If Len(s) < 2 Then
            Console.WriteLine(s)
        Else
            strNew = Left(s, 2) + Right(s, 2)
            Console.WriteLine(strNew)
        End If

        Console.ReadKey()
    End Sub

End Module
