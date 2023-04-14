numeros = [1, 2, 3, 4, 5]
indice = 0
maior= numeros[indice]

while indice < len(numeros):
    if numeros[indice] > maior:
        maior = numeros[indice]
    indice += 1

print(maior)
