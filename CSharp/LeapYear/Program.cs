namespace LeapYear;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Program sprawdzający czy podany rok jest rokiem przestępnym.");
        Console.WriteLine();

        Console.WriteLine("Proszę podać rok");
        int rok =  int.Parse(Console.ReadLine());

        if (rok % 4 == 0 && rok % 100 != 0 || rok % 400 == 0)
        {
            Console.WriteLine($"Rok {rok} jest przestępny.");
        }
        else
        {
            Console.WriteLine($"Rok {rok} nie jest przestępny.");
        }
    }
}