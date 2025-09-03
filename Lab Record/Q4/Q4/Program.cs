class Shape
{
    public virtual void Draw() => Console.WriteLine("Drawing a shape..");
    public virtual void Erase() => Console.WriteLine("Erasing the Shape...");
}
class Circle : Shape
{
    public override void Draw() => Console.WriteLine("Drawing a Circle...");

    public override void Erase() => Console.WriteLine("Erasing the Circle...");
}
class Triangle : Shape
{
    public override void Draw() => Console.WriteLine("Drawing a Triangle...");
    
    public override void Erase() => Console.WriteLine("Erasing the Triangle...");
}
class Square : Shape
{
    public override void Draw() => Console.WriteLine("Drawing a Square...");

    public override void Erase() => Console.WriteLine("Erasing the Square...");
}
class Program
{
    public static void Main(string[] args)
    {
        //Circle c1 = new Circle();
        //c1.Draw();
        //c1.Erase();

        Shape[] lst = { new Circle(), new Triangle(), new Square() };

        foreach (Shape s in lst)
        {
            s.Draw();
            s.Erase();
            Console.WriteLine();
        }
    }
}