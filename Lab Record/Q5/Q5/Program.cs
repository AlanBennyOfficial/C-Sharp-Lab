using System;
abstract class Shape
{
    public abstract void CalculateArea();
    public abstract void CalculatePerimeter();
}
class Circle(double r) : Shape
{
    public override void CalculateArea() => Console.WriteLine("Area = " + 3.14 * r * r);
    
    public override void CalculatePerimeter() => Console.WriteLine("Perimeter = " + 2*3.14*r);
}
class Triangle(double a, double b, double c, double h) : Shape
{
    public override void CalculateArea() => Console.WriteLine("Area = " + 0.5*b*h);
    
    public override void CalculatePerimeter() => Console.WriteLine("Perimeter = " + a+b+c);
}
class Program
{
    static void Main(string[] args)
    {
        Triangle t1 = new Triangle(5.0, 10.0, 6.0, 10.0); // a+b>c , a+c>b
        t1.CalculatePerimeter();
        t1.CalculateArea();

        Circle c1 = new Circle(5.0);
        c1.CalculatePerimeter();
        c1.CalculateArea();
    }
}