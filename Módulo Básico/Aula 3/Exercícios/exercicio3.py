# Pedindo para o usuário o preço original do produto e guardando esse valor na variável 'preco_original'.

preco_original = float(input("Digite o preço do produto: R$ "))

# Verificando o valor para aplicar o desconto adequado:
# - Se o preço original for maior que 100, aplica 10% de desconto.
# - Se for menor ou igual a 100, aplica 5% de desconto.

if preco_original > 100:
    desconto = 0.10  # 10% de desconto
else:
    desconto = 0.05  # 5% de desconto

# Calculando o valor do desconto e o preço final do produto.
valor_desconto = preco_original * desconto
preco_final = preco_original - valor_desconto

# Exibindo o preço final com desconto.
print(f"O preço com desconto é: R$ {preco_final:.2f}")
