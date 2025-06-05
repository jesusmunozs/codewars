import random as rm

class Limite(Exception):
    pass

cont = 0
gan = False
while cont != 3:
    numeros = []
    ganadores = []

    try:
        print("Ingrese sus 7 números de la suerte.")
        for i in range(7):
            num = int(input(f"({i+1}). Ingrese número: "))
            if num < 1 or num > 49:
                raise Limite
            else:
                numeros.append(num)
    except Limite:
        print("Debe ingresar números entre 1 y 49")
        continue
    except ValueError:
        print("Debe ingresar números enteros")
        continue

    print(f"Usted ingresó los siguientes números: {numeros}")

    for i in range(7):
        num = rm.randint(1, 49)
        ganadores.append(num)
    
    print(f"Los numeros sorteados en la ronda {cont + 1}")
    for i in range(7):
        print(ganadores[i])

    for i in numeros:
        if i in ganadores:
            gan = True
            break
    
    if gan:
        print("Tienes un número ganador!!!!!")
        break
    else:
        print("Lo siento, pero no has ganado en esta ronda")

    cont += 1