namespace LINQ_Where
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<int> list = new List<int>() { 1, 2, 3, 4 };

            var result = list.Where(x => x>2);

            foreach (var r in result)
            {
                Console.WriteLine(r);
            }
        }
    }
}
