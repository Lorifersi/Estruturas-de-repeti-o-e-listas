numeros = [8, 5, 1, 9, 4]

soma = sum(numeros)

multiplicacao = 1
for num in numeros:
    multiplicacao *= num

print("Números", numeros)
print("Soma: ", soma)
print("Multiplicação: ", multiplicacao)