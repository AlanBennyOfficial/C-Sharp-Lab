using System;
class car
{
    public string color;
    public string model;
    public void drive()
    {
        Console.WriteLine("i like driving");
    }
    class program
    {
        static void Main()
        {
            car c = new car();
            c.color = "red";
            Console.WriteLine("color is"+ c.color);
            c.drive();






        }
    }

}
