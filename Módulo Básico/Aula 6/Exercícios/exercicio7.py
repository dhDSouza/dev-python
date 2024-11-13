import random

# Inicializa a pontuação do usuário
pontuacao = 0

# Executa o loop até que o usuário escolha parar ou a pontuação seja -1
while pontuacao > -1:
    
    # Sorteia um número aleatório entre 1 e 100
    numero_sorteado = random.randint(1, 100)

    # Pergunta ao usuário se ele quer continuar ou parar
    decisao = input("Digite 'parar' para encerrar ou qualquer tecla para continuar: ")

    # Verifica se o usuário escolheu parar
    if decisao.lower() == "parar":
        print(f"Você desistiu do jogo com uma pontuação final de {pontuacao}.")
        break

    # Verifica se o número sorteado é par ou ímpar
    if numero_sorteado % 2 == 0:
        # Número par: o usuário ganha um ponto
        pontuacao += 1
        print(f"Parabéns! Você ganhou 1 ponto.\nO número sorteado foi {numero_sorteado}.\nPontuação atual: {pontuacao}.")
    else:
        # Número ímpar: o usuário perde um ponto
        pontuacao -= 1
        print(f"Que pena! Você perdeu 1 ponto.\nO número sorteado foi {numero_sorteado}.\nPontuação atual: {pontuacao}.")

    # Se a pontuação do usuário chegar a -1, o jogo acaba automaticamente
    if pontuacao == -1:
        print("Sua pontuação chegou a -1. O jogo acabou!")
