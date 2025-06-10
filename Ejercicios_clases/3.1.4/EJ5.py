class Limite(Exception):
    pass

productos = ["Tomate", "Leche", "Huevos", "Harina", "Levadura", "Manteqilla", "Queso", "Vienesas"]
precios = [500, 900, 2500, 1000, 500, 2300, 4000, 3000]
IVA = .19

cant = 0

while True:
    total = 0
    try:
        for i in range(len(productos)):
            print(productos[i])
            print(precios[i])
            cant = int(input("Ingrese cantidad: "))

            if cant < 0:
                raise Limite
            total += cant * precios[i]
    except Limite:
        print("La cantidad no puede ser negativa")
        continue
    except ValueError:
        print("Ingrese un tipo de dato válido")
        continue

    print("Detalle pago:")
    print(f"Total: {total}")
    print(f"IVA: {total * IVA}")
    print(f"Total a pagar: {total + total * IVA}")
    break