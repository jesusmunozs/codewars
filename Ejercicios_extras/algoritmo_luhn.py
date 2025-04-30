def luhn_algoritm(n):
    text = str(n)
    card = text.replace(" ", "")
    list = [int(digito) for digito in card]
    
    for i in range(len(list)- 2, -1, -2):
        if list[i] * 2 >= 10:
            list[i] = sum(int(d) for d in str(list[i]*2))
        else:
            list[i] *= 2

    return sum(list) % 10 == 0

if luhn_algoritm("4242 4242 4242 4242"):
    print("La tarjeta es válida")
else:
    print("La tarjeta no es válida")