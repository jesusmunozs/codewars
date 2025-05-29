def es_anagrama(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    if len(palabra1) != len(palabra2):
        return False
    elif palabra1 == palabra2:
        return False
    
    return sorted(palabra1) == sorted(palabra2)

print(es_anagrama("listen", "silent"))
print(es_anagrama("hello", "world"))
print(es_anagrama("Race", "Care"))
print(es_anagrama("anagram", "nagaram"))
print(es_anagrama("listen", "listen"))