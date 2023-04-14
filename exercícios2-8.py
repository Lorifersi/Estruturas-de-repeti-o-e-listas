algarismos = [1, 2, 3, 4, 5]
soma = 0
i = 0

while i < len(algarismos):
    soma += algarismos[i]
    i += 1

media = soma / len(algarismos)
print(media)