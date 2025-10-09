using System;

public class Stack
{
    private int[] items;
    private int top = -1;

    public int Size { get; set; }

    public Stack(int size)
    {
        Size = size;
        items = new int[Size];
    }

    public void Push(int value)
    {
        if (top == Size - 1)
        {
            Console.WriteLine("Stack overflow");
        }
        else
        {
            items[++top] = value;
        }
    }

    public int Pop()
    {
        if (top == -1)
        {
            Console.WriteLine("Stack underflow");
            return -1; // invalid value (-1) to indicate failure
        }
        else
        {
            return items[top--];
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        Stack s = new Stack(3);
        s.Push(10);
        s.Push(20);
        s.Push(30);
        Console.WriteLine("Pop: " + s.Pop());
        Console.WriteLine("Pop: " + s.Pop());
        Console.WriteLine("Pop: " + s.Pop()); // Additional pop to test underflow
    }
}
