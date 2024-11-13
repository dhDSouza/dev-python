# Usando um laço for para percorrer os números de 1 a 20.
# A função range(2, 21, 2) começa em 2 e pula de 2 em 2, assim pega apenas os números pares.

for numero in range(2, 21, 2):
    print(numero)


# Usando um laço for para percorrer todos os números de 1 a 20.
# Em cada iteração, verifica se o número é par usando o operador módulo (%).
# Se o resto da divisão por 2 for zero, o número é par e será exibido.

for numero in range(1, 21):
    if numero % 2 == 0:  # Verificando se o número é par
        print(numero)
