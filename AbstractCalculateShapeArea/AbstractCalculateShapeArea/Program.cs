namespace AbstractCalculateShapeArea
{
    using System;
    abstract class Shape
    {
        public abstract double CalculateArea();
    }
    class Circle : Shape
    {
        private double radius;
        public Circle(double radius)
        {
            this.radius = radius;
        }
        public override double CalculateArea()
        {
            return Math.PI * radius * radius;
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            Shape c1 = new Circle(5.0);
            Console.WriteLine("Area of the circle: "+ c1.CalculateArea());
            
        }
    }
}
