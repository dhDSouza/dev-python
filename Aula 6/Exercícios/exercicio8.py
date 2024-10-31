# Inicializa a lista para armazenar o histórico de mensagens
historico_mensagens = []

while True:
    # Solicita uma mensagem ao usuário
    mensagem = input("Digite uma mensagem ('sair' para encerrar): ")

    # Encerra o loop se o usuário digitar 'sair'
    if mensagem.lower() == "sair":
        break

    # Adiciona a mensagem ao histórico
    historico_mensagens.append(mensagem)

# Exibe o histórico completo de mensagens após o encerramento do chat
print("\nHistórico de mensagens:")
for msg in historico_mensagens:
    print(f"- {msg}")
