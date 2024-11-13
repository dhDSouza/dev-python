# Pedindo para o usuário digitar um número e armazenando esse valor na variável 'numero'.

numero = float(input("Digite um número: "))

# Verificando se o número é negativo, positivo ou zero:
# - Se o número for menor que zero, é negativo.
# - Se o número for maior que zero, é positivo.
# - Se o número for igual a zero, é neutro.

if numero < 0:
    print("O número é negativo.")
elif numero > 0:
    print("O número é positivo.")
else:
    print("O número é zero.")
