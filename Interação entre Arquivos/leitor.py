nomes = []
notas = []

with open("notas.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    i = 0
    while i < len(linhas):
        nome = linhas[i].strip()
        nomes.append(nome)
        notas_aluno = [float(linha.strip()) for linha in linhas[i+1:i+4]]
        notas.append(notas_aluno)
        i += 4

print("Nomes dos alunos:", nomes)
print("Notas dos alunos:", notas)

# Função para calcular a média das notas de um aluno
def calcular_media(notas):
    return sum(notas) / len(notas)


def verificar_status(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Exame"
    else:
        return "Reprovado"


for nome, notas_aluno in zip(nomes, notas):
    media = calcular_media(notas_aluno)
    status = verificar_status(media)


    nome_arquivo = f"{status.lower()}s.txt"
    with open(nome_arquivo, "a") as arquivo_status:
        arquivo_status.write(f"{nome}: {media:.2f}\n")
