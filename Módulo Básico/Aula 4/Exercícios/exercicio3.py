# Pedindo ao usuário para digitar um número inteiro positivo.
numero = int(input("Digite um número inteiro positivo: "))

# Inicializando a variável soma, que vai guardar o somatório dos números.
soma = 0

# Usando um laço for para somar todos os números de 1 até o número fornecido.
for i in range(1, numero + 1):
    soma += i  # Adicionando o valor de 'i' à variável 'soma' em cada iteração.

# Exibindo o resultado do somatório.
print(f"A soma de todos os números de 1 até {numero} é: {soma}")
