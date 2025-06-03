def permutations(s):

    if len(s) == 0:
        return [""]
    if len(s) == 1:
        return [s]

    todas_las_permutaciones = []

    for i, char in enumerate(s):

        restantes = s[:i] + s[i+1:]

        permutaciones_de_los_restantes = permutations(restantes)

        for perm_restante in permutaciones_de_los_restantes:
            todas_las_permutaciones.append(char + perm_restante)

    return todas_las_permutaciones
print(permutations("abc"))