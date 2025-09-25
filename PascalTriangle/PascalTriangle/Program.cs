namespace PascalTriangle
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter the number of rows: ");
            int rows = Convert.ToInt32(Console.ReadLine());

            for (int i = 1; i <= rows; i++) // Outer loop for rows
            {
                // print leading spaces
                for (int j = 1; j <= (rows - i); j++)
                {
                    Console.Write(" ");
                }

                // print asterisks
                for (int k = 1; k <= i; k++)
                {
                    Console.Write("1");
                }
                Console.WriteLine(); // Move to the next line
            }
        }
    }
}
