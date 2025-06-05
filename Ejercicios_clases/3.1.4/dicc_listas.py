
datos = {
    "Estudiantes" : [
        {
            "id" : None,
            "Nombre" : None,
            "Apellido" : None,
            "Edad" : None,
            "Carrera" : None

        }
    ],
    "Carreras" : ["Analista", "Informatica", "Conectividad y redes"]
}
id = 0

while True:
    try:
        print("---Gestion de estudiantes---")
        print("(1). Ingresar estudiante")
        print("(2). Mostrar estudiantes")
        print("(3). Actualizar estudiante")
        print("(4). Eliminar estudiante")
        print("(5). Salir")
        opc = int(input("Ingrese opción: "))
    except ValueError:
        print("Ingrese una opción válida")
        continue

    if opc == 1:
        datos["Estudiantes"]{
            ""
        }
    elif opc == 2:
        pass
    elif opc == 3:
        pass
    elif opc == 4:
        pass
    elif opc == 5:
        print("Saliendo...")
        break
    else:
        print("Ingrese una opción válida")
        continue
