using System.ComponentModel.DataAnnotations;

namespace ReverseWord
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter your string: ");
            string str = Console.ReadLine();

            string[] arr = str.Split(" ").ToArray();
            for (int i = arr.Length - 1; i >= 0; i--)
            {
                Console.Write($"{arr[i]} ");
            }
            
        }
    }
}
