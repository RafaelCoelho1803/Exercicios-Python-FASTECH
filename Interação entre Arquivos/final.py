
def calcular_media_exame(media_anterior, nota_exame):
    return (media_anterior + nota_exame) / 2


def verificar_status_exame(media_exame):
    if media_exame >= 5:
        return "Aprovado após exame"
    else:
        return "Reprovado após exame"


alunos_exame = []


with open("exames.txt", "r") as arquivo_exames:
    for linha in arquivo_exames:
        aluno = linha.strip()
        nota_exame = float(input(f"Informe a nota do exame para o aluno {aluno}: "))
        alunos_exame.append((aluno, nota_exame))


for aluno, nota_exame in alunos_exame:
    media_exame = nota_exame
    status = verificar_status_exame(media_exame)


    nome_arquivo = "aprovados.txt" if status == "Aprovado após exame" else "reprovados.txt"
    with open(nome_arquivo, "a") as arquivo_resultado:
        arquivo_resultado.write(f"{aluno}: {media_exame:.2f} - {status}\n")
