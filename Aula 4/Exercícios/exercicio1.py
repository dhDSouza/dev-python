# Usando um laço for para contar de 10 até 0 de forma regressiva.
# A função range(10, -1, -1) gera números de 10 até 0 (o -1 indica o passo, que é negativo para contagem regressiva).

for i in range(10, -1, -1):
    print(i)

# Exibindo a mensagem final após a contagem regressiva.
print("Lançamento!")


# Usando um laço for para contar de 10 até 0 de forma regressiva, mas de uma maneira diferente.
# A função range(11) gera números de 0 a 10. Em cada iteração, subtraímos o valor de 'i' de 10, 
# o que cria uma contagem decrescente de 10 até 0.

for i in range(11):
    print(f"{10 - i}")  # Subtraindo o valor atual de i de 10 para exibir a contagem regressiva

# Exibindo a mensagem final após a contagem regressiva.
print("Lançamento!")
