def znajdz_skladniki(tab, sumy):
    n = znajdz_max(tab)
    if n == 1:
        return
    i = 1
    tab.remove(n)
    while i < n//2+1:
        j = i
        while j < n//2+1:
            lista = [j, n-j]
            lista.extend(tab)
            lista_kopia = lista.copy()
            lista_kopia = sortuj(lista_kopia)
            j += i
            if lista_kopia not in sumy:
                sumy.append(lista_kopia)
            # print(lista)
            znajdz_skladniki(lista, sumy)
        i += 1
    return sumy


def znajdz_max(lista):
    _max = lista[0]
    for x in lista:
        if x > _max:
            _max = x
    return _max


def sortuj(a):
    for x in range(len(a)-1):
        for b in range(len(a)-1):
            if a[b] > a[b+1]:
                a[b], a[b+1] = a[b+1], a[b]
    return a


n = 14
s = []
print(znajdz_skladniki([n], s))
