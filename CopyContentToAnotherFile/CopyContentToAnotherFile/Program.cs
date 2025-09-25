namespace CopyContentToAnotherFile
{
    internal class Program
    {
        static void Main(string[] args)
        {
            File.Copy("file1.txt", "file2.txt");
            Console.WriteLine("Execution Completed");
        }
    }
}
