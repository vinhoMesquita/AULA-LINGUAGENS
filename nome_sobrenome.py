#ler nome e sobrenome e mostrar na tela sobrenome e a primeira letra do nome
#e a ultima letra do nome

nome_user = input("Digite seu nome:")
sobrenome_user = input("Digite seu sobre-nome:")
tamanho = len(nome_user)

print(sobrenome_user,", ", nome_user[0], ", ", nome_user[tamanho-1], sep='')




