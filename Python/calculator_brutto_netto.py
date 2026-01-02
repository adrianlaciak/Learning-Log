import os
import sys


# Function to clear the console screen safely
# Funkcja do bezpiecznego czyszczenia ekranu konsoli
def clear_screen():
    # Check if we are running in a real terminal / Sprawdzamy, czy działamy w prawdziwym terminalu
    if sys.stdout.isatty():
        if os.name == 'nt':
            os.system('cls')  # Windows
        else:
            # Linux/Mac - suppress errors if TERM is missing / Linux/Mac - ukryj błędy, jeśli brakuje TERM
            result = os.system('clear 2> /dev/null')
            if result != 0:
                print("\n" * 50)
    else:
        # Fallback for IDEs like PyCharm/VS Code output window / Zapasowe rozwiązanie dla okien wyjścia IDE
        print("\n" * 50)


clear_screen()

# Initialize variables / Inicjalizacja zmiennych
social_security = 0  # ZUS
health_insurance = 0  # Składka zdrowotna
income_tax = 0  # Podatek
net_amount = 0  # Kwota netto

# --- STEP 1: Get Gross Amount / KROK 1: Pobranie kwoty brutto ---
while True:
    gross_input = input("Please enter the gross amount (e.g., 5000.50): ")
    try:
        # Try to convert string to float / Próba zamiany tekstu na liczbę zmiennoprzecinkową
        gross_amount = float(gross_input)

        # Check decimal places / Sprawdzenie miejsca po przecinku
        if (gross_amount * 100) != int(gross_amount * 100):
            print("The amount cannot have more than 2 decimal places.")
            continue

        if gross_amount <= 0:
            print("The amount must be greater than zero.")
            continue

        # Break loop if correct / Przerwanie pętli, jeśli wszystko ok
        break

    except ValueError:
        print("Invalid number. Please use a dot as a separator.")

clear_screen()

print(f"Accepted amount for calculation: {gross_amount:.2f} PLN")

# --- STEP 2: Get Age / KROK 2: Pobranie wieku ---
while True:
    age_input = input("Please enter your age: ")
    try:
        age = int(age_input)
        break
    except ValueError:
        print("Please enter a valid age in years (e.g., 20)")

clear_screen()

print(f"Age accepted for calculation: {age} years")

# --- STEP 3: Choose Contract Type / KROK 3: Wybranie rodzaju umowy ---
while True:
    print("Please select the source of income:")
    print("[1] Employment Contract (Umowa o Pracę)")
    print("[2] Mandate Contract (Umowa Zlecenie)")
    print("[3] Specific Task Contract (Umowa o Dzieło)")
    print("[4] B2B (Business-to-Business)")
    contract_type = input("Contract number: ")

    try:
        contract_type = int(contract_type)
        if 1 <= contract_type <= 4:
            break
        else:
            print("Please enter a valid number: 1, 2, 3 or 4.")
    except ValueError:
        print("Please enter a valid number: 1, 2, 3 or 4.")

clear_screen()

# Handle specific contract details / Obsługa szczegółów konkretnej umowy
if contract_type == 1:
    print("Selected: Employment Contract.")

elif contract_type == 2:
    print("Selected: Mandate Contract.")
    # Ask about sickness insurance / Pytanie o składkę chorobową
    while True:
        deduct_sickness = input("Deduct sickness insurance 2.45%?\n[Y]es\n[N]o\nPlease select: ").lower()
        if deduct_sickness in ('y', 'n'):
            break
        else:
            print("Please select Y or N.")

    # Ask about student status / Pytanie o status studenta
    while True:
        is_student = input("Are you a student?\n[Y]es\n[N]o\nPlease select: ").lower()
        if is_student in ('y', 'n'):
            break
        else:
            print("Please select Y or N.")

elif contract_type == 3:
    print("Selected: Specific Task Contract.")

else:
    print("Selected: B2B.")

# Define constants / Definicja stałych
pension_contribution_rate = 0.0976  # Składka emerytalna
disability_contribution_rate = 0.0150  # Składka rentowa
sickness_contribution_rate = 0.0245  # Składka chorobowa

# --- CALCULATIONS / OBLICZENIA ---

# 1. Employment Contract / Umowa o Pracę
if contract_type == 1:
    social_security = gross_amount * (
                disability_contribution_rate + pension_contribution_rate + sickness_contribution_rate)
    health_basis = gross_amount - social_security
    health_insurance = health_basis * 0.09

    if age < 26:
        income_tax = 0
    else:
        tax_deductible_expenses = 250  # Koszty uzyskania przychodu
        tax_basis = health_basis - tax_deductible_expenses
        income_tax = (tax_basis * 0.12) - 300
        if income_tax < 0:
            income_tax = 0

    net_amount = gross_amount - social_security - health_insurance - income_tax

