def zeros(n):
    fact = 1
    zeros = 0
    for i in range(1, n):
        fact *= i

    x = str(fact)
    for i in x:
        if i == "0":
            zeros += 1
    return zeros
print(zeros(6))