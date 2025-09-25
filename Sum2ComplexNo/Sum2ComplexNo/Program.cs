namespace Sum2ComplexNo
{
    public class Complex
    {
        public int real {  get; set; }
        public int imaginary { get; set; }
        public Complex(int r, int i)
        {
            real = r;
            imaginary = i;
        }
        public static Complex operator +(Complex a, Complex b)
        {
            return new Complex(a.real+b.real, a.imaginary+b.imaginary);
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            Complex a = new Complex(10, 2);
            Complex b = new Complex(20, 1);
            Console.WriteLine(a + b);
        }
    }
}
