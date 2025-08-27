/*
 * 1. Develop a C# program to create a class named shape. Create three sub classes namely: 
 * circle, triangle and square, each class has two member functions named draw () and erase (). 
 * Demonstrate polymorphism concepts by developing suitable  methods, defining member data and main program. 
 */

class Shape
{
    public void Draw()
    {
        Console.WriteLine("Drawing a shape..");
    }
    public void Erase()
    {
        Console.WriteLine("Erasing the Shape...");
    }
}
class Circle : Shape
{
    public void Draw()
    { 
        Console.WriteLine("Drawing a Circle..."); 
    }
    public void Erase()
    {
        Console.WriteLine("Erasing the Circle...");
    }
}
class Triangle : Shape
{
    public void Draw()
    {
        Console.WriteLine("Drawing a Triangle...");
    }
    public void Erase()
    {
        Console.WriteLine("Erasing the Triangle...");
    }
}
class Square : Shape
{
    public void Draw()
    {
        Console.WriteLine("Drawing a Square...");
    }
    public void Erase()
    {
        Console.WriteLine("Erasing the Square...");
    }
}
class Program
{
    public static void Main(string[] args)
    {
        Circle c1 = new Circle();
        c1.Draw();
        c1.Erase();
    }
}