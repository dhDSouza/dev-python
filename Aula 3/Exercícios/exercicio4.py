# Pedindo para o usuário digitar um número e armazenando esse valor na variável 'numero'.

numero = int(input("Digite um número: "))

# Verificando se o número é múltiplo de 3, de 5, ou de ambos.
# - Um número é múltiplo de 3 se o resto da divisão por 3 é zero (numero % 3 == 0).
# - Um número é múltiplo de 5 se o resto da divisão por 5 é zero (numero % 5 == 0).

if numero % 3 == 0 and numero % 5 == 0:
    print("O número é múltiplo de 3 e de 5.")
elif numero % 3 == 0:
    print("O número é múltiplo de 3.")
elif numero % 5 == 0:
    print("O número é múltiplo de 5.")
else:
    print("O número não é múltiplo de 3 nem de 5.")
