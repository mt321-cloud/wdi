import random


class InicjacjaGry:
    def __init__(self, s):
        n = input('Podaj liczbe skoczkow:')
        if int(n) >= 100:
            raise ValueError('Podano zbyt duza liczbe')
        self.dane = []
        for i in range(int(n)):
            wsp = (random.randrange(0, s-1),
                   random.randrange(0, s-1))
            self.dane.append(wsp)
        print('Wspolrzedne skoczkow:', self.dane)
        print('')


class Szachownica:
    def __init__(self, wspol, s):
        self.wsp = wspol
        plansza = []
        for w in range(s):
            plansza.append([])
            for k in range(s):
                if (w, k) in self.wsp:
                    plansza[w].append('X')
                else:
                    plansza[w].append('O')
        self.plansza = plansza

    def wypisz_szachownice(self):
        for wiersz in self.plansza:
            r = ''
            for pole in wiersz:
                r += pole+' '
            print(r)

    def znajdz_szach(self):
        szach = []
        for s1 in self.wsp:
            x1 = s1[0]
            y1 = s1[1]
            for s2 in self.wsp:
                x2 = s2[0]
                y2 = s2[1]
                if (x1+2 == x2 and y1-1 == y2) or (x1+2 == x2 and y1+1 == y2) or (x1+1 == x2 and y1+2 == y2) or (x1-1 == x2 and y1+2 == y2) or (x1-2 == x2 and y1+1 == y2) or (x1-2 == x2 and y1-1 == y2) or (x1-1 == x2 and y1-2 == y2) or (x1+1 == x2 and y1-2 == y2):
                    if (s2, s1) not in szach:
                        szach.append((s1, s2))
        return szach


rozmiar_szach = 10
dane = InicjacjaGry(rozmiar_szach).dane
# dane = [(2, 2), (4, 1), (6, 2), (4, 3), (8, 7)]
sz = Szachownica(dane, rozmiar_szach)
sz.wypisz_szachownice()

if sz.znajdz_szach():
    print('Szachuja sie:')
    for t in sz.znajdz_szach():
        print(f'{t[0]} i {t[1]}')
else:
    print('Zadne skoczki sie nie szachuja')
