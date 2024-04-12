# Este código tenta contar o número de palavras em uma string fornecida pelo usuário.
# No entanto, está incompleto e contém erros.
# Complete e corrija o código para que ele funcione corretamente.
# O usuário deve digitar uma string, e seu programa deve imprimir o número de palavras nessa string.
# Considere uma palavra como qualquer sequência de caracteres delimitada por espaços.

texto = input("Digite um texto: ")


#Dividi uma string em substrings com base em um separador definido
texto_no_space = texto.split()

numero_de_palavras = len(texto_no_space)

# Seu código para contar as palavras vai aqui

print(f"O número de palavras é: {numero_de_palavras}")




'''
texto = "   Olá, mundo!   "



print(texto)
semL = texto.split()
print(semL)
texto_trimmed = texto.strip("!")
print(texto_trimmed)  # Output: "Olá, mundo!"
'''