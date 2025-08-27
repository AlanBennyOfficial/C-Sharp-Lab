public interface Resizeable
{
    void resizeWidth(int width);
    void resizeHeight(int height);
}
public class Rectangle(int width, int height) : Resizeable
{
    public void resizeWidth(int w)
    {
        Console.WriteLine($"Resizing width of rectangle to {w}");
    }
    public void resizeHeight(int h)
    {
        Console.WriteLine($"Resizing height of rectangle to {h}");
    }
}
class Program
{
    static void Main(string[] args)
    {
        Rectangle r1 = new Rectangle(10,5);
        r1.resizeWidth(10);
        r1.resizeHeight(20);
    }
}