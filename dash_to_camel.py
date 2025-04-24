"""
Crea un metodo/funcion que convierta '_'
o '-' en camel case 'camelCase', la primera
letra de la oracion debe quedar en su estado original
"""

def mayus_to_camel(word:str):
    result = ""
    dash = False
    for i in word:
        if i == "-" or i == "_":
            dash = True
            continue
        
        if dash:
            result += i.upper()
            dash = False
        else:
            result += i
    return result

print(mayus_to_camel("the-stealth-warrior"))
print(mayus_to_camel("The_Stealth_Warrior"))
print(mayus_to_camel("The_Stealth-Warrior"))

