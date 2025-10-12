using System;
using System.IO;

class Program
{
    static void Main()
    {
        using (var sr = new StreamReader("ReadToEnd.txt"))
        {
            string all = sr.ReadToEnd();
            Console.WriteLine(all); // prints entire file content
        }
    }
}
