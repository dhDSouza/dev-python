def calcular_media_positiva(numeros):
    # Inicializa as variáveis 'soma' e 'quantidade' para armazenar respectivamente a soma dos números positivos e a quantidade deles
    soma, quantidade = 0, 0
    
    # Itera sobre cada número na lista 'numeros'
    for numero in numeros:
        # Verifica se o número é positivo
        if numero > 0:
            soma += numero        # Se for positivo, adiciona à soma
            quantidade += 1       # Aumenta a quantidade de números positivos encontrados
    
    # Se não houver números positivos na lista (quantidade for 0)
    if quantidade == 0:
        resultado = "Não foi possível fazer a média, pois não tem número positivos na lista."
    else:
        # Se houver números positivos, calcula a média
        resultado = soma / quantidade
    
    # Retorna o resultado, que pode ser a média ou uma mensagem de erro
    return resultado

# Chama a função passando uma lista com apenas números negativos
print(calcular_media_positiva([-3, -4, -7, -10, -5, -10]))
