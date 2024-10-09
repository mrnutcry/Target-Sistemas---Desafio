def count_letter_a(string):
    count = string.lower().count('a')
    if count > 0:
        return f"A letra 'a' aparece {count} vezes na string."
    else:
        return "A letra 'a' não aparece na string."

input_string = input("Informe uma string: ")

resultado = count_letter_a(input_string)
print(resultado)