# 2. Mandate Contract / Umowa Zlecenie
elif contract_type == 2:
    if age < 26 and is_student == 'y':
        net_amount = gross_amount
    else:
        if deduct_sickness == 'y':
            social_security = gross_amount * (
                        disability_contribution_rate + pension_contribution_rate + sickness_contribution_rate)
        else:
            social_security = gross_amount * (disability_contribution_rate + pension_contribution_rate)

        health_basis = gross_amount - social_security
        health_insurance = health_basis * 0.09

        if age < 26:
            income_tax = 0
        else:
            tax_deductible_expenses = health_basis * 0.20
            tax_basis = health_basis - tax_deductible_expenses
            income_tax = (tax_basis * 0.12) - 300
            if income_tax < 0:
                income_tax = 0

        net_amount = gross_amount - social_security - health_insurance - income_tax

# 3. Specific Task Contract / Umowa o Dzieło
elif contract_type == 3:
    if age < 26:
        income_tax = 0
    else:
        tax_deductible_expenses = gross_amount * 0.20
        tax_basis = gross_amount - tax_deductible_expenses
        income_tax = tax_basis * 0.12
    net_amount = gross_amount - income_tax

# 4. B2B / Działalność gospodarcza
elif contract_type == 4:
    # Choose taxation form / Wybór formy opodatkowania
    while True:
        print("Please choose your preferred taxation form:")
        print("[1] Lump Sum (Ryczałt)")
        print("[2] Linear Tax (Podatek Liniowy)")
        print("[3] Tax Scale (Skala Podatkowa)")
        taxation_form = input("Selected form: ")
        try:
            taxation_form = int(taxation_form)
            if 1 <= taxation_form <= 3:
                break
            else:
                print("Please select a number between 1 and 3")
        except ValueError:
            print("Please select a number between 1 and 3")

    clear_screen()

    # Choose ZUS rate / Wybór stawki ZUS
    while True:
        print("Please select ZUS rate:")
        print("[1] Small ZUS (Mały ZUS)")
        print("[2] Big ZUS (Duży ZUS)")
        zus_choice = input("Your choice: ")
        try:
            zus_choice = int(zus_choice)
            if zus_choice in (1, 2):
                break
            else:
                print("Please select 1 or 2.")
        except ValueError:
            print("Please select 1 or 2.")

    if zus_choice == 1:
        social_security = 405
    else:
        social_security = 1750

    clear_screen()

    # Logic for Lump Sum / Logika dla Ryczałtu
    if taxation_form == 1:
        while True:
            print("Please select Lump Sum rate:")
            print("[1] 8.5%")
            print("[2] 12%")
            print("[3] 15%")
            lump_sum_rate_choice = input("Selected rate: ")
            try:
                lump_sum_rate_choice = int(lump_sum_rate_choice)
                if 1 <= lump_sum_rate_choice <= 3:
                    break
                else:
                    print("Please select a number between 1 and 3.")
            except ValueError:
                print("Please select a number between 1 and 3.")

        if lump_sum_rate_choice == 1:
            lump_sum_rate = 0.085
        elif lump_sum_rate_choice == 2:
            lump_sum_rate = 0.12
        else:
            lump_sum_rate = 0.15

        annual_revenue = gross_amount * 12

        # Health insurance thresholds for Lump Sum / Progi zdrowotne na ryczałcie
        if annual_revenue <= 60000:
            health_insurance = 419
        elif annual_revenue <= 300000:
            health_insurance = 699
        else:
            health_insurance = 1258

        tax_basis = gross_amount - (social_security * 0.5)
        income_tax = tax_basis * lump_sum_rate

    # Logic for Linear Tax or Tax Scale / Logika dla Liniowego lub Skali
    else:
        while True:
            business_costs_input = input("Please enter monthly business costs: ")
            try:
                business_costs = float(business_costs_input)
                if business_costs < 0:
                    print("Amount cannot be less than 0.")
                    continue
                elif business_costs * 100 == int(business_costs * 100):
                    break
                else:
                    print("Error: The amount cannot have more than 2 decimal places.")
                    continue
            except ValueError:
                print("Please enter a valid float amount (e.g. 150.30).")

        income = gross_amount - business_costs - social_security

        # Linear Tax / Podatek Liniowy
        if taxation_form == 2:
            health_insurance = income * 0.049
            income_tax = income * 0.19

        # Tax Scale / Skala Podatkowa
        else:
            health_insurance = income * 0.09

            if income <= 10000:
                income_tax = income * 0.12 - 300
            else:
                surplus = income - 10000
                income_tax = 1200 + (surplus * 0.32) - 300

        if income_tax < 0:
            income_tax = 0

        # Minimum health insurance / Minimalna składka zdrowotna
        if health_insurance < 419.46:
            health_insurance = 419.46

    net_amount = gross_amount - social_security - health_insurance - income_tax

# --- SUMMARY / PODSUMOWANIE ---
clear_screen()
print("S U M M A R Y")
print(f"Gross Amount:      {gross_amount:>10.2f} PLN")
print(f"ZUS + Health Ins.: {social_security + health_insurance:>10.2f} PLN")
print(f"Income Tax (PIT):  {income_tax:>10.2f} PLN")
print(f"Net Amount:        {net_amount:>10.2f} PLN")