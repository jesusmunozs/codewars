def elem_comunes(lista1, lista2):
    comunes = []
    for i in lista1:
        if i in lista2:
            comunes.append(i)
    return comunes

print(elem_comunes([1, 3, 6, 7],[2, 3, 7]))