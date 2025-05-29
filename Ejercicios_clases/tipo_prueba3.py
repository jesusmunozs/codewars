class LargoIncorrecto(Exception):
    pass
class NombreCorto(Exception):
    pass

while True:
    cant_novatos = 0
    cant_elite = 0
    try:
        cant_supers = int(input("Ingrese cantidad de superhéroes: "))
        if cant_supers < 1:
            raise LargoIncorrecto
    except LargoIncorrecto:
        print("La cantidad debe ser mayor a 0")
        continue
    except:
        print("¡Error! Alguno de los valores no es fue ingresado correctamente")
        continue
    
    try:
        for i in range(cant_supers):
                    
            nombre = input(f"({i+1}). Ingrese el nombre del superhéroe: ")
            if len(nombre) < 5:
                raise NombreCorto
            
            experiencia = int(input(f"({i+1}). Ingrese los años de experiencia: "))
            if experiencia < 0:
                raise LargoIncorrecto
            
            if experiencia <= 60:
                cant_novatos += 1
            else:
                cant_elite += 1

        print(f"La cantidad de heroes novatos es {cant_novatos}")
        print(f"La cantidad de heroes élite es {cant_elite}")
        break
    
    except NombreCorto:
        print("El nombre debe tenr mas de 5 caracteres")
    except LargoIncorrecto:
        print("Los años de experiencia debe ser un valor positivo")
    except:
        print("¡Error! Alguno de los valores no es fue ingresado correctamente")