# Função para encontrar todos os números ímpares em um intervalo
def impares_na_faixa(inicio, fim):
    # Cria uma lista vazia onde serão armazenados os números ímpares
    impares = []
    
    # Laço de repetição que percorre todos os números no intervalo [inicio, fim]
    # O "range(inicio, fim + 1)" garante que o número "fim" também será incluído
    for num in range(inicio, fim + 1):
        # Verifica se o número é ímpar (resto da divisão por 2 diferente de zero)
        if num % 2 != 0:
            # Se for ímpar, adiciona o número na lista "impares"
            impares.append(num)
    
    # Retorna a lista com os números ímpares encontrados no intervalo
    return impares

# Chama a função para imprimir os números ímpares entre 3 e 10
# O resultado será uma lista com os números ímpares no intervalo
print(f"Números ímpares na faixa: {impares_na_faixa(3, 10)}")
