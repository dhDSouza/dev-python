# Pedindo para o usuário digitar a nota do aluno e guardando esse valor na variável 'nota'.

nota = float(input("Digite a nota do aluno (0 a 10): "))

# Verificando a nota para determinar a mensagem adequada:
# - Nota 9 ou 10: "Aprovado com distinção".
# - Nota entre 7 e 8 (inclusive): "Aprovado".
# - Nota menor que 7: "Reprovado".

if nota >= 9 and nota <= 10:
    print("Aprovado com distinção")
elif nota >= 7 and nota < 9:
    print("Aprovado")
else:
    print("Reprovado")
