using System;

delegate void Greet();
class Program
{
    static void SayHello()
    {
        Console.WriteLine("Hello, Students!");
    }
    static void Main()
    {
        Greet greetDeldate = SayHello;
        greetDeldate();
    }
}