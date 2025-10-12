using System.IO;

class Program
{
    static void Main()
    {
        var sr = new StreamReader("CloseReader.txt");
        string line = sr.ReadLine();
        sr.Close(); // releases file handle
    }
}
