using System;

delegate void MyDelegate();
class Program
{
    static void Method1()
    {
        Console.WriteLine("This is method 1");
    }
    static void Method2()
    {
        Console.WriteLine("This is method 2");
    }
    static void Main()
    {
        MyDelegate d= Method1;
        d += Method2;
        d();
    }
}