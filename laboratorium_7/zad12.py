# Zadanie 12.
# Wykorzystując listy proszę napisać program, który symuluje wykonywanie działań arytmetycznych w słupku. Program powinien pobierać od użytkownika liczby M i N oraz odpowiedni znak D (znak działania). Należy zaimplementować możliwość dodawania i odejmowania liczb mniejszych niż 10^10 i obsłużyć wyjątki, gdy użytkownik zażąda wykonania mnożenia lub dzielenia.
m = input("Podaj pierwsza liczbe:")
n = input("Podaj druga liczbe:")
d = input("Podaj znak dzialania:")

if int(m) >= 10**10 or int(n) >= 10**10:
    raise ValueError("Podano zbyt duza liczbe")

if d == '*' or d == '/':
    raise ValueError("Nieobslugiwana operacja arytmetyczna")

czy_wynik_ujemny = False

# sprawdzamy czy pierwsza liczba jest mniejsza od drugiej
if int(m) < int(n):
    m, n = n, m
    czy_wynik_ujemny = True

m_cyfry = [int(c) for c in m]
n_cyfry = [int(c) for c in n]

r = abs(len(m_cyfry)-len(n_cyfry))

# dopisanie zer z przodu krótszej liczby
if len(m_cyfry) > len(n_cyfry):
    for x in range(r):
        n_cyfry.insert(0, 0)
else:
    for x in range(r):
        m_cyfry.insert(0, 0)

# print(m_cyfry, n_cyfry)

wynik = ''

if d == '+':
    i = len(m_cyfry)-1
    czy_nadwyzka = False
    while i >= 0:
        suma = m_cyfry[i]+n_cyfry[i]
        if czy_nadwyzka:
            suma += 1
        if suma > 9:
            suma = suma-10
            czy_nadwyzka = True
        else:
            czy_nadwyzka = False
        wynik = str(suma)+wynik
        i -= 1
    if czy_nadwyzka:
        wynik = '1'+wynik

elif d == '-':
    i = len(m_cyfry)-1
    czy_pozyczka = False
    while i >= 0:
        roznica = m_cyfry[i]-n_cyfry[i]
        if czy_pozyczka:
            roznica -= 1
        if roznica < 0:
            roznica = roznica+10
            czy_pozyczka = True
        else:
            czy_pozyczka = False
        wynik = str(roznica)+wynik
        i -= 1
    if czy_wynik_ujemny:
        wynik = '-'+wynik

print('Wynik działania:', int(wynik))
