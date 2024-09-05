total_atendimentos = 0
ruim = 0
bom = 0
otimo = 0


while True:
    print("\n1. Ruim\n2. Bom\n3. Ótimo\n4. Sair e mostrar resultados")
    opcao = input("Avalie o atendimento: ")

    if opcao == "1":
        ruim += 1
        total_atendimentos += 1
    elif opcao == "2":
        bom += 1
        total_atendimentos += 1
    elif opcao == "3":
        otimo += 1
        total_atendimentos += 1
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")


if total_atendimentos > 0:
    perc_ruim = (ruim / total_atendimentos) * 100
    perc_bom = (bom / total_atendimentos) * 100
    perc_otimo = (otimo / total_atendimentos) * 100


    print(f"\nTotal de atendimentos: {total_atendimentos}")
    print(f"Ruim: {ruim} ({perc_ruim:.2f}%)")
    print(f"Bom: {bom} ({perc_bom:.2f}%)")
    print(f"Ótimo: {otimo} ({perc_otimo:.2f}%)")
else:
    print("\nNenhum atendimento registrado.")
