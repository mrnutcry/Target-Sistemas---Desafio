def fibonacci_sequence(n):
    sequence = [0, 1]
    while sequence[-1] < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def check_number_in_fibonacci(n):
    sequence = fibonacci_sequence(n)
    if n in sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))

resultado = check_number_in_fibonacci(numero)
print(resultado)
