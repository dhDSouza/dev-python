# Solicita um número inicial para a contagem regressiva
numero = int(input("Digite um número para a contagem regressiva: "))

# Realiza a contagem regressiva até zero
while numero >= 0:
    print(numero)
    numero -= 1  # Decrementa o número a cada iteração

# Exibe a mensagem final após a contagem
print("Boom!")
