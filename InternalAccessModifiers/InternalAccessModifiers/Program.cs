using System;
using ClassLibrary1;
namespace InternalAccessModifiers
{
    class Point
    {
        internal int x;
        internal int y;

        public void Test()
        {
            Console.WriteLine("Test() in point class");
            Console.WriteLine("Cerated a new point object inside");
        }
    }

    internal class Program:Point
    {
        static void Main(string[] args)
        {
            Point p = new Point();
            Program p1 = new Program();
            p1.Test();
            p.Test();
        }
    }
}
namespace N
{
    class Sample
    {
        public void Display()
        {
            InternalAccessModifiers.Point p = new InternalAccessModifiers.Point();
        }
    }
}
