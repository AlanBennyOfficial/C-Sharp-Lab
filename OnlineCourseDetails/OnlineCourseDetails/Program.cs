namespace OnlineCourseDetails
{
    class Study
    {
        protected void CourseDetails()
        {
            Console.WriteLine("This is a course on C# programming.");
        }
    }
    class OnlineCourse : Study
    {
        public void CourseInfo() 
        { 
            CourseDetails();
            Console.WriteLine("This course is available online.");
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            OnlineCourse o1 = new OnlineCourse();
            o1.CourseInfo();
        }
    }
}
