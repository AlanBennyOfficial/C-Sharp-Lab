using System;
using System.IO;

class Program
{
    static void Main()
    {
        var sw = new StreamWriter("Flush.txt");
        sw.Write("Hello");    // written to buffer
        sw.Flush();           // forces write to file immediately
        Console.WriteLine("Data flushed to file.");
        sw.Close();
    }
}
