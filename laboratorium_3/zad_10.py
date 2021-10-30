import random
czy_nowe = "T"
while czy_nowe == "T":
    print("Podaj liczby po kolei a następnie wprowadz znak operacji")
    wynik = ""
    w = input()
    tab = []
    while w.isnumeric():
        tab.append(int(w))
        w = input()
    if w == '+':
        wynik = sum(tab)
    elif w == '-':
        wynik = tab[0]
        for x in tab[1:]:
            wynik -= x
    elif w == '*':
        wynik = tab[0]
        for x in tab[1:]:
            wynik *= x
    elif w == '/':
        wynik = tab[0]
        for x in tab[1:]:
            wynik /= x
    elif w == '**':
        wynik = tab[0]
        for x in tab[1:]:
            wynik **= x
    elif w == '^':
        wynik = tab[0]
        for x in tab[1:]:
            wynik **= 1/x
    elif w == 'x':
        if len(tab) != 2:
            print("Musisz podac dwie liczby")
        else:
            wynik = random.randrange(tab[0], tab[1])
    else:
        print("Brak takiej operacji. Sprobuj ponownie")
    print("Twoje liczby:", tab)
    print(wynik)

    czy_nowe = input("Czy chcesz wprowadzić nowe dane?(T/N)")
    while czy_nowe != "T" and czy_nowe != "N":
        czy_nowe = input("Czy chcesz wprowadzić nowe dane?(T/N)")
