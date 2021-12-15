import random
import os

if os.path.exists("wspolrzedne.txt"):
    os.remove("wspolrzedne.txt")

f = open("wspolrzedne.txt", 'a')


def create_3d(n):
    tab_3d = [[[random.randrange(1, 9) for h in range(n)]
               for j in range(n)]for i in range(n)]
    return tab_3d


def save_positions(tablica_wsp, nr_plaszczyzny):
    f.write('plaszczyzna '+str(nr_plaszczyzny)+':\n')
    f.writelines(tablica_wsp)


def arrange_3d(tab):
    for ind_p, plaszczyzna in enumerate(tab):
        liczby = []
        wsp = []
        print(f'płaszczyzna {ind_p}:')
        for ind_w, wiersz in enumerate(plaszczyzna):
            print(wiersz)
            for ind_k, liczba in enumerate(wiersz):
                liczby.append(liczba)
                wsp.append(str(liczba)+': ' +
                           '('+str(ind_w)+','+str(ind_k)+') -> ')
        print(f'liczby z plaszczyzny {ind_p}:', liczby)

        liczby_nier = liczby.copy()

        # sortowanie liczb rosnaco
        for a in range(len(liczby)-1):
            for b in range(len(liczby)-1):
                if liczby[b] > liczby[b+1]:
                    liczby[b], liczby[b+1] = liczby[b+1], liczby[b]
        print('w kolejnosci rosnacej:', liczby)

        # ustawienie liczb po spirali
        spirala = plaszczyzna.copy()
        x = 0
        y = 0
        i = 0
        rozm = len(tab)
        wciecie = 1
        while i < len(liczby)-1:
            # wypelnienie gornego wiersza
            while y < rozm-wciecie:
                spirala[x][y] = liczby[i]
                nr_wiersza = liczby_nier.index(liczby[i])
                wsp[nr_wiersza] += '('+str(x)+','+str(y)+')\n'
                liczby_nier[nr_wiersza] = 'x'
                i += 1
                y += 1
            # wypelnienie prawej kolumny
            while x < rozm-wciecie:
                spirala[x][y] = liczby[i]
                nr_wiersza = liczby_nier.index(liczby[i])
                wsp[nr_wiersza] += '('+str(x)+','+str(y)+')\n'
                liczby_nier[nr_wiersza] = 'x'
                i += 1
                x += 1
            # wypelnienie dolnego wiersza
            while y > wciecie-1:
                spirala[x][y] = liczby[i]
                nr_wiersza = liczby_nier.index(liczby[i])
                wsp[nr_wiersza] += '('+str(x)+','+str(y)+')\n'
                liczby_nier[nr_wiersza] = 'x'
                i += 1
                y -= 1
            # wypelnienie lewej kolumny
            while x > wciecie-1:
                spirala[x][y] = liczby[i]
                nr_wiersza = liczby_nier.index(liczby[i])
                wsp[nr_wiersza] += '('+str(x)+','+str(y)+')\n'
                liczby_nier[nr_wiersza] = 'x'
                i += 1
                x -= 1
            # zmniejszenie rozmiaru 'pierscienia'
            wciecie += 1
            # ustawienie wspolrzednych na pierwsze pole nowego 'pierscienia'
            x += 1
            y += 1
        # wypelnienie srodkowego pola
        if rozm % 2 != 0:
            spirala[x][y] = liczby[-1]
            nr_wiersza = liczby_nier.index(liczby[i])
            wsp[nr_wiersza] += '('+str(x)+','+str(y)+')\n'
            liczby_nier[nr_wiersza] = 'x'
        print(f'spirala {ind_p}:')
        for w in spirala:
            print(w)
        # print(wsp)
        save_positions(wsp, ind_p)


dism = input("Podaj rozmiar listy:")
lista = create_3d(int(dism))
print('tablica 3d:', lista)
arrange_3d(lista)
