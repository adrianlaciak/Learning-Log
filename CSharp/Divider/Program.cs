namespace Divider;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Program sprawdzający czy druga liczba jest dzielnikiem pierwszej.");
        
        Console.Write("Proszę podać pierwszą liczbę całkowitą: ");
        int pierwsza =  int.Parse(Console.ReadLine());
        
        Console.Write("Proszę podać drugą liczbę całkowitą: ");
        int druga = int.Parse(Console.ReadLine());

        if (pierwsza % druga == 0)
        {
            Console.WriteLine($"{druga} jest dzielnikiem {pierwsza}");
        }
        else
        {
            Console.WriteLine($"{druga} nie jest dzielnikiem  {pierwsza}");
        }
    }
}