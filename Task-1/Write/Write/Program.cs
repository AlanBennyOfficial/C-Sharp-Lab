using System.IO;

class Program
{
    static void Main()
    {
        using (var sw = new StreamWriter("Write.txt"))
        {
            sw.Write("Hello World"); // no newline
        }
    }
}
