using System;
using System.IO;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        using (var sw = new StreamWriter("WriteAsync.txt"))
        {
            await sw.WriteAsync("Hello Async (WriteAsync)"); // writes without newline
            await sw.FlushAsync();
        }
    }
}
