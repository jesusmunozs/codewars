"""
Mueve la primera letra de cada palabra al final de esta y
agrega un 'ay' despues de esta.
"""
#Primera solucion
#Es ineficiente, poco escalable y tiene errores en casos especiales
def first_to_last(word:str):
    first = True
    letter = ""
    result = ""
    for i in word:
        if first:
            letter = i
            first = False
            continue
            
        if i == " ":
            result += letter + "ay" + " "
            first = True
        elif i == word[-1]:
            result += i
            result += letter + "ay"
        else:
            result += i
    
    return result

print(first_to_last("Fuel Dust!"))

#Segunda solucion (Más eficiente) sigue dando problemas
def first_to_last(word: str):
    words = word.split()  # 1. Divide el string en palabras
    processed = [w[1:] + w[0] + 'ay' for w in words if w]  # 2. Procesa cada palabra
    return ' '.join(processed)  # 3. Une las palabras procesadas