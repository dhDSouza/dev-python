# Matriz de nomes
matriz_nomes = [
    ["Alice", "Bob"],
    ["Carol", "Dave"]
]

# Solicita ao usuário um nome para procurar na matriz
nome = input("Digite o nome que deseja procurar: ")

# Inicializa uma variável de controle para indicar se o nome foi encontrado
existe = False

# Dois loops aninhados para percorrer cada elemento da matriz
for i in range(len(matriz_nomes)):          # Percorre cada linha da matriz
    if existe:                              # Interrompe a busca se o nome já foi encontrado
        break
    for j in range(len(matriz_nomes[i])):   # Percorre cada coluna da linha
        if nome == matriz_nomes[i][j]:      # Verifica se o nome atual corresponde ao nome buscado
            existe = True                   # Marca que o nome foi encontrado
            break                           # Sai do loop interno
        else:
            existe = False                  # Continua buscando até o fim da matriz

# Exibe o resultado da busca
if existe:
    print("O nome está na lista.")
else:
    print("O nome não está na lista.")
