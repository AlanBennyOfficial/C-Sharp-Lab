namespace LuckyTicketNumbers
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Print a list of lucky ticket numbers between 1 and 100, multiples of 4 and 6 are considered lucky.
            Console.WriteLine("Lucky Ticket Numbers:");
            for(int i = 1; i <= 100; i++)
            {
                if (i % 4 == 0 && i % 6 == 0)
                {
                    Console.WriteLine(i);
                }
            }
        }
    }
}
