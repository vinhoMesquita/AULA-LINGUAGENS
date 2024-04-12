# Este código tenta implementar um jogo simples de adivinhação de números.
# O programa deve escolher um número aleatório entre 1 e 10 e permitir que o usuário tente adivinhar o número.
# No entanto, o código está incompleto e contém erros.
# Complete e corrija o código para que o jogo funcione corretamente.
# O usuário tem três tentativas para adivinhar o número. Após cada tentativa, o programa deve informar
# se o palpite é muito alto, muito baixo ou correto.

import random

numero_secreto = random.randint(1, 10)
tentativas = 3

while tentativas > 0:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    if palpite == numero_secreto:
        print("Parabéns! Você acertou.")
        break
    elif palpite != numero_secreto:
        print("Prabéns! Você falhou miseravelmente, tente novamente")   
        if palpite > numero_secreto:
            print("Um pouco mais abaixo") 
        else:
            print("Um pouco mais em cima")
    tentativas -= 1

print("Fim do jogo, o número era: ", numero_secreto)