class NoValido(Exception):
    pass

romper = False
opc = "s"
id = 0
alumnos = {}
while True:
    error = False
    try:
        alumnos[id + 1] = {
            "Nombre" : input("Ingrese nombre del alumno: "),
            "Direccion" : input("Ingrese direccion del alumno: "),
            "Telefono" : int(input("Ingrese telefono del alumno: "))
        }
    except ValueError:
        print("El número ingresado no es válido.")
        error = True
    except:
        print("Algo salio mal...")
        error = True
    id += 1

    if error:
        continue
    
    while True:
            opc = input("Desea agregar otro alumno (s/n): ")
            opc.lower()
            if opc == "s":
                break
            elif opc == "n":
                print("\n")
                for id, detalle in alumnos.items():
                    for sub_clave, sub_valor in detalle.items():
                        print(f"{sub_clave}: {sub_valor}")
                    print("\n")
                romper = True
                break
            else:
                print("Ingrese una opcion válida (s/n)")

    if romper:
        break



