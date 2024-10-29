# Pedindo para o usuário digitar sua idade e guardando esse valor na variável 'idade'.

idade = int(input("Digite a sua idade: "))

# Verificando a idade para decidir a categoria do usuário:
# - Se for menor que 18, é menor de idade.
# - Se for entre 18 e 64, é maior de idade.
# - Se for 65 ou mais, é considerado idoso.

if idade < 18:
    print("Você é menor de idade.")
elif idade < 65:
    print("Você é maior de idade.")
else:
    print("Você é idoso.")
