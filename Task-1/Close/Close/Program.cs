using System.IO;

class Program
{
    static void Main()
    {
        var sw = new StreamWriter("Close.txt");
        sw.WriteLine("Hello World");
        sw.Close(); // closes writer and underlying stream
    }
}
