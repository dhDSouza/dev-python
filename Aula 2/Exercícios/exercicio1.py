# Pedindo para o usuário digitar seu nome, idade e altura e armazenando esses valores nas variáveis.

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
altura = float(input("Digite a sua altura: "))

# 1ª forma de mostrar as informações:
# Convertendo os valores para texto (string) e juntando com outras palavras para formar uma frase.

print("Olá, " + nome + ". Você tem " + str(idade) + " anos e " + str(altura) + "m de altura.")

# 2ª forma de mostrar as informações:
# Usando uma forma mais prática de montar a frase com "f-strings" (basta colocar um "f" antes das aspas).
# Colocamos as variáveis entre chaves {} e elas aparecem no texto automaticamente.

print(f"Olá, {nome}. Você tem {idade} anos e {altura}m de altura.")
