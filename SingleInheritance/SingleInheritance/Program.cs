namespace SingleInheritance
{
    public class Animal
    {
        public void Speak()
        {
            Console.WriteLine("Animal sounds");
        }
    }
    public class Dog : Animal
    {
        public void Bark()
        {
            Console.WriteLine("Bark!");
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            Dog d1 = new Dog();
            d1.Speak();
            d1.Bark();
        }
    }
}
