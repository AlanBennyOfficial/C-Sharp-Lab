using System;
using System.IO;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        using (var sw = new StreamWriter("WriteLineAsync.txt"))
        {
            await sw.WriteLineAsync("Hello World"); // writes with newline
            await sw.FlushAsync();
        }
    }
}
