' MixUp:
'  - Given strings a and b, return a single string with a and b separated by a space '<a> <b>', except swap the first 2 chars of each string.
'  - E.g. 'mix', pod' -> 'pox mid', 'dog', 'dinner' -> 'dig donner'
'  - Assume a and b are length 2 or more.

Module Module1

    Sub Main()
        Dim a, b, strNew As String

        a = ""
        b = ""
        strNew = ""

        Console.Write("Enter a string: ")
        a = Console.ReadLine()
        Console.Write("Enter another string: ")
        b = Console.ReadLine()

        strNew = Left(b, 2) + Mid(a, 3, Len(a)) + " " + Left(a, 2) + Mid(b, 3, Len(b))

        Console.WriteLine("Altered string: " & strNew)

        Console.ReadKey()
    End Sub

End Module
