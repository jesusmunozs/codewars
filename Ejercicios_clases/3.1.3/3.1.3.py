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

# Ejercicio 2
lista_super = {
    "Producto" : [],
    "Valor" : []
}
while True:
    try:
        print("----Bienvenido al super----")
        print("(1). Agregar producto")
        print("(2). Detalle boleta")
        print("(3). Salir")
        opc = int(input("Ingrese opción: "))
    except ValueError:
        print("Ingrese 1, 2 o 3")
        continue

    if opc == 1:
        try:
            producto = input("Ingrese producto: ")
            precio = int(input("Ingrese el precio del producto: "))

            if precio < 1:
                raise Limite
            
            lista_super["Producto"].append(producto)
            lista_super["Valor"].append(precio)
        except Limite:
            print("El valor del producto debe ser mayor a 0")
            continue
        except ValueError:
            print("Ingrese un número")
            continue
        except:
            print("A ocurrido un error")
            continue
    elif opc == 2:
        try:
            if not lista_super["Producto"]:
                raise Vacio
            
            print("-----Detalle Boleta-----")
            for i in range(len(lista_super["Producto"])):
                elemento = lista_super["Producto"][i]
                valor = lista_super["Valor"][i]
                print(f"{elemento}:    ${valor}")
            print(f"El valor total es: {sum(lista_super['Valor'])}")
        except Vacio:
            print("Debe agregar algún producto...")
            continue
    elif opc == 3:
        print("Muchas gracias por su compra!")
    else:
        print("Ingrese 1, 2, o 3")
