using System;
using System.IO;

class Program
{
    static void Main()
    {
        using (var sr = new StreamReader("Read.txt"))
        {
            int value = sr.Read(); // numeric code of first char
            Console.WriteLine($"Read returned: {value} char: {(char)value}");
        }
    }
}
