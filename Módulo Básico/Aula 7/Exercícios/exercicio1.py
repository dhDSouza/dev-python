def saudacao_horario(nome, horario):
    # Verifica se o horário está entre 5 e 12 (inclusive), para determinar a saudação "Bom dia"
    if horario >= 5 and horario <= 12:
        saudacao = "Bom dia"
    # Verifica se o horário está entre 12 e 18 (inclusive), para determinar a saudação "Boa tarde"
    elif horario <= 18:
        saudacao = "Boa tarde"
    # Caso o horário não se encaixe nos intervalos anteriores, a saudação será "Boa noite"
    else:
        saudacao = "Boa noite"
    
    # Verifica se o horário informado é inválido (menor ou igual a 0 ou maior que 24)
    if horario <= 0 or horario > 24:
        return "Horário inválido"
    
    # Retorna a saudação formatada com o nome da pessoa
    return f"{saudacao}, {nome}!"

# Exemplo de chamada da função, com o nome "Daniel" e horário 3
saudacao_horario("Daniel", 3)
