nome = input("Nome:")
while len(nome) <3:
    print ("mínimo 3 caracteries")
    nome = input("Nome:")

idade = input("Idade:")
while not idade.isnumeric() or int(idade) <0 or int(idade) >150:
    print ("Entre 0 e 150")
    idade = input("Idade:")
idade = int(idade)

salário = input("Sálario:")
while not salário.replace('.','', 1).isnumeric() or float(salário) <=0:
    print ("Maior que zero")
    salário = input("Salário:")
    idade = int(idade)

Sexo = ("Sexo(femino, masculino ou prefiro não dizer)")
while Sexo not in ['Feminino', 'Masculino', 'Prefiro não dizer']:
    print("Gênero inválido. Digite 'Feminino' para feminino, 'Masculino' para masculino ou 'Prefiro não dizer' para não indefinido.")
    genero = input("Digite seu gênero (F/M/I): ")

estadoCivil = input("Estado civil: Solteiro(a), Casado(a), Viúvo(a) ou Divorciado(a):")
while estadoCivil not in ['Solteiro', 'Solteira', 'Casado', 'Casada', 'Viúvo', 'Viúva', 'Divorciado', 'Divorciada']:
    print("Estado civil inválido. Digite 'Solteiro' para solteiro(a), 'Casado' para casado(a), 'Vivo' para viúvo(a) ou 'Divorciado' para divorciado(a).")
    estadoCivil = input("Digite seu estado civil (S/C/V/D): ")