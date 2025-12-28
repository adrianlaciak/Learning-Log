import os

def clear_screen():
    print("\n" * 100)

clear_screen()

while True:
    brutto_input = input("Proszę podać kwotę brutto (np. 5000.50): ")
    try:
        # Próbujemy zamienić tekst na liczbę
        brutto = float(brutto_input)

        # Sprawdzamy, czy kwota nie ma więcej niż 2 miejsc po przecinku
        if (brutto * 100) != int(brutto * 100):
            print("Błąd: Kwota nie może mieć więcej niż 2 miejsca po przecinku (grosze).")
            continue

        if brutto <= 0:
            print("Błąd: Kwota musi być większa od zera.")
            continue

        # Jeśli wszystko jest ok, przerywamy pętlę
        break

    except ValueError:
        print("Błąd: To nie jest prawidłowa liczba. Użyj kropki jako separatora.")

clear_screen()

print(f"Przyjęta kwota do obliczeń: {brutto:.2f} PLN")

while True:
    wiek = input("Proszę podać swój wiek: ")
    try:
        wiek = int(wiek)
        break
    except ValueError:
        print("Proszę podać poprawny wiek w latach (np. 20)")

clear_screen()

print(f"Przyjęto do obliczeń wiek {wiek} lat")

while True:
    umowa = input("Proszę wybrać źródło dochodu spośród podanych:\n[1] Umowa o Pracę\n[2] Umowa Zlecenie\n[3] Umowa o Dzieło\n[4] B2B\nUmowa numer: ")
    try:
        umowa = int(umowa)
        if 1 <= umowa <= 4:
            break
        else:
            print("Proszę wpisać odpowiednią liczbę: 1, 2, 3 lub 4.")
    except ValueError:
        print("Proszę wpisać odpowiednią liczbę: 1, 2, 3 lub 4.")

clear_screen()

if umowa == 1:
    print("Wybrano Umowę o Pracę.")
elif umowa == 2:
    print("Wybrano Umowę Zlecenie.")
elif umowa == 3:
    print("Wybrano Umowę o Dzieło.")
else:
    print("Wybrano B2B.")

netto = 0
#
#1. Umowa o Pracę
#
#2. Umowa Zlecenie
if umowa == 2:
    if wiek < 26:
        netto = brutto

print(f"Kwota brutto: {brutto:.2f}\nKwota netto: {netto:.2f}")
