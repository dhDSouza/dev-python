# Matriz quadrada 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Dois loops para acessar e exibir apenas os elementos da diagonal principal
for i in range(len(matriz)):        # Percorre cada linha da matriz
    for j in range(len(matriz[i])): # Percorre cada coluna da linha
        if j == i:                  # Verifica se o índice da coluna é igual ao da linha (condição para a diagonal principal)
            print(matriz[i][j])     # Exibe o elemento da diagonal principal
