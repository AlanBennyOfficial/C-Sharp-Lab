using System;
using System.IO;

class Program
{
    static void Main()
    {
        File.WriteAllText("SeekSimple.txt", "Hello World"); // create file
        var fs = new FileStream("SeekSimple.txt", FileMode.Open, FileAccess.Read);
        fs.Seek(5, SeekOrigin.Begin);                        // move past "Hello"
        var sr = new StreamReader(fs);
        Console.WriteLine(sr.ReadToEnd());                   // prints "12345"
    }
}
