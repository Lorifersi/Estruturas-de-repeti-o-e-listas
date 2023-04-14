números = [1, 2, 3, 4, 5]
indice = 0
maior= números[indice]

while indice < len(números):
    if números[indice] > maior:
        maior = números[indice]
    indice += 1
    
print(maior)
