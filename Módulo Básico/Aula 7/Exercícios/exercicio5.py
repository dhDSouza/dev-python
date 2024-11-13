def palindromo_avancado(frase):
    # Caracteres que devem ser ignorados ou substituídos
    invalido = [' ', ',', '.', '!', '?', ';', ':', '-', '_']
    a = ['ã', 'á', 'à', 'â']
    e = ['é', 'ê']
    u = ['ú', 'ü']
    
    # Variável para armazenar o texto formatado
    texto_formatado = ''

    # Itera sobre cada letra da frase
    for letra in frase.lower():
        if letra not in invalido:  # Ignora caracteres inválidos
            if letra in a:
                texto_formatado = texto_formatado.join('a')  # Substitui os caracteres 'a' com til ou acentuados por 'a'
            elif letra in e:
                texto_formatado = texto_formatado.join('e')  # Substitui os caracteres 'e' acentuados por 'e'
            elif letra in u:
                texto_formatado = texto_formatado.join('u')  # Substitui os caracteres 'u' acentuados ou com diacríticos por 'u'
            elif letra == 'í':
                texto_formatado = texto_formatado.join('i')  # Substitui 'í' por 'i'
            elif letra == 'ç':
                texto_formatado = texto_formatado.join('c')  # Substitui 'ç' por 'c'
            else:
                texto_formatado += letra  # Adiciona o caractere que não precisa de substituição

    # Verifica se o texto formatado é um palíndromo
    return texto_formatado == texto_formatado[::-1]

# Teste da função
print(palindromo_avancado("A man, a plan, a canal, Panama!"))  # Saída: True
