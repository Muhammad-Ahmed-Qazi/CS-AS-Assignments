' Find the character that appears most number of times in an entered string and output it.

Module Module1

    Sub Main()
        Dim strOrig, strNew As String
        Dim charCurr As Char
        Dim count, searchCount, charCountSta, charCountEnd, high As Integer

        strOrig = ""
        strNew = ""

        charCurr = ""

        count = 0
        searchCount = 0
        charCountSta = 0
        charCountEnd = 0
        high = 0

        Console.Write("Enter a string: ")
        strOrig = LCase(Console.ReadLine())

        For count = 1 To Len(strOrig)
            charCurr = Mid(strOrig, count, 1)
            If Asc(charCurr) >= 97 And Asc(charCurr) <= 122 Then
                If InStr(strNew, charCurr) = 0 Then
                    strNew = strNew + charCurr + "1" + " "
                Else
                    charCountSta = InStr(strNew, charCurr) + 1
                    For searchCount = charCountSta To (Len(strNew))
                        If Mid(strNew, searchCount, 1) = " " Then
                            charCountEnd = searchCount
                            Exit For
                        End If
                    Next
                    strNew = Left(strNew, charCountSta - 1) & (Int(Mid(strNew, charCountSta, (charCountEnd - charCountSta))) + 1) & " " & Right(strNew, (Len(strNew) - charCountEnd))
                End If
            End If
        Next
        
        Console.WriteLine(strNew)

        count = 0

        For count = 1 To Len(strNew)
            charCurr = Mid(strNew, count, 1)
            If Asc(charCurr) >= 48 And Asc(charCurr) <= 57 Then
                If Val(charCurr) > high Then
                    high = Val(charCurr)
                End If
            End If
        Next

        Console.WriteLine("The character that appears most number of times is: " & Mid(strNew, (InStr(strNew, high) - 1), 1))

        Console.ReadKey()
    End Sub

End Module
