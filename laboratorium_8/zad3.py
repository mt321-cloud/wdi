# Zadanie 3.
# Proszę napisać program, który wypełnia N -elementową listę pseudolosowymi liczbami nieparzystymi z zakresu [ 1 , 99 ] a następnie wyznacza i wypisuje różnicę pomiędzy długością najdłuższego znajdującego się w niej ciągu arytmetycznego o dodatniej różnicy, a długością najdłuższego ciągu arytmetycznego o ujemnej różnicy, przy założeniu, że kolejnymi wyrazami ciągu są elementy listy o kolejnych indeksach. Należy także przygotować własne przypadki testowe.

import random
# utworzenie i wpisanie do listy losowych liczb z zakresu od 1 do 99


def wypelnij_losowo():
    n = input("Podaj rozmiar listy:")
    l = []
    for x in range(int(n)):
        liczba = random.randrange(1, 99)
        while liczba % 2 == 0:
            liczba = random.randrange(1, 99)
        l.append(liczba)
    return l


# lista = [3, 5, 7, 9, 243234, 435354534, 234324324, 20, 19, 18, 17, 16, 15, 14]
#lista = [2, 4, 6, 55433544, 10, 15, 20, 25, 21, 17, 3453553435]
lista = wypelnij_losowo()
print(lista)

dl_ciagu = 2
max_dl_ciagu_rosn = 2
max_dl_ciagu_mal = 2

r1 = lista[1]-lista[0]
i = 1
while i < len(lista)-1:
    r2 = lista[i+1]-lista[i]
    if r1 == r2:
        dl_ciagu += 1
    else:
        dl_ciagu = 2
    r1 = r2
    if r2 > 0 and dl_ciagu > max_dl_ciagu_rosn:
        max_dl_ciagu_rosn = dl_ciagu
    elif r2 < 0 and dl_ciagu > max_dl_ciagu_mal:
        max_dl_ciagu_mal = dl_ciagu
    i += 1

print("Dlugosc najdluzszego ciagu rosnacego:", max_dl_ciagu_rosn)
print("Dlugosc najdluzszego ciagu malejacego:", max_dl_ciagu_mal)
print("Roznica miedzy dlugosciami tych ciagow:",
      abs(max_dl_ciagu_rosn-max_dl_ciagu_mal))
