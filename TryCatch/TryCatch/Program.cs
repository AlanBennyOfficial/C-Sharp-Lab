namespace TryCatch
{
    internal class Program
    {
        static void Main(string[] args)
        {
            try
            {
                Console.Write("Enter the first number: ");
                int num1 = Convert.ToInt32(Console.ReadLine());
                Console.Write("Enter the second number: ");
                int num2 = Convert.ToInt32(Console.ReadLine());
                int result = num1 / num2;
                Console.WriteLine($"The result of {num1} divided by {num2} is {result}");
            }
            catch (DivideByZeroException)
            {
                Console.WriteLine("Error: Cannot divide by zero!");
            }
            catch (FormatException)
            {
                Console.WriteLine("Error: Invalid input format! Please enter numeric values.");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An unexpected error occurred: {ex.Message}");
            }
            finally
            {
                Console.WriteLine("Execution completed.");
            }
        }
    }
}
