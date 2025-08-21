sealed class Animal
{
    public string Name;
    public int ageInMonth;

    public void Move()
    {
        Console.WriteLine("Moving...");
    }
    public void Eat()
    {
        Console.WriteLine("Eating...");
    }
}

internal class Program
{
    static void Main(string[] args)
    {
        Animal a1 = new Animal();
        a1.Name = "Dog";
        a1.ageInMonth = 1;
        a1.Move();
        a1.Eat();
    }
}

