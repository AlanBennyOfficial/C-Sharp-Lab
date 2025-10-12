using System.IO;

class Program
{
    static void Main()
    {
        using (var sw = new StreamWriter("WriteLine.txt"))
        {
            sw.WriteLine("Hello World"); // ends with newline
        }
    }
}
