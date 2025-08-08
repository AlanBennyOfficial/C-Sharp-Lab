using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Square
{
    public class Square
    {
        public void FindSquare(int number)
        {
            int result = number * number;
            Console.WriteLine("Square of "+number+ " is "+ result);
        }
    }
}
