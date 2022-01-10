def znajdz_skladniki(tab):
    sumy = []
    n = znajdz_max(tab)
    if n == 1:
        return
    i = 1
    tab.remove(n)
    # print(l)
    while i < n:
        j = i
        while j < n:
            lista = [j, n-j]
            # print(i)
            lista.extend(tab)
            j += i
            if set(lista) not in sumy:
                sumy.append(set(lista))
                print(lista)
        i += 1
        return znajdz_skladniki(lista)


def znajdz_max(lista):
    _max = lista[0]
    for x in lista:
        if x > _max:
            _max = x
    return _max


n = 8
znajdz_skladniki([n])
