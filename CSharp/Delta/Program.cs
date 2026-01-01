namespace Delta;

/*Napisz program, który oblicza deltę dla równania kwadratowego ax2 + bx + c = 0. 
Program ma prosić użytkownika o podanie współczynników równania a, b oraz c. Wzór: b2 - 4ac.*/

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Proszę podać a:");
        double a = double.Parse(Console.ReadLine());
        
        Console.WriteLine("Proszę podać b:");
        double b = double.Parse(Console.ReadLine());
        
        Console.WriteLine("Proszę podać c:");
        double c = double.Parse(Console.ReadLine());
        
        double delta = Math.Pow(b, 2) - 4 * a * c;
        Console.WriteLine($"Delta dla równania: {a}x² + {b}x + {c} = 0 wynosi {Math.Round(delta, 2)}.");
    }
}