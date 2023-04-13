NotaAlunos = [['Leticia', [5, 2, 5, 1]], ['Isabela', [10, 7, 6, 8]], ['Natalia', [4, 4, 2, 10]], ['Maykon', [8, 8, 9, 10]], ['Lorena', [2, 4, 5, 10]], ['Larissa', [5, 1, 9, 7]], ['Julia', [5, 4, 7, 9]], ['Raquel', [4, 9, 6, 10]], ['Ariel', [4, 8, 8, 6]], ['Endryll', [1, 3, 10, 5]]]
contador_alunos = 0

for aluno in NotaAlunos:
    notas = aluno[1]
    media = sum(notas) / len(notas)
    if media >= 7.00:
        contador_alunos += 1
        print(f"A média do/a {aluno[0]} é {media:.2f}")

print(f"Quantidades de médias positivas: {contador_alunos}")