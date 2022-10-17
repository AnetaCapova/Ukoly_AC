def zkontroluj_delku_cisla(delka_cisla):
    if delka_cisla == 9 or delka_cisla == 13:
        return True
    else:
        return False



zadane_cislo = input("Zadejte prosím telefonní číslo bez mezer(!): ")
# zjistit správný formát
pocet_znaku_cisla = len(zadane_cislo)

zkontroluj_delku_cisla(pocet_znaku_cisla)
# print(pocet_znaku_cisla)

if zkontroluj_delku_cisla(pocet_znaku_cisla) == False:
    exit()

import math
from math import ceil

def vypocti_cenu_zpravy(text_zpravy):
    delka_zpravy = len(text_zpravy)
    cena = 3
    jedna_zprava = 180
    if delka_zpravy <= jedna_zprava:
        cena_zpravy = cena
    elif delka_zpravy > jedna_zprava:
        pocet_zprav = delka_zpravy / jedna_zprava
        cena_zpravy = math.ceil(pocet_zprav) * cena
    return cena_zpravy

zadany_text_zpravy = input("Vypište prosím text zprávy: ")
# kolik bude zpráva stát

konecna_cena = vypocti_cenu_zpravy(zadany_text_zpravy)

print(konecna_cena)
