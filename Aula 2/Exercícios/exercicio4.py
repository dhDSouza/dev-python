# Pedindo para o usuário digitar seu peso (em kg) e sua altura (em metros) e armazenando esses valores.

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em m: "))

# Calculando o IMC (Índice de Massa Corporal) usando a fórmula: peso dividido pela altura ao quadrado.

imc = peso / (altura ** 2)

# 1ª forma de exibir o IMC: Mostrando o valor completo sem limitar as casas decimais.

print(f"O seu IMC é: {imc}")

# 2ª forma de exibir o IMC: Mostrando o valor com apenas 2 casas decimais para facilitar a leitura.

print(f"O seu IMC é: {imc:.2f}")
