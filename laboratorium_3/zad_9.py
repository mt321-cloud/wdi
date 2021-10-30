saldo = 0
pin = '0000'
podaj_typ = ""

while podaj_typ != "exit":
    print("\n")
    if podaj_typ:
        print("Co chcesz zrobić w kolejnym kroku?")
    print("Wybierz typ operacji")
    print("wplata - wp")
    print("wyplata - wyp")
    print("sprawdzenie salda - s")
    print("wyjscie - exit")

    podaj_typ = input("Podaj typ operacji:")
    if podaj_typ != 'exit':
        podaj_pin = input("Podaj PIN:")
        while podaj_pin != pin:
            podaj_pin = input("Bledny PIN.Sprobuj jeszcze raz:")
    if podaj_typ == 'wp':
        print("\n")
        kw_wp = input("Podaj kwote wplaty:")
        saldo += int(kw_wp)
    elif podaj_typ == 'wyp':
        print("\n")
        kw_wyp = input("Podaj kwote wyplaty:")
        while int(kw_wyp) > saldo:
            kw_wyp = input("Za duza kwota.Sprobuj jeszcze raz:")
        saldo -= int(kw_wyp)
    elif podaj_typ == 's':
        print("\n")
        print("Twoje saldo:", saldo)

print("Do widzenia")
