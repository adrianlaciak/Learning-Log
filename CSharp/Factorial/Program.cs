namespace Factorial;

/*
Napisz program obliczający n! (n silnia), gdzie n jest podane przez użytkownika.
*/

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Proszę podać liczbę: ");
        int n =  int.Parse(Console.ReadLine());
        int wynik = 1;
        for (int i = 1; i <= n; i++)
        {
            wynik *= i;
        }
        Console.WriteLine($"{n}! = {wynik}");
    }
}