namespace LINQ_OrderBy
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<int> list = new List<int>() { 253, 5, 54, 53, 4365 };

            var result = list.OrderBy(x => x * x);

            foreach (var r in result)
            {
                Console.WriteLine(r);
            }
        }
    }
}
