while True:
    nome = input("Nome do aluno: ")
    n1 = input("Nota 1: ")
    n2 = input("Nota 2: ")
    n3 = input("Nota 3: ")

    with open("notas.txt", "a") as notas:
        notas.write("{}\n".format(nome))
        notas.write("{}\n".format(n1))
        notas.write("{}\n".format(n2))
        notas.write("{}\n".format(n3))

    continuar = input("Deseja adicionar outro aluno? (s/n): ").lower()
    if continuar != 's':
        break
