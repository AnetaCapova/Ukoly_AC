class Recept:
    def __init__(self, nazev, narocnost, url_adresa):
        self.nazev = nazev
        self.narocnost = narocnost
        self.url_adresa = url_adresa
        self.vyzkouseno = False
    def __str__(self):
        return f"Recept, který nese název: {self.nazev} je {self.narocnost} a naleznete ho na webových stránkách {self.url_adresa}, recept byl vyzkoušen: {self.vyzkouseno}."
    def zmen_narocnost(self, nova_hodnota):
        self.narocnost = nova_hodnota
    def zkusit(self):
        self.vyzkouseno = True

pho = Recept("Polévka Pho", "středně náročný", "http://www.acotedajis.cz/")
# print(pho)
tofu = Recept("Kari tofu", "lehký", "http://www.acotedanejis.cz/")
# print(tofu)
# print(str(pho))
pho.zkusit()
# pho.zmen_narocnost("velmi náročný")
tofu.zmen_narocnost("velmi náročný")
print(pho)
print(tofu)

class Kucharka:
    def __init__(self, nazev, autor):
        self.nazev = nazev
        self.autor = autor
        self.recepty = []
    def __str__(self):
        return f"Kuchařka se jmenuje {self.nazev}, napsal/a ji {self.autor} a obsahuje recepty, např. {self.recepty}."
    def pocet_receptu(self):
        pocet_receptu = len(self.recepty)
        print(f"V kucharce je {pocet_receptu} receptu")
    def pridej_recept(self, recept_novy):
        self.recepty.append(recept_novy)

kucharka = Kucharka("Veggie kuchařka", "Aneta Čápová")
kucharka.pocet_receptu()
kucharka.pridej_recept("pho")
kucharka.pocet_receptu()
print(kucharka)

