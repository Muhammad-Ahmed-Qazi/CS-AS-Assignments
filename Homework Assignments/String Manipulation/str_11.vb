' Not_bad:
'  - Given a string, find the first appearance of the substring 'not' and 'bad'. If the 'bad' follows the 'not', replace the whole 'not'...'bad' substring with 'good'.
'  - Return the resulting string.
'  - Input: 'This dinner is not that bad!' 
'  - Outputs: This dinner is good!

Module Module1

    Sub Main()
        Dim strOrig, strNew As String

        strOrig = ""
        strNew = ""

        Console.Write("Enter a string: ")
        strOrig = Console.ReadLine()

        If InStr(strOrig, "not") < InStr(strOrig, "bad") Then
            strNew = Left(strOrig, InStr(strOrig, "not") - 1) + "good" + Mid(strOrig, InStr(strOrig, "bad") + 3)
        Else
            strNew = strOrig
        End If

        Console.WriteLine("Altered string: " & strNew)

        Console.ReadKey()
    End Sub

End Module
