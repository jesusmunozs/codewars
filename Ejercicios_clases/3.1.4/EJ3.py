import random as rm

arreglo = []
for i in range(50):
    num = rm.randint(1, 1000)
    arreglo.append(num)
print("Arreglo original")
print(arreglo)

n = len(arreglo)

flag = True
while True:
    cambios = 0
    for i in range(n-1):
        if arreglo[i] > arreglo[i+1]:
            arreglo[i], arreglo[i+1] = arreglo[i+1], arreglo[i]
            cambios += 1

    if cambios == 0:
        break
print(arreglo)

if n%2 == 0:
    mediana = ((arreglo[int(n/2)]) / 2) + ((arreglo[int(n/2+1)])/2)
else:
    mediana = arreglo[int(n/2)]
print(f"La mediana es: {mediana}")
