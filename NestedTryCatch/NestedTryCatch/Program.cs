namespace NestedTryCatch
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int divisor = 0;
            try
            {
                try
                {
                    int divideByZero = 6 / divisor;
                }
                catch (IndexOutOfRangeException e)
                {
                    Console.WriteLine("Inner catch is executed: " + e.Message);
                }
            }
            catch (DivideByZeroException ex)
            {
                Console.WriteLine("Outer catch executed: " + ex.Message);
            }
        }
    }
}
