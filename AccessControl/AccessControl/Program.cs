using System;
//using System.Diagnostics.CodeAnalysis;

//class Age
//{
//    private int age;
//    public void ShowAge(int age)
//    {
//        Console.WriteLine("Age = " + age);
//    }
//}
//class display
//{
//    static void Main(string[] args) { 
//        Age a = new Age();
//        a.ShowAge(23);
//    }
//}

class Animal
{
    protected void MakeSound()
    {
        Console.WriteLine("Animal sounds...");
    }
}

class Dog : Animal
{
    public void Bark()
    {
        MakeSound();
        Console.WriteLine("Dog Sounds...");
    }
}
class display
{
    static void Main(string[] args)
    {
        Dog d = new Dog();
        d.Bark();
    }
}