def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def verifica_pertencimento(numero):
    sequencia = fibonacci_sequence(numero)
    if numero in sequencia:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
print(verifica_pertencimento(numero))
