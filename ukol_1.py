baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

kod_baliku = input("Zadejte prosím kód balíku: ")

if kod_baliku in baliky.values == True:
    print("Balík byl předán kurýrovi")
else:
    print("Balík zatím nebyl předán kurýrovi")