# Pedindo ao usuário para escolher uma operação (adição, subtração, multiplicação ou divisão).

operacao = input("Escolha a operação (+, -, *, /): ")

# Pedindo ao usuário para inserir dois números para a operação.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Verificando a operação escolhida e executando o cálculo adequado:
# - Se a operação for "+", realiza a adição.
# - Se a operação for "-", realiza a subtração.
# - Se a operação for "*", realiza a multiplicação.
# - Se a operação for "/", realiza a divisão (com verificação para evitar divisão por zero).

if operacao == "+":
    resultado = numero1 + numero2
    print(f"O resultado da adição é: {resultado}")
elif operacao == "-":
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == "*":
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida!")
else:
    print("Operação inválida!")
