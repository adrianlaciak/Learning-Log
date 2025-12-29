import os

def clear_screen():
    print("\n" * 100)

clear_screen()

zus = 0
skladka_zdrowotna = 0
podatek = 0

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
    while True:
        czy_skladka_chorobowa = input("Czy odliczyć składkę chorobową 2,45%?\n[Y]es\n[N]o\nProszę wybrać spośród podanych: ").lower()
        if czy_skladka_chorobowa in ('y','n'):
            break
        else:
            print("Proszę wybrać Y lub N.")
    while True:
        czy_student = input("Czy jesteś studentem?\n[Y]es\n[N]o\nProszę wybrać spośród podanych: ").lower()
        if czy_student in ('y','n'):
            break
        else:
            print("Proszę wybrać Y lub N.")

elif umowa == 3:
    print("Wybrano Umowę o Dzieło.")
else:
    print("Wybrano B2B.")

skladka_emerytalna = 0.0976
skladka_rentowa = 0.0150
skladka_chorobowa = 0.0245
#
#1. Umowa o Pracę
#
#2. Umowa Zlecenie
if umowa == 2:
    if wiek < 26 and czy_student == 'y':
        netto = brutto
    else:
        if czy_skladka_chorobowa == 'y':
            zus = brutto * (skladka_rentowa + skladka_emerytalna + skladka_chorobowa)
        else:
            zus = brutto * (skladka_rentowa + skladka_emerytalna)

        podstawa_zdrowotna = brutto - zus
        skladka_zdrowotna = podstawa_zdrowotna * 0.09

        if wiek < 26:
            podatek = 0
        else:
            koszty_uzyskania_przychodu = podstawa_zdrowotna * 0.20
            podstawa_podatku = podstawa_zdrowotna - koszty_uzyskania_przychodu
            podatek = (podstawa_podatku * 0.12) - 300
            if podatek < 0: podatek = 0


        netto = brutto - zus - skladka_zdrowotna - podatek
clear_screen()
print("P O D S U M O W A N I E")
print(f"Kwota brutto: {brutto:>10.2f} PLN")
print(f"ZUS + NFZ: {zus + skladka_zdrowotna:>10.2f} PLN")
print(f"Podatek PIT: {podatek:>10.2f} PLN")
print(f"Kwota netto: {netto:>10.2f} PLN")