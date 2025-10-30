namespace LINQ_OddOrEven
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<int> list = new List<int>() { 253, 5, 54, 53, 4365 };

            var result = list.OrderBy(x => x * x);

            foreach (var r in result)
            {
                if (r % 2 == 0)
                {
                    Console.WriteLine("Even: " + r);
                }
                else
                {
                    Console.WriteLine("Odd: " +r);
                }
            }
        }
    }
}
