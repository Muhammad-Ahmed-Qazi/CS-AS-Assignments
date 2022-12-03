' doughnuts:
'  - INPUT an INT count of a number of doughnuts, OUTPUT a string of the form 'Number of doughnuts: <count>', where <count> is the number input. 
'  - However, if the count is 10 or more, then use the word 'many' instead of the actual count.
'  - So doughnuts(5) outputs 'Number of doughnuts: 5' and doughnuts(23) outputs 'Number of doughnuts: many'

Module Module1

    Sub Main()
        Dim donCount As Integer

        donCount = 0

        Console.Write("Enter the number of doughnuts: ")
        donCount = Int(Console.ReadLine())

        If donCount >= 10 Then
            Console.WriteLine("Number of doughnuts: many")
        Else
            Console.WriteLine("Number of doughnuts: " & donCount)
        End If

        Console.ReadKey()
    End Sub

End Module
