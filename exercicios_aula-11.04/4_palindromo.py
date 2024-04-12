# O código abaixo é uma tentativa de criar um verificador de palíndromos.
# Palíndromos são palavras ou frases que são iguais quando lidas de trás para frente.
# No entanto, o código está incompleto e contém erros.
# Complete e corrija o código para que ele funcione corretamente.
# O usuário deve digitar uma palavra ou frase, e o programa deve imprimir se é um palíndromo ou não.
# Ignore espaços, pontuações e diferenças entre maiúsculas e minúsculas.





texto_entrada = str(input("Digite um texto: "))
texto_separado = texto_entrada.lower().split()
texto = "".join(texto_separado)

texto_invertido = texto[::-1]

if texto == texto_invertido:
    print(f"A palavra {texto} é um palíndromo")
else:
    print(f"A palavra {texto} não é um palíndromo")
    
    
