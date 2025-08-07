namespace CheckNumber
{
    public class Program
    {
        static void Main(string[] args)
        {
            CheckNumber check = new CheckNumber();
            check.Determine(-12);
            check.Determine(9);
            check.Determine(0);
        }
    }
}
