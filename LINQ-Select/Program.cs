namespace LINQ_Select
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<int> list = new List<int>() { 1,2,3,4};

            var result = list.Select(x => x*x );

            foreach (var r in result)
            {
                Console.WriteLine(r);
            }
        }
    }
}
