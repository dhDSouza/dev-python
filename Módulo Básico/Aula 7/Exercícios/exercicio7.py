# Função para classificar idades em diferentes faixas etárias
def classificar_idades(idades):
    # Dicionário para armazenar a contagem de pessoas em cada faixa etária
    # Inicializa com 0 para cada categoria: crianças, adolescentes, adultos e idosos
    classificacao = {
        "crianças": 0,
        "adolescentes": 0,
        "adultos": 0,
        "idosos": 0
    }

    # Laço para iterar sobre todas as idades fornecidas na lista "idades"
    for idade in idades:
        # Verifica se a idade está na faixa de 0 a 12 anos (inclusive)
        if idade >= 0 and idade <= 12:
            classificacao["crianças"] += 1  # Incrementa a contagem de crianças
        # Verifica se a idade está na faixa de 13 a 17 anos (inclusive)
        elif idade <= 17:
            classificacao["adolescentes"] += 1  # Incrementa a contagem de adolescentes
        # Verifica se a idade está na faixa de 18 a 64 anos (inclusive)
        elif idade <= 64:
            classificacao["adultos"] += 1  # Incrementa a contagem de adultos
        # Se a idade for maior que 64 anos, considera como idoso
        else:
            classificacao["idosos"] += 1  # Incrementa a contagem de idosos
    
    # Retorna o dicionário com a contagem das pessoas em cada faixa etária
    return classificacao

# Chama a função com uma lista de idades e imprime a classificação das idades
print(classificar_idades([3, 14, 20, 67, 8, 33, 73, 17]))
