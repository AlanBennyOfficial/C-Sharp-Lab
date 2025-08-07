using System;

public class HelloWorld
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Enter a number:");
        int n = Convert.ToInt32(Console.ReadLine());
        int temp = n;

        int sum = 0;
        int power = 0;
        //Count the digits
        while (n > 0)
        {
            power++;
            n /= 10;
        }
        n = temp;
        // Add the powers of each digit
        while (n > 0)
        {
            sum += (int)Math.Pow(n % 10, power);
            n /= 10;
        }
        if (temp == sum)
        {
            Console.WriteLine("It is an Armstrong Number!");
        }
        else
        {
            Console.WriteLine("It is not an Armstrong Number!");
        }
    }
}