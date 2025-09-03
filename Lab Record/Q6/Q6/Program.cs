public interface Resizable
{
    void resizeWidth(int width);
    void resizeHeight(int height);
}
public class Rectangle(int width, int height) : Resizable
{
    public void resizeWidth(int w)
    {
        Console.WriteLine($"New width: {w}");
    }
    public void resizeHeight(int h)
    {
        Console.WriteLine($"New Height: {h}");
    }
}
class Program
{
    static void Main(string[] args)
    {
        Rectangle r1 = new Rectangle(10, 5);
        r1.resizeWidth(15);
        r1.resizeHeight(25);
    }
}