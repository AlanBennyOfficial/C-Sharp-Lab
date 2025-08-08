using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Reverse
{
    public class ReverseNumber
    {
        public void Reverse(int number)
        {
            int rev = 0;
            while (number > 0)
            {
                int digit = number % 10;
                rev = rev * 10 + digit;
                number = number / 10;
            }
            Console.WriteLine("Reverse of Number is :" +rev); 
        }
    }
}
