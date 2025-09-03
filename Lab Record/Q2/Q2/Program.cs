using System;

class Program
{
    static void Main()
    {
        for (int i = 1; i <= 1000; i++)
        {
            int sum = 0, temp = i, len = i.ToString().Length;
            while (temp > 0)
            {
                int digit = temp % 10;
                sum += (int)Math.Pow(digit, len);
                temp /= 10;
            }
            if (sum == i) Console.WriteLine(i);
        }
    }
}