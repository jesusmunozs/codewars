usuario1 = "1"
usuario2 = None
usuario3 = "hola"
contraseña1 = "2"
contraseña2 = None
contraseña3 = "hola"

while True:
    opc1 = 0
    token = False

    print("----MENU----")
    print("(1). Inicio sesión")
    print("(2). Registro usuario")
    print("(3). Salir")
    try:
        opc = int(input("Ingrese opcion: "))    
    except ValueError:
        print("El valor ingresado no es válido")
        continue
    except:
        print("¡Error! Algo fue ingresado erroneamente")
        continue

    if opc == 1:
        if any(v is not None for v in [usuario1, usuario2, usuario3]):
            usuario = input("Ingrese usuario: ")
            contraseña = input("Ingrese contraseña: ")

            if usuario == usuario1 and contraseña == contraseña1:
                token = True
            elif usuario == usuario2 and contraseña == contraseña2:
                token = True
            elif usuario == usuario3 and contraseña == contraseña3:
                token = True
            
            if token:
                print("----MENU----")
                print("(1). Realizar llamada")
                print("(2). Enviar correo electronico")
                print("(3). Cerrar sesión")
                try:
                    opc1 = int(input("Ingrese opcion: "))
                except ValueError:
                    print("El valor ingresado no es válido")
                    continue
                except:
                    print("¡Error! Algo fue ingresado erroneamente")
                    continue

                if opc1 == 1:
                    celular = input("Ingrese su celular: ")
                    
            else:
                print("El usuario o contraseña ingresado no es válido")
                continue

        else:
            print("Debe registrar un usuario antes...")
            continue
    elif opc == 2:
        pass
    elif opc == 3:
        print("Muchas gracias por utilizar nuestro software")
        break
    else:
        print("la opcion ingresada no es válida")
        continue