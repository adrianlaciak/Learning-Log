namespace UserStop;

/*Napisz program pobierający od użytkownika liczby całkowite. Program ma pobierać te
liczby do czasu, gdy użytkownik wprowadzi wartość 0 (zero). Wynikiem działania programu
ma być informacja o sumie wprowadzonych przez użytkownika liczb.*/

class Program
{
    static void Main(string[] args)
    {
        int suma = 0;
        int x = 1;
        while (x != 0)
        {
            Console.WriteLine("Proszę podać liczbę: ");
            x = int.Parse(Console.ReadLine());
            suma += x;
        }
        Console.WriteLine($"Suma podanych liczb wynosi {suma}.");
    }
}