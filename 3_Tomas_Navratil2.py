"""
Identifikační údaje o autorovi projektu:
    Jméno a příjmení: Tomáš Navrátil
    tel.: 776 261 616
    e-mail: tomas.navratil16@gmail.com
"""
# importuje os
import os

# Získání cesty k programu
cesta_k_programu = os.path.abspath(__file__)
# Získání cesty k souboru - batohy_vstup.txt
cesta_k_souboru = os.path.join(os.path.dirname(cesta_k_programu), 'batohy_vstup.txt')

# Vypíše informace o cestě k programu a vstupnímu souboru 
print("Vyhledání společných věcí v každém batohu")
print("*" * 41)
print()
print(f"Cesta k aktuálně spuštěnému programu:\n {cesta_k_programu}")
print()
print(f"Cesta ke vstupnímu souboru s popisem batohů:\n {cesta_k_souboru}")
print()
print("Obsah batohů v první a druhé polovině (odděleno mezerou)")
print("*" * 56)
print()

# Funkce pro výpočet priority písmena
def priorita_znak(pismeno):
    if 'a' <= pismeno <= 'z':
        return ord(pismeno) - ord('a') + 1
    elif 'A' <= pismeno <= 'Z':
        return ord(pismeno) - ord('A') + 27
    return 0

# Otevření souboru a načtení dat
with open(cesta_k_souboru, 'r') as soubor:
    seznam_batohu = soubor.readlines()

celkovy_soucet_priorit = 0
vsechny_spolecne_predmety = [] 

for batoh in seznam_batohu:
    batoh = batoh.strip()
    delka = len(batoh)
    polovina = delka // 2
    cast1 = batoh[:polovina]
    cast2 = batoh[polovina:]

    # Hledání společných předmětů
    spolecne = set(cast1) & set(cast2)
    vsechny_spolecne_predmety.extend(spolecne)  # Přidání do hlavního seznamu

    for predmet in spolecne:
        # Zjištění výskytu předmětu v batohu
        pocet_vyskytu = batoh.count(predmet)
        # Výpočet priority pomocí funkce - priorita_znak
        priorita = priorita_znak(predmet) * pocet_vyskytu
        celkovy_soucet_priorit += priorita

    print(f"{cast1} {cast2}")
    print()

# Výpis zjištěných informací
print("Zjištěné informace o batozích")
print("*" * 30)
print()
print("Všechny společné předměty ze všech batohů:", vsechny_spolecne_predmety)
print()
print("Celkový součet priorit všech batohů:", celkovy_soucet_priorit)