import random

# Define um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

# Solicita ao usuário para adivinhar
adivinhacao = int(input("Adivinhe um número entre 1 e 10: "))

# Executa o loop enquanto o usuário não adivinhar o número
while adivinhacao != numero_secreto:
    adivinhacao = int(input("Errado! Tente novamente: "))

# Quando o usuário acerta, exibe uma mensagem de parabéns
print("Parabéns! Você acertou!")
