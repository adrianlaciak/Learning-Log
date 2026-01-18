namespace QuadraticEquation;

/*Napisz program obliczający liczbę pierwiastków równania kwadratowego. Program ma
prosić użytkownika o podanie współczynników równania, a następnie ma wyświetlić
stosowny komunikat.*/

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Równanie kwadratowe: ax2+bx+c=0");
        Console.WriteLine("Proszę podać a: ");
        double a = double.Parse(Console.ReadLine());
        Console.WriteLine("Proszę podać b: ");
        double b =  double.Parse(Console.ReadLine());
        Console.WriteLine("Proszę podać c: ");
        double c =  double.Parse(Console.ReadLine());

        double delta = Math.Pow(b, 2) - 4 * a * c;

        if (delta > 0)
        {
            Console.WriteLine($"Równanie {a}x2+{b}x+{c}=0 posiada dwa rozwiązania.");
        }
        else if (delta == 0)
        {
            Console.WriteLine($"Równanie {a}x2+{b}x+{c}=0 posiada jeden rozwiązanie.");
        }
        else
        {
            Console.WriteLine($"Równanie {a}x2+{b}x+{c}=0 nie posiada rozwiązań.");
        }
    }
}