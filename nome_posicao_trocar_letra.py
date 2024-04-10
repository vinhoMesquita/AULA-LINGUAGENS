#FAÇA UM PROGRAMA E PYTHON QUE RECEBA O NOME DO USUARIO E A POSICAO EM QUE ELE DESEJA
#ADICIONAR UMA LETRA, SE A LETRA QUE ESTIVER NA POSICAO INDICADA FOR R,
#SUBSTITUIR POR S, SE FOR M SUBSTITUIR POR N
#SENAO FOR NENHUMA DESSAS, REMOVER A LETRA DO NOM E IMPRIMA NA TELA
#A PALAVRA REFORMULADA


nome = str(input("Digite seu nome: "))

i = int(input("Digite a posição que quer adicionar uma letra: "))


if nome[i] == "R" or nome[i] == "r":
   print(nome[:i]+"r"+nome[i+1:])
elif nome[i] == "m" or nome[i] == "M":
    print(nome[:i]+"n"+nome[i+1:])
else: 
   print(nome[:i]+"r"+nome[i+1:])
##


