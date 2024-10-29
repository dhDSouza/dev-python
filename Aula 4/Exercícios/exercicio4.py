# Pedindo ao usuário para digitar um número inteiro.
numero = int(input("Digite um número para ver sua tabuada: "))

# Usando um laço for para gerar a tabuada de 1 a 10.
for i in range(1, 11):
    resultado = numero * i  # Calculando o resultado da multiplicação.
    print(f"{numero} x {i} = {resultado}")
