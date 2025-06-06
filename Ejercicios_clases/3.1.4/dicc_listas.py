class Limite(Exception):
    pass
class Vacio(Exception):
    pass
class Corto(Exception):
    pass

datos = {
    "estudiantes" : [],
    "carreras" : ["Analista", "Informatica", "Conectividad y redes"]
}
id = 0

while True:
    try:
        print("---Gestion de estudiantes---")
        print("(1). Ingresar estudiante")
        print("(2). Mostrar estudiantes")
        print("(3). Eliminar estudiante")
        print("(4). Actualizar estudiante")
        print("(5). Salir")
        opc = int(input("Ingrese opción: "))
    except ValueError:
        print("Ingrese una opción válida")
        continue

    if opc == 1:
        try:
            while True:
                for i in datos["carreras"]:
                    print(i)
                carrera = input("Ingrese carrera: ").capitalize()
                if carrera not in datos["carreras"]:
                    print("Ingrese una carrera válida")
                    continue
                else:
                    break

            estudiante = {
                "id" : id + 1,
                "nombre" : input("Nombre estudiante: "),
                "apellido" : input("Apellido estudiante: "),
                "edad" : int(input("Edad estudiante: ")),
                "carrera": carrera
            }

            if estudiante["edad"] < 17 or estudiante["edad"] > 100:
                raise Limite
            elif len(estudiante["nombre"]) < 3 or len(estudiante["apellido"]) < 3:
                raise Corto
            id += 1

            datos["estudiantes"].append(estudiante)
        except Corto:
            print("El nombre o apellido ingresado es muy corto")
            continue
        except Limite:
            print("La edad debe ser un número positivo entre 17 y 100")
            continue
        except ValueError:
            print("Un dato no fue correctamente ingresado")
            continue
        datos["estudiantes"]
    elif opc == 2:
        try:
            if len(datos["estudiantes"]) == 0:
                raise Vacio
            
            lista = datos["estudiantes"]
            for dic_estudiantes in lista:
                    print(f"ID: {dic_estudiantes["id"]}\nNOMBRE: {dic_estudiantes["nombre"]}\nAPELLIDO: {dic_estudiantes["apellido"]}\nEDAD: {dic_estudiantes["edad"]}\nCARRERA: {dic_estudiantes["carrera"]}")
        except Vacio:
            print("Ingrese un estudiante primero")
            continue
    elif opc == 3:
        try:
            if len(datos["estudiantes"]) == 0:
                raise Vacio
            esta = False
            eliminar = int(input("Ingrese ID a eliminar: "))
            for i in datos["estudiantes"]:
                if i["id"] == eliminar:
                    esta = True
                    datos["estudiantes"].remove(i)
                    print("Alumno eliminado correctamente")
            if esta == False:
                print("El ID del alumno no fue encontrado")
        except ValueError:
            print("Ingrese un número entero mayor a 0")
            continue
        except Vacio:
            print("Debe ingresar un alumno primero")
            continue
    elif opc == 4:
        try:
            if len(datos["estudiantes"]) == 0:
                raise Vacio
            esta = False
            actualizar = int(input("Ingrese ID a actualizar: "))
            for i in datos["estudiantes"]:
                if i["id"] == actualizar:
                    alum_encontrado = i
                    updt = {}
                    esta = True
                    while True:
                        for i in datos["carreras"]:
                            print(i)
                        carrera = input("Ingrese carrera: ").capitalize()
                        if carrera not in datos["carreras"]:
                            print("Ingrese una carrera válida")
                            continue
                        else:
                            break
                    nombre = input("Nombre: ")
                    apellido = input("Apeliido: ")
                    edad = int(input("Edad: "))
                    if estudiante["edad"] < 17 or estudiante["edad"] > 100:
                        raise Limite
                    elif len(estudiante["nombre"]) < 3 or len(estudiante["apellido"]) < 3:
                        raise Corto
                    
                    updt["nombre"] = nombre
                    updt["apellido"] = apellido
                    updt["edad"] = edad
                    updt["carrera"] = carrera

                    alum_encontrado.update(updt)
                    print("Alumno actualizado correctamente")
            if esta == False:
                print("El ID del alumno no fue encontrado")
        except ValueError:
            print("Ingrese un número entero mayor a 0")
            continue
        except Vacio:
            print("Debe ingresar un alumno primero")
            continue
        except Corto:
            print("El nombre o apellido ingresado es muy corto")
            continue
        except Limite:
            print("La edad debe ser un número positivo entre 17 y 100")
            continue
    elif opc == 5:
        print("Saliendo...")
        break
    else:
        print("Ingrese una opción válida")
        continue
