namespace BiggestNum;

/*Napisz program pobierający od użytkownika 3 liczby. Program ma wyświetlić wartość
największej z nich.*/

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Proszę podać 1 liczbę: ");
        double pierwsza = double.Parse(Console.ReadLine());
        Console.WriteLine("Proszę podać 2 liczbę: ");
        double druga =  double.Parse(Console.ReadLine());
        Console.WriteLine("Proszę podać 3 liczbę: ");
        double trzecia = double.Parse(Console.ReadLine());

        double najwieksza = pierwsza;
        if (druga > najwieksza)
        {
            najwieksza = druga;
        }

        if (trzecia > najwieksza)
        {
            najwieksza = trzecia;
        }
        
        Console.WriteLine($"Spośród liczb {pierwsza}; {druga}; {trzecia} największa to {najwieksza}.");

    }
}