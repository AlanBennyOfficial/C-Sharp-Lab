namespace PaymentDetails
{   
    interface IPayment
    {
        public void MakePayment(double amount);
    }
    class CreditCardPayment:IPayment
    {
        public void MakePayment(double amount)
        {
            Console.WriteLine($"Payment of INR {amount} made via Credit Card");
        }
    }
    class PayPalPayment:IPayment
    {
        public void MakePayment(double amount)
        {
            Console.WriteLine($"Payment of INR {amount} made via PayPal");
        }
    }
    class UPIpayment : IPayment
    {
        public void MakePayment(double amount)
        {
            Console.WriteLine($"Payment of INR {amount} made via UPI");
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            CreditCardPayment c1 = new CreditCardPayment();
            c1.MakePayment(5000.0);
            Console.WriteLine();

            PayPalPayment p1 = new PayPalPayment();
            p1.MakePayment(2000.0);
            Console.WriteLine() ;

            UPIpayment u1 = new UPIpayment();
            u1.MakePayment(1000.0);
        }
    }
}
