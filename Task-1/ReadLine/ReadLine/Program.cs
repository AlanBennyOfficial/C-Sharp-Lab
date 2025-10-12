using System;
using System.IO;

class Program
{
    static void Main()
    {
        using (var sr = new StreamReader("ReadLine.txt"))
        {
            string line = sr.ReadLine();
            Console.WriteLine(line); // prints "Hello World"
        }
    }
}
