namespace MultipleInheritance
{
    interface Cat
    {
        void MakeSound()
        {
            Console.WriteLine("Meow...");
        }
    }
    interface Dog
    {
        void MakeSound()
        {
            Console.WriteLine("Bark..");
        }
    }
    class Animal : Cat, Dog
    {
        public void MakeSound()
        {
            Console.WriteLine("Animal sounds...");
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            Animal a1 = new Animal();
            a1.MakeSound();
        }
    }
}
