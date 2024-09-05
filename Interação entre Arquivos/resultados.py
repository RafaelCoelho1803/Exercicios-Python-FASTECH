
def imprimir_lista(arquivo):
    print("Lista dos alunos:")
    with open(arquivo, "r") as f:
        for linha in f:
            print(linha.strip())


print("Alunos Aprovados:")
imprimir_lista("aprovados.txt")


print("\nAlunos Reprovados:")
imprimir_lista("reprovados.txt")
