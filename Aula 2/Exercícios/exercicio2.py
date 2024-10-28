# Pedindo para o usuário digitar dois números e armazenando esses valores nas variáveis.

primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite outro número: "))

# Calculando a soma, subtração, multiplicação e divisão desses dois números e salvando cada resultado em uma variável.

soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
multiplicacao = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero

# Mostrando os resultados dos cálculos de forma mais organizada e fácil de entender usando f-strings.

print(f"O valor da soma entre {primeiro_numero} e {segundo_numero} é: {soma}")
print(f"O valor da subtração entre {primeiro_numero} e {segundo_numero} é: {subtracao}")
print(f"O valor da multiplicação entre {primeiro_numero} e {segundo_numero} é: {multiplicacao}")
print(f"O valor da divisão entre {primeiro_numero} e {segundo_numero} é: {divisao}")
