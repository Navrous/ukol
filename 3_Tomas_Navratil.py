
from curses.ascii import islower
import os

cesta_programu = os.path.dirname(os.path.abspath(__file__))
nova_cesta = os.path.join(cesta_programu, "batohy_vstup.txt")


#def 
def cislo_pismene(pismeno):
    if pismeno.islower():
        cislo = ord(pismeno) - ord("a") + 1
    else:
        cislo = ord(pismeno) - ord("A") + 27
    return cislo

def rozdel_vetu(veta):
    delka = len(veta)
    polovna = delka // 2
    cast1 = veta[:polovna]
    cast2 = veta[polovna:]
    return cast1 + cast2

print("Vyhledání společných věcí v každém batohu")
print("*"*41)
print()
print(f"Cesta k aktuálně spuštěnému programu:\n {cesta_programu}")
print()
print(f"Cesta ke vstupnímu souboru s popisem batohů:\n {nova_cesta}")
print()
print("Obsah batohů v první a druhé polovině (odděleno mezerou)")
print("*"*56)
print()

with open(nova_cesta, "r") as file:
    obsah = file.readlines()

print(rozdel_vetu(obsah[0:10]))


print()
#for cislo in obsah:
    #print(cislo_pismene(obsah))

#for znak in seznam1, seznam2:
    #if znak in seznam1 == znak in seznam2:
        #print(znak)



print("Zjištěné informace o batozích")
print("*"*30)
print()
print("Seznam společných položek v každém batohu: {}")
print()
print("Celkový součet priorit u všech batohů: {}")
    