using System.IO;

class Program
{
    static void Main()
    {
        var sw = new StreamWriter("DisposeWrite.txt");
        sw.WriteLine("Hello World");
        sw.Dispose(); // explicitly release resources
    }
}
