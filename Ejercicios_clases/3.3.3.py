def validar_lista_numeros():
    while True:
        try:
            entrada = input("Ingrese numeros enteros separados por un espacio: ")
            lista = entrada.split()
            lista_enteros = [int(i) for i in lista]
            break
        except:
            print("Ingrese números enteros separados por un espacio...")
    return lista_enteros
lista_enteros = validar_lista_numeros()

pares = [i for i in lista_enteros if i%2 == 0]
impares = [i for i in lista_enteros if i%2 != 0]

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")




