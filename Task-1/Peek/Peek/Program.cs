using System;
using System.IO;

class Program
{
    static void Main()
    {
        using (var sr = new StreamReader("Peek.txt"))
        {
            int p = sr.Peek();             // int for next char ('A')
            Console.WriteLine($"Peek: {(char)p} (int {p})");
        }
    }
}
