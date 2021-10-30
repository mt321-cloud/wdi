l = input("Wprowadzona przez Ciebie liczba to ")
l = int(l)

ile_gw = 3
ile_sp = l-2

print(' '*(l-1)+'X')

for x in range(l-1):
    print(' '*ile_sp+'*'*ile_gw)
    ile_gw += 2
    ile_sp -= 1
print(' '*(l-1)+"U")
