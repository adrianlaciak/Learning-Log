namespace BMI;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Kalkulator BMI");
        Console.WriteLine();
        
        Console.Write("Proszę podać wagę w kilogramach (np. 70,50): ");
        double masa = double.Parse(Console.ReadLine());
        
        Console.Write("Proszę podać wzrost w centymetrach (np. 180,2): ");
        double wzrost_cm = double.Parse(Console.ReadLine());
        Console.WriteLine();
        
        double wzrost = wzrost_cm / 100.0;
        double bmi = Math.Round(masa / Math.Pow(wzrost, 2), 2);
        if (bmi > 30)
        {
            Console.WriteLine("---Otyłość---");
        }
        else if (bmi >= 25)
        {
            Console.WriteLine("---Nadwaga---");
        }
        else if (bmi >= 18.5)
        {
            Console.WriteLine("---Prawidłowa masa ciała---");
        }
        else
        {
            Console.WriteLine("---Niedowaga---");
        }
        Console.WriteLine($"Twoje bmi wynosi {bmi}.");
    }
}