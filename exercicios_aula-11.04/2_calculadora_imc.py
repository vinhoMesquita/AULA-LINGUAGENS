# O código abaixo é uma tentativa de criar uma calculadora de Índice de Massa Corporal (IMC).
# No entanto, ele está incompleto e contém erros.
# Modifique o código para que ele solicite ao usuário seu peso em quilogramas e altura em metros.
# Seu programa deve calcular e imprimir o IMC do usuário seguindo a fórmula IMC = peso / (altura ** 2).
# Além disso, deve classificar o resultado em: Baixo peso, Peso normal, Sobrepeso ou Obesidade, 
# baseando-se nos valores de IMC.

peso = float(input("Digite seu peso em kg: (65.5)"))
altura = float(input("Digite sua altura em metros: (1.75)"))

# Cálculo do IMC precisa ser corrigido

imc = peso / (altura**2)

# Classificação do IMC (faltam informações)
if imc < 18.5:
    classificacao = "Baixo peso"
elif imc < 24.9:
    classificacao = "Peso normal"
elif imc < 29.9:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"Seu IMC é {imc:.2f} e sua classificação é: {classificacao}")
