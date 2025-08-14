namespace AbstractCalculateShapeArea
{
    using System;
    abstract class Shape
    {
        abstract public double CalculateArea();
    }
    abstract class Circle : Shape
    {
        public double radius;
        public override double CalcuteArea(double radius)
        {
            return Math.PI * radius * radius;
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            Shape c1 = new Circle();
            Console.WriteLine($"Area of the circle: {c1.CalculateArea(5.0)}");
            
        }
    }
}
