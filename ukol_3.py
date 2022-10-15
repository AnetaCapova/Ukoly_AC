from doctest import FAIL_FAST
from math import ceil


cislo = input("Zadejte prosím telefonní číslo bez mezer(!): ")
# zjistit správný formát
pocet_cisel = len(cislo)

def spravny_format(pocet_cisel):
    if pocet_cisel == 9 or 13:
        return True
    else:
        return False

text_zpravy = input("Vypište prosím text zprávy: ")
# kolik bude zpráva stát


def cena_zpravy():
    delka_zpravy = len(text_zpravy)
    cena = 3
    jedna_zprava = 180
    # mena = "kč"
    if delka_zpravy <= jedna_zprava:
        cena_zpravy = cena
    elif delka_zpravy > jedna_zprava:
        import math
        skutecna_delka = delka_zpravy / jedna_zprava
        cena_zpravy = math.ceil(skutecna_delka) * cena

# print(spravny_format())
# print(cena_zpravy())
print(cena_zpravy)