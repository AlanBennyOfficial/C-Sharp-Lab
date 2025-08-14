namespace EncapsulationWithGetSetIncludingValidation
{
    class Person
    {
        private string name;
        private int age;
        public string Name
        {
            get { return name; }
            set
            {
                if (string.IsNullOrWhiteSpace(value))
                {
                    Console.WriteLine("Name cannot be null or empty.");
                }
                name = value;
            }
        }
        public int Age
        {
            get { return age; }
            set
            {
                if (value < 0 || value > 120)
                {
                    Console.WriteLine("Age must be between 0 and 120.");
                }
                age = value;
            }
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            Person p1 = new Person();
            p1.Name = "Alan";
            p1.Age = 20;
            Console.WriteLine($"Name: {p1.Name}, Age: {p1.Age}");
        }
    }
}
