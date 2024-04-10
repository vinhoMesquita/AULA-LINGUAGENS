#receber idade, verificar se é criança(0~12), adolescente(13~18), adulto(18~60) ou idoso(>60)

print("Write an age: ")
idade = int(input())

if idade > 0 and idade <=12:
    print("Child")    
elif idade > 60:
    print("Elderly")
elif idade <19:  
    print("Teenager")
else:   
    print("Adult")