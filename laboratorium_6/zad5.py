# Zadanie 5.
# Proszę napisać program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy liczba naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.

def czy_palindrom(liczba):
    i = 0
    while i < len(liczba)/2:
        if liczba[i] != liczba[-i-1]:
            return False
        i += 1
    return True


while True:
    n = input('Podaj liczbe naturalna:')
    try:
        if int(n) >= 0:
            break
        else:
            raise
    except:
        print('Podana liczba nie jest liczba naturalna. Sproboj ponownie')


n_bin = bin(int(n))[2:]
print('W systemie dziesietnym:', n_bin)

if czy_palindrom(n):
    print('Podana liczba jest palindromem w systemie dziesietnym')
else:
    print('Podana liczba nie jest palindromem w systemie dziesietnym')

if czy_palindrom(n_bin):
    print('Podana liczba jest palindromem w systemie binarnym')
else:
    print('Podana liczba nie jest palindromem w systemie binarnym')
