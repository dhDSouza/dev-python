while True:
    # Solicita um número do usuário
    numero = int(input("Digite um número para ver sua tabuada (ou 0 para sair): "))

    # Se o usuário digitar 0, encerra o loop
    if numero == 0:
        break

    # Calcula e exibe a tabuada do número
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print()  # Linha em branco para separar as tabuadas
