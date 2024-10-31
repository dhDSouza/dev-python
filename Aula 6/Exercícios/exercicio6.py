# Saldo inicial da caixinha de dinheiro
saldo = 100.0

while True:
    print(f"Saldo atual: R${saldo:.2f}")
    
    # Pede ao usuário que informe a operação desejada
    acao = input("Digite 'depositar', 'sacar' ou 'sair' para encerrar: ").lower()
    
    if acao == "sair":
        print(f"Encerrando a caixinha. Saldo final: R${saldo:.2f}")
        break
    
    elif acao == "depositar":
        
        # Converte a entrada para um valor numérico
        valor = float(input("Digite o valor a depositar: R$"))
        saldo += valor
        print(f"R${valor:.2f} adicionados com sucesso!")
    
    elif acao == "sacar":
        
        valor = float(input("Digite o valor a sacar: R$"))
        # Verifica se possuí saldo suficiente para o saque
        if valor <= saldo:
            saldo -= valor
            print(f"R${valor:.2f} retirados com sucesso!")
        else:
            print("Saldo insuficiente para realizar a retirada.")

    else:
        print("Opção inválida! Tente 'depositar', 'sacar' ou 'sair'.")
