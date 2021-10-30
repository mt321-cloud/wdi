l1 = input("Wprowadzona przez Ciebie liczba 1 to ")
l2 = input("Wprowadzona przez Ciebie liczba 2 to ")
l1 = int(l1)
l2 = int(l2)

if abs(l1-l2) > 20:
    avg = (l1+l2)/2
    print("srednia:", avg)
    i = 1
    while i <= 3:
        print(int(avg-i))
        print(int(avg+i))
        i += 1

else:
    for x in range(l1, l2+1):
        print(x)
