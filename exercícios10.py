Vetor1 = []
Vetor2 = []
for i in range(10):
    num_1 = int(input(f"Digite o {i+1}º elemento do vetor 1:"))
    Vetor1.append(num_1)
    num_2 = int(input(f"Digite o {i+1}º elemento do vetor 2:"))
    Vetor2.append(num_2)

intercalado = []
for i in range(10):
    intercalado.append(Vetor1[i])
    intercalado.append(Vetor2[i])

print("Vetor 1:", Vetor1)
print("Vetor 2:", Vetor2)
print("Intercalada:", intercalado)
    