#receba 10 notas do usuário e guarde em uma lista e tire a média dessas notas
#no final o programa deve imprimir se o aluno foi aprovado ou não, média 7

'''
notas = []
soma = 0

for i in range(10):
   notas.append(float(input(f"Digite a {i+1}° nota: ")))
   #soma = soma + notas[i]
  
soma = sum(notas) 
print(soma)
qtd = len(notas)

media = soma / qtd

if media < 7:
    print(f"Rprovado! a media é: {media:.2f}")
else:
    print(f"Aprovado! media é: {media:.2f}")
'''

notas = []
soma = 0

i=1

nota = float(input(f"Digite a {i}° nota: "))

while nota != -1:
    notas.append(nota)
    nota = (float(input(f"Digite a {i}° nota: ")))
    i+=1
    
    
   
    
soma = sum(notas) 
print(soma)
qtd = len(notas)

media = soma / qtd

if media < 7:
    print(f"Rprovado! a media é: {media:.2f}")
else:
    print(f"Aprovado! media é: {media:.2f}")