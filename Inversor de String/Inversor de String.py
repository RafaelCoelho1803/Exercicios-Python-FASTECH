def inverte_string(string):
    string_invertida = ""


    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]

    return string_invertida


texto = input("Digite uma string para inverter: ")
texto_invertido = inverte_string(texto)
print("String invertida:", texto_invertido)
