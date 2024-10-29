# Matriz inicial de 2x2
matriz = [
    [1, 2],
    [3, 4]
]

# Solicita ao usuário um número para multiplicar cada elemento da matriz
numero = int(input("Digite um número: "))

# Dois loops aninhados para acessar cada elemento da matriz
for i in range(len(matriz)):            # Percorre cada linha da matriz
    for j in range(len(matriz[i])):     # Percorre cada coluna da linha
        matriz[i][j] *= numero          # Multiplica o elemento atual pelo número fornecido
        print(matriz[i][j], end=" ")    # Exibe o elemento atualizado, permanecendo na mesma linha
    print()                             # Quebra de linha após cada linha da matriz
