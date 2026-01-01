import os


def clear_screen():
    print("\n" * 100)


clear_screen()

zus = 0
skladka_zdrowotna = 0
podatek = 0
netto = 0

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
    umowa = input(
        "Proszę wybrać źródło dochodu spośród podanych:\n[1] Umowa o Pracę\n[2] Umowa Zlecenie\n[3] Umowa o Dzieło\n[4] B2B\nUmowa numer: ")
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
        czy_skladka_chorobowa = input(
            "Czy odliczyć składkę chorobową 2,45%?\n[Y]es\n[N]o\nProszę wybrać spośród podanych: ").lower()
        if czy_skladka_chorobowa in ('y', 'n'):
            break
        else:
            print("Proszę wybrać Y lub N.")
    while True:
        czy_student = input("Czy jesteś studentem?\n[Y]es\n[N]o\nProszę wybrać spośród podanych: ").lower()
        if czy_student in ('y', 'n'):
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
# 1. Umowa o Pracę
if umowa == 1:
    zus = brutto * (skladka_rentowa + skladka_emerytalna + skladka_chorobowa)
    podstawa_zdrowotna = brutto - zus
    skladka_zdrowotna = podstawa_zdrowotna * 0.09
    if wiek < 26:
        podatek = 0
    else:
        koszty_uzyskania_przychodu = 250
        podstawa_podatku = podstawa_zdrowotna - koszty_uzyskania_przychodu
        podatek = (podstawa_podatku * 0.12) - 300
        if podatek < 0: podatek = 0

    netto = brutto - zus - skladka_zdrowotna - podatek
# 2. Umowa Zlecenie
elif umowa == 2:
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

# 3. Umowa o Dzieło
elif umowa == 3:
    if wiek < 26:
        podatek = 0
    else:
        koszty_uzyskania_przychodu = brutto * 0.20
        podstawa_podatku = brutto - koszty_uzyskania_przychodu
        podatek = podstawa_podatku * 0.12
    netto = brutto - podatek

# 4. B2B
elif umowa == 4:
    while True:
        forma_opodatkowania = input(
            "Proszę wybrać preferowaną formę opodatkowania: \n[1] Ryczałt\n[2] Podatek Liniowy\n[3] Skala podatkowa\nWybrana forma: ")
        try:
            forma_opodatkowania = int(forma_opodatkowania)
            if 1 <= forma_opodatkowania <= 3:
                break
            else:
                print("Proszę wybrać liczbę od 1 do 3")
        except ValueError:
            print("Proszę wybrać liczbę od 1 do 3")

    clear_screen()

    while True:
        wybor_zus = input("Proszę wybrać stawkę ZUS:\n[1] Mały ZUS\n[2] Duży ZUS\nWybór ZUS: ")
        try:
            wybor_zus = int(wybor_zus)
            if wybor_zus in (1, 2):
                break
            else:
                print("Proszę wybrać liczbę od 1 do 2.")
        except ValueError:
            print("Proszę wybrać liczbę od 1 do 2.")
    if wybor_zus == 1:
        zus = 405
    else:
        zus = 1750

    clear_screen()

    if forma_opodatkowania == 1:
        while True:
            stawka_ryczaltu = input("Proszę wybrać stawkę ryczłtu: \n[1] 8,5%\n[2] 12%\n[3] 15%\nWybrana stawka: ")
            try:
                stawka_ryczaltu = int(stawka_ryczaltu)
                if 1 <= stawka_ryczaltu <= 3:
                    break
                else:
                    print("Proszę wybrać liczbę od 1 do 3.")
            except ValueError:
                print("Proszę wybrać liczbę od 1 do 3.")

        if stawka_ryczaltu == 1:
            stawka_ryczaltu = 0.085
        elif stawka_ryczaltu == 2:
            stawka_ryczaltu = 0.12
        else:
            stawka_ryczaltu = 0.15

        przychod_roczny = brutto * 12

        if przychod_roczny <= 60000:
            skladka_zdrowotna = 419
        elif przychod_roczny <= 300000:
            skladka_zdrowotna = 699
        else:
            skladka_zdrowotna = 1258

        podstawa_opodatkowania = brutto - (zus * 0.5)
        podatek = podstawa_opodatkowania * stawka_ryczaltu

    else:
        while True:
            koszty_firmowe = input("Proszę podać miesięczne koszty prowadzenia działalności: ")
            try:
                koszty_firmowe = float(koszty_firmowe)
                if koszty_firmowe < 0:
                    print("Kwota nie może być mniejsza od 0.")
                    continue
                elif koszty_firmowe * 100 == int(koszty_firmowe * 100):
                    break
                else:
                    print("Błąd: Kwota nie może mieć więcej niż 2 miejsca po przecinku (grosze).")
                    continue
            except ValueError:
                print("Proszę podać kwotę w formacie zmiennoprzecinkowym (np. 150.30).")

        dochod = brutto - koszty_firmowe - zus

        if forma_opodatkowania == 2:
            skladka_zdrowotna = dochod * 0.049
            podatek = dochod * 0.19

        else:
            skladka_zdrowotna = dochod * 0.09

            if dochod <= 10000:
                podatek = dochod * 0.12 - 300
            else:
                nadwyzka = dochod - 10000
                podatek = 1200 + (nadwyzka * 0.32) - 300

        if podatek < 0: podatek = 0

        if skladka_zdrowotna < 419.46: skladka_zdrowotna = 419.46

    netto = brutto - zus - skladka_zdrowotna - podatek

clear_screen()
print("P O D S U M O W A N I E")
print(f"Kwota brutto: {brutto:>10.2f} PLN")
print(f"ZUS + NFZ: {zus + skladka_zdrowotna:>10.2f} PLN")
print(f"Podatek PIT: {podatek:>10.2f} PLN")
print(f"Kwota netto: {netto:>10.2f} PLN")
