palavra = ["o", "r", "g", "a", "n", "i", "z", "a", "d", "o"]
quantidadeconsoantes = 0

for Consoante in palavra:
    if Consoante not in "aeiou":
        quantidadeconsoantes = quantidadeconsoantes + 1
        print(Consoante)

print("Quantidade de consoantes:" + str(quantidadeconsoantes))
