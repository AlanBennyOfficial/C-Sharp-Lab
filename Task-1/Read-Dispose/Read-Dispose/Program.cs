using System;
using System.IO;

class Program
{
    static void Main()
    {
        var sr = new StreamReader("DisposeRead.txt");
        string content = sr.ReadToEnd();
        sr.Dispose(); // explicitly release resources

        Console.WriteLine(content);
    }
}
