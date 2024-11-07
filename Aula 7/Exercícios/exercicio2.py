def calculadora_avancada(a, b, operacoes):
    # Cria uma lista vazia chamada 'resultados' para armazenar os resultados das operações
    resultados = []
    
    # Itera sobre cada operação na lista 'operacoes'
    for operacao in operacoes:
        # Verifica se a operação é uma soma
        if operacao == "soma":
            resultados.append(a + b)  # Adiciona o resultado da soma à lista 'resultados'
        
        # Verifica se a operação é uma subtração
        elif operacao == "subtracao":
            resultados.append(a - b)  # Adiciona o resultado da subtração à lista 'resultados'
        
        # Verifica se a operação é uma multiplicação
        elif operacao == "multiplicacao":
            resultados.append(a * b)  # Adiciona o resultado da multiplicação à lista 'resultados'
        
        # Verifica se a operação é uma divisão
        elif operacao == "divisao":
            # Verifica se o valor de 'b' não é zero para evitar divisão por zero
            if b != 0:
                resultados.append(a / b)  # Adiciona o resultado da divisão à lista 'resultados'
            else:
                resultados.append("Erro: Divisão por zero")  # Se 'b' for zero, adiciona uma mensagem de erro
        
        # Caso a operação não seja reconhecida, adiciona uma mensagem de erro
        else:
            resultados.append("Operação inválida")
    
    # Retorna a lista com os resultados das operações
    return resultados

# Chama a função com os valores a=10, b=0 e uma lista de operações
print(calculadora_avancada(10, 0, ["soma", "divisao", "subtracao", "multiplicacao"]))