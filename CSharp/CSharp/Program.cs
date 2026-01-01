namespace Fahrenheit;

/*Napisz program przeliczający temperaturę w stopniach Celsjusza na temperaturę w
stopniach Fahrenheita. Program ma prosić użytkownika o podanie temperatury w stopniach
Celsjusza. Wzór: F = 32 + 9/5C.*/

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Proszę wpisać temperaturę w stopniach Celsjusza: ");
        double celsjusz = double.Parse(Console.ReadLine());
        double fahrenheit = 32 + celsjusz * 9.0 / 5.0;
        Console.WriteLine($"{celsjusz} stopni Celsjusza to {fahrenheit} stopni Fahrenheit'a.");
    }
}
