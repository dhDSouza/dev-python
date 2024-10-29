# Criando uma lista vazia para armazenar os nomes.
nomes = []

# Usando um laço for para pedir 5 nomes ao usuário.
for i in range(5):
    nome = input(f"Digite o nome {i + 1}: ")
    nomes.append(nome)  # Adicionando cada nome à lista 'nomes'.

# Usando um laço for para exibir cada nome armazenado na lista.
print("Lista de nomes:")
for nome in nomes:
    print(nome)
