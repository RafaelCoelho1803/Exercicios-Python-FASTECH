assentos = [[False] * 50 for _ in range(20)]

def ocupar_assento(fileira, cadeira):
    if assentos[fileira - 1][cadeira - 1]:
        print(f"O assento {cadeira} da fileira {fileira} já está ocupado.")
    else:
        assentos[fileira - 1][cadeira - 1] = True
        print(f"Assento {cadeira} da fileira {fileira} foi ocupado.")

def liberar_assento(fileira, cadeira):
    if assentos[fileira - 1][cadeira - 1]:
        assentos[fileira - 1][cadeira - 1] = False
        print(f"Assento {cadeira} da fileira {fileira} foi liberado.")
    else:
        print(f"O assento {cadeira} da fileira {fileira} já está livre.")

def mostrar_proxima_fileira():
    for i, fileira in enumerate(assentos, start=1):
        if False in fileira:
            print(f"Fileira {i} é a próxima com assentos disponíveis.")
            return
    print("Todas as fileiras estão ocupadas.")


while True:
    print("\n1. Ocupar assento\n2. Liberar assento\n3. Próxima fileira disponível\n4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        fileira = int(input("Informe a fileira (1-20): "))
        cadeira = int(input("Informe a cadeira (1-50): "))
        ocupar_assento(fileira, cadeira)
    elif opcao == "2":
        fileira = int(input("Informe a fileira (1-20): "))
        cadeira = int(input("Informe a cadeira (1-50): "))
        liberar_assento(fileira, cadeira)
    elif opcao == "3":
        mostrar_proxima_fileira()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
