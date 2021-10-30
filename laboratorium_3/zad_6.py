l1 = input("Wprowadzona przez Ciebie liczba 1 to ")
l2 = input("Wprowadzona przez Ciebie liczba 2 to ")
l1 = int(l1)
l2 = int(l2)

"""
sprawdzenie czy liczby sa mniejsze od zera
jesli tak, zakonczenie programu
"""

if l1 < 0 and l2 < 0:
    print("liczby mniejsze od zera. koniec programu")
else:
    if l1 < 0:
        l1 = abs(l1)
    elif l2 < 0:
        l2 = abs(l2)
    # obliczenie i przypisanie do zmiennych

    s = l1+l2
    r = l1-l2
    ic = l1*l2
    ir = l1/l2
    k1 = pow(l1, 2)
    k2 = pow(l2, 2)
    p1 = pow(l1, 1/2)
    p2 = pow(l2, 1/2)

    # wypisanie wynikow

    print("suma:", s)
    print("roznica:", r)
    print("iloczyn:", ic)
    if ic == 10:
        print("Yay!")
    print("iloraz:", ir)
    print("kwadrat liczby 1:", k1)
    print("kwadrat liczby 2:", k2)
    print("pierwiastek liczby 1:", p1)
    print("pierwiastek liczby 2:", p2)
