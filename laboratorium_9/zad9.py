# Zadanie 9.
# Proszę napisać program wczytujący tablicę dwuwymiarową o ustalonym wymiarze n × n wypełnioną liczbami naturalnymi. Dla danej tablicy należy napisać funkcję, która zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży element do sumy elementów wiersza w którym leży element jest największa. Wymiar tablicy powinien być definiowany przez użytkownika.

import random


def wypelnij_losowo():
    n = input("Podaj rozmiar listy:")
    l = []
    for i in range(int(n)):
        l.append([])
        for j in range(int(n)):
            liczba = random.randrange(1, 9)
            l[i].append(liczba)
    return l


lista = wypelnij_losowo()
for wiersz in lista:
    print(wiersz)


def najw_iloraz(tab):
    sumy_wierszy = []
    sumy_kolumn = []
    for i, wiersz in enumerate(tab):
        suma_w = 0
        suma_k = 0
        for j, liczba in enumerate(wiersz):
            suma_w += liczba
            suma_k += tab[j][i]
        sumy_wierszy.append(suma_w)
        sumy_kolumn.append(suma_k)
    print('sumy kolejnych wierszy:', sumy_wierszy)
    print('sumy kolejnych kolumn:', sumy_kolumn)

    min_w = sumy_wierszy[0]
    max_k = sumy_kolumn[0]
    for x in range(1, len(sumy_wierszy)):
        if sumy_wierszy[x] < min_w:
            min_w = sumy_wierszy[x]
        if sumy_kolumn[x] > max_k:
            max_k = sumy_kolumn[x]
    nr_w = sumy_wierszy.index(min_w)
    nr_kol = sumy_kolumn.index(max_k)
    return f'najwiekszy iloraz: {max_k/min_w}\nnr wiersza: {nr_w}\nnr kolumny: {nr_kol}'


print(najw_iloraz(lista))
