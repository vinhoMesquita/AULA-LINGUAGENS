#exibir o nome todo em letras minúsculas e o sobrenome todo maiusculo

nome = str(input())
sobre_nome = str(input())
born = input()

name = nome.lower()
under_name = sobre_nome.upper()

print(f"{name +" "+ under_name} nasceu no ano de {born}")
