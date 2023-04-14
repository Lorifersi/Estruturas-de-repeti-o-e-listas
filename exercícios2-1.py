while True:
    Nota = float(input("Nota de 0 a 10:"))
    if Nota >=0 and Nota <=10:
        print ("Nota válida:", Nota)
    else:
        print("Inválido")
        break