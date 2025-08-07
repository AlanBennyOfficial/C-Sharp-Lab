using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CheckNumber
{
    public class CheckNumber
    {
        public void Determine(int number)
        {

            if (number > 0)
            {
                Console.WriteLine(number + " is Positive");
            }
            else if (number < 0)
            {
                Console.WriteLine(number + " is Negative");
            }
            else
            {
                Console.WriteLine("The Number is Zero. ");
            }

        }

    }
}
