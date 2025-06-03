def sum_pares1(list):
    suma = [i for i in list if i%2 == 0]
    return sum(suma)
print(sum_pares1([1, 2, 3, 4]))

def sum_pares2(list):
    return sum([i for i in list if i%2 == 0])
print(sum_pares2([1, 2, 3, 4]))