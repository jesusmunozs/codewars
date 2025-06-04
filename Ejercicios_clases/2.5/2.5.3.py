class OpcionIncorrecta(Exception):
    pass
class MontoInvalido(Exception):
    pass
class PagoInvalido(Exception):
    pass

CUPO = 500000

deuda = 100000
opc = 0

while opc != 3:
    print("-------MENU-------")
    print("1. Pagar tarjeta de credito")
    print("2. Realizar pago")
    print("3. Salir")

    try:
        opc = int(input("Ingrese opcion: "))

        if opc < 1 or opc > 3:
            raise OpcionIncorrecta
    except ValueError:
        print("Error, ingrese un valor válido 1, 2 o 3")
        continue
    except OpcionIncorrecta:
        print("La opción ingresada no es válida")
        continue

    try:
        if opc == 1:
            print("-------Sistema de pago-------")
            print(f"Cupo: {CUPO}")
            print(f"Deuda: {deuda}")

            monto_a_pagar = int(input("Ingrese monto a pagar: "))

            if monto_a_pagar < 0:
                raise MontoInvalido
            
            if monto_a_pagar > (CUPO - deuda):
                raise MontoInvalido
            
            deuda -= monto_a_pagar

            print(f"Su deuda actual es: {deuda}")
    except ValueError:
        print("Error, ingrese un valor válido")
        continue
    except MontoInvalido:
        print("El monto ingresado no es válido")
        continue
    
    try:
        if opc == 2:
            while True:
                print("-------Sistema de compra-------")
                print(f"Su cupo es de: {CUPO-deuda}")


                monto_a_comprar = int(input("Ingrese monto a comprar: "))

                if monto_a_comprar < 0:
                    raise PagoInvalido

                if monto_a_comprar > (CUPO - deuda):
                    raise PagoInvalido

                deuda += monto_a_comprar

                print(f"Su saldo actual es: {CUPO-deuda}")

                seguir = input("Desea seguir comprando? y/n\n")
                seguir.lower()

                if seguir == "n":
                    break
                elif seguir == "y":
                    continue
                else:
                    raise OpcionIncorrecta
    except ValueError:
        print("Error, ingrese un valor válido")
        continue
    except PagoInvalido:
        print("El monto ingresado no es válido")
        continue
    except OpcionIncorrecta:
        print("La opcion ingresada no es correcta")
    