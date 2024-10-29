# Usando dois laços for aninhados para criar uma matriz 3x3.
# O laço externo controla as linhas e o interno as colunas.

# Inicializando um contador para preencher os números de 1 a 9.
contador = 1

for i in range(3):                  # Laço para cada linha (3 linhas).
    for j in range(3):              # Laço para cada coluna dentro da linha (3 colunas).
        print(contador, end=" ")    # Imprime o número atual e permanece na mesma linha.
        contador += 1               # Incrementa o contador para o próximo número.
    print()                         # Pula para a próxima linha após 3 números.

# ----------------------------------------
# Outra maneira de resolver o exercício é:
# ----------------------------------------

# Inicializando uma lista vazia que representará a matriz 3x3.
matriz = []

# Usando dois loops para preencher a matriz com números de 1 a 9.
contador = 1

for i in range(3):              # Laço para cada linha
    linha = []                  # Lista vazia que representará uma linha da matriz
    for j in range(3):          # Laço para cada coluna dentro da linha
        linha.append(contador)  # Adiciona o próximo número na linha
        contador += 1           # Incrementa o contador para o próximo número
    matriz.append(linha)        # Adiciona a linha completa à matriz

# Exibindo a matriz em formato de matriz 3x3.
for linha in matriz:
    print(linha)
