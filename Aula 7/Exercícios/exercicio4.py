def contar_vogais(texto):
    # Lista de vogais, usadas para verificar as letras do texto
    vogais = ['a', 'e', 'i', 'o', 'u']

    # Dicionário para armazenar a contagem de cada vogal
    contagem = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0
    }

    # Itera sobre cada letra do texto, convertendo para minúscula para garantir que a contagem seja case-insensitive
    for letra in texto.lower():
        # Verifica se a letra é uma vogal
        if letra.lower() in vogais:
            contagem[letra.lower()] += 1  # Incrementa a contagem da vogal correspondente
    
    # Retorna o dicionário com a contagem das vogais
    return contagem

# Chama a função com um texto de exemplo e imprime o resultado
print(contar_vogais("O rato roeu a roupa do rei de roma!"))
