namespace HowManyNumbers;

/*Napisz program obliczający ile kolejnych liczb całkowitych (rozpoczynając od wartości
1) należy dodać do siebie, aby suma przekroczyła wartość 100.*/

class Program
{
    static void Main(string[] args)
    {
        int wartosc = 100;
        int suma = 0;
        int licznik = 0;

        for (int i = 1; suma <= wartosc; i++)
        {
            suma += i;
            licznik++;
        }
        Console.WriteLine($"Potrzeba {licznik} liczb.");
    }
}