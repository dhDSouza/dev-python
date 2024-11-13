import random

# Define um número aleatório entre 1 e 20
numero_secreto = random.randint(1, 20)

# Define o número máximo de tentativas
tentativas = 5

# Executa o loop enquanto o usuário tiver tentativas
while tentativas > 0:
    adivinhacao = int(input("Adivinhe um número entre 1 e 20: "))

    # Verifica se o usuário acertou
    if adivinhacao == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    else:
        tentativas -= 1  # Decrementa as tentativas
        print(f"Errado! Você tem {tentativas} tentativas restantes.")

# Se o usuário não acertar, exibe a mensagem de derrota
if tentativas == 0:
    print("Você perdeu!")
