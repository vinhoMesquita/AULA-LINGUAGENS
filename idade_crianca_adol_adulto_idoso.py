#receber idade, verificar se é criança(0~12), adolescente(13~18), adulto(18~60) ou idoso(>60)

print("Digite alguma idade: ")
idade = int(input())

if idade > 0 and idade <=12:
    print("Idade de criança")    
elif idade > 60:
    print("Idade de idoso")
elif idade >= 13 and idade <=18:  
    print("Idade de adulto")
else:   
    print("Idade de adulto")