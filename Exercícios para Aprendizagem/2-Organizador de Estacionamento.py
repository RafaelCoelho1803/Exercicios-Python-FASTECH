vagas = [False] * 5

def estacionar():
    for i in range(5):
        if not vagas[i]:
            vagas[i] = True
            print(f"O carro foi estacionado na vaga {i + 1}.")
            return
    print("O estacionamento está cheio.")

def liberar_vaga(vaga):
    if vagas[vaga - 1]:
        vagas[vaga - 1] = False
        print(f"A vaga {vaga} foi liberada.")
    else:
        print(f"A vaga {vaga} já está livre.")

def mostrar_vagas():
    for i, vaga in enumerate(vagas, start=1):
        status = "ocupada" if vaga else "livre"
        print(f"Vaga {i}: {status}")

# Loop principal
while True:
    print("\n1. Estacionar carro\n2. Liberar vaga\n3. Mostrar status das vagas\n4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        estacionar()
    elif opcao == "2":
        vaga = int(input("Informe o número da vaga (1-5): "))
        liberar_vaga(vaga)
    elif opcao == "3":
        mostrar_vagas()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
