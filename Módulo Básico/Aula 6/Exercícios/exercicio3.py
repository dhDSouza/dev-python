# Define a senha correta
senha_correta = "python123"

# Solicita ao usuário para digitar a senha
senha = input("Digite a senha: ")

# Executa o loop enquanto a senha estiver incorreta
while senha != senha_correta:
    senha = input("Senha incorreta! Tente novamente: ")

# Exibe a mensagem quando a senha está correta
print("Acesso concedido")
