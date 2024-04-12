# O código abaixo tem alguns problemas e está incompleto! 
# Altere o código abaixo para que ele atue como uma calculadora
# O usuário deve digitar um valor, um operador e outro valor
# seu programa deverá imprimir na tela o resultado da operação
# Faça com que o seu programa funcione até que o usuário digite -1

def soma(valor1, valor2):
    resultado = valor1 + valor2
    return resultado

def diferenca(valor1, valor2):
    resultado = valor1 - valor2
    return resultado

def multiplicacao(valor1, valor2):
    resultado = valor1 * valor2
    return resultado

def divisao(valor1, valor2):
    resultado = valor1 / valor2
    return resultado

valor1 = float(input("Num1"))
operador = str(input("op"))
valor2 = float(input("Num2"))

resultado = 0

while valor1 != -1 and valor2 != -1:
    
    if operador == '+':
        resultado = soma(valor1, valor2)
        print({f"{valor1} + {valor2} = {resultado}"})  
    elif operador == '-':
        resultado = diferenca(valor1, valor2)
        print({f"{valor1} - {valor2} = {resultado}"}) 
    elif operador == "*":
        resultado = multiplicacao(valor1, valor2)
        print({f"{valor1} * {valor2} = {resultado}"}) 
    elif operador == '/':
        resultado = divisao(valor1, valor2)
        print({f"{valor1} / {valor2} = {resultado}"}) 
    else:
        print("Operador inválido!")
        
    #print({f"{valor1} - {valor2} = {resultado}"})         
   
        
    valor1 = float(input("Num1"))
    operador = str(input("op"))
    valor2 = float(input("Num2"))
    
    
        
 
     







