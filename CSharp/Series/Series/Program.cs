namespace Series

/*    Napisz program obliczający sumę szeregu W(n)=1 – 2 + 3 – 4 + ...± n, gdzie n jest
dowolną liczbą naturalną, którą program ma wczytać.*/

{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Proszę podać liczbę: ");
            int n = int.Parse(Console.ReadLine());
            int suma_plus = 0;
            int suma_minus = 0;
            for (int i = 1; i <= n; i++)
            {
                if (i % 2 == 0)
                {
                    suma_minus += i;
                }
                else
                {
                    suma_plus += i;
                }
            }
            int wynik = suma_plus - suma_minus;
            Console.WriteLine($"Suma szeregu wynosi {wynik}.");
        }
    }
}
