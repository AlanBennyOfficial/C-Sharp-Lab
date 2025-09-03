using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter operator (+,-,*,/,%) : ");
        char op = Console.ReadKey().KeyChar;
        Console.WriteLine();
        Console.Write("Enter first number: ");
        double a = double.Parse(Console.ReadLine());
        Console.Write("Enter second number: ");
        double b = double.Parse(Console.ReadLine());
        double res = 0;
        switch (op)
        {
            case '+': res = a + b; break;
            case '-': res = a - b; break;
            case '*': res = a * b; break;
            case '/': res = a / b; break;
            case '%': res = a % b; break;
            //default: Console.WriteLine("Invalid Operator!");break;
        }
        Console.WriteLine("Result: " + res);
    }
}