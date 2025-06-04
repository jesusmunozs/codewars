#Ejercicio 1
class Limite(Exception):
    pass

class Vacio(Exception):
    pass

lista_notas = []

while True:
    print("---Bienvenido al sistema de notas")
    print("(1). Agregar nota")
    print("(2). Mostrar notas")
    print("(3). Mostrar cantidad de notas")
    print("(4). Obtener promedio")
    print("(5). Salir")
    try:
        opc = int(input("Ingrese opción: "))
    except:
        print("Ingrese 1, 2, 3 o 4")
        continue

    if opc == 1:
        try:
            nota = float(input("Ingrese nota: "))
            if nota < 1 or nota > 7:
                raise Limite
            
            lista_notas.append(nota)
        except Limite:
            print("Ingrese notas entre 1 y 7")
            continue
        except ValueError:
            print("Ingrese solo valores númericos")
            continue
    elif opc ==2:
        try:
            if len(lista_notas) == 0:
                raise Vacio
        except Vacio:
            print("Ingrese una nota primero")
            continue

        print(f"Las notas ingresadas son: {lista_notas}")
    elif opc == 3:
        try:
            if lista_notas == []:
                raise Vacio
        except Vacio:
            print("Ingrese una nota primero")  
            continue      
        print(f"La cantidad de notas ingresadas es: {len(lista_notas)}")
    elif opc == 4:
        try:
            if lista_notas == []:
                raise Vacio
        except Vacio:  
            print("Ingrese una nota primero") 
            continue

        print(f"El promedio de notas es: {sum(lista_notas) / len(lista_notas)}")
    elif opc == 5:
        print("Gracias por usar nuestro sistema...")
        break       
    else:
        print("Ingrese 1, 2, 3 o 4")
        