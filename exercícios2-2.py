while True:
    NomeDeUsuario = input("Nome de usuário: ")
    Senha = input("Senha: ")
    
    if NomeDeUsuario == Senha:
        print("'Senha' não pode ser igual ao nome de usuário.")
    else:
        print("Aceitos")
        break