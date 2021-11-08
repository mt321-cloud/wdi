# Zadanie 10. Napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb.

def nwd(a, b):

    if b == 0:
        return a
    else:
        r = a % b
        return nwd(b, r)


x = int(input("Wprowadz pierwsza liczbe:"))
y = int(input("Wprowadz druga liczbe:"))
z = int(input("Wprowadz trzecia liczbe:"))

wynik = nwd(nwd(x, y), z)
print("NWD zadanych liczb to", wynik)
