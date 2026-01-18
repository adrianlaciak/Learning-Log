namespace Calculator;

/*Napisz program – prosty kalkulator, który wczytuje od użytkownika wartości dwóch
zmiennych typu double oraz znak operacji (+ lub – lub * lub /), 
a następnie wyświetla wynik operacji dla podanych wartości. 
Przykładowo użytkownik wprowadził znak „+” i liczby 1,5
oraz 2,5, program powinien wyświetlić sumę obu liczb, czyli 4,0.*/

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Proszę podać pierwszą liczbę: ");
        double x = double.Parse(Console.ReadLine());
        Console.WriteLine("Proszę podać znak operacji: ");
        string znak = Console.ReadLine();
        Console.WriteLine("Proszę podać drugą liczbę: ");
        double y = double.Parse(Console.ReadLine());
        double wynik = 0;
        
        switch (znak)
        {
            case "+":
                wynik = x + y;
                break;
            case "-":
                wynik = x - y;
                break;
            case "*":
                wynik = x * y;
                break;
            case "/":
                wynik = x / y;
                break;
        }
        
        Console.WriteLine($"{x} {znak} {y} = {wynik}");
    }
}