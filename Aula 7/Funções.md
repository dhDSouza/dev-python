# Aula: Funções em Python

## 1. O Que é uma Função?

Uma **função** é um bloco de código que realiza uma tarefa específica e pode ser chamado em diferentes partes do código. Em Python, as funções ajudam a **organizar** e **reutilizar** código, evitando repetição e tornando o código mais claro e modular.

### Estrutura Básica de uma Função

Uma função é definida usando a palavra-chave `def`, seguida por um nome, parênteses `()`, e dois pontos `:`. O código que pertence à função deve ser indentado.

```python
def nome_da_funcao():
    # Bloco de código da função
```

### Exemplo Simples: Função que Exibe uma Mensagem

```python
def saudacao():
    print("Olá, bem-vindo à aula de funções!")
    
# Chamando a função
saudacao()
```

## 2. Parâmetros e Argumentos

As funções podem receber **parâmetros**, que são variáveis locais que você define na criação da função e que podem ser diferentes a cada chamada. Os valores passados para a função são chamados de **argumentos**.

```python
def saudacao(nome):
    print(f"Olá, {nome}! Bem-vindo à aula de funções!")
    
saudacao("Daniel")
```

- `nome` é um **parâmetro** da função `saudacao`.
- `"Daniel"` é um **argumento** passado ao chamar a função.

### Função com Múltiplos Parâmetros

```python
def soma(a, b):
    resultado = a + b
    print(f"A soma de {a} e {b} é {resultado}")

soma(5, 3)  # Saída: A soma de 5 e 3 é 8
```

## 3. Funções com Retorno

Funções também podem retornar valores usando a palavra-chave `return`. Esse valor pode ser armazenado em uma variável para uso posterior.

### Exemplo: Função de Soma com Retorno

```python
def soma(a, b):
    return a + b

resultado = soma(10, 15)
print(f"O resultado da soma é: {resultado}")
```

- O `return` faz a função `soma` retornar um valor, que pode ser usado em outras partes do código.

### Função com Vários Retornos

Também é possível retornar múltiplos valores usando uma tupla.

```python
def operacoes(a, b):
    soma = a + b
    diferenca = a - b
    produto = a * b
    return soma, diferenca, produto

resultado = operacoes(10, 5)
print(resultado)  # Saída: (15, 5, 50)
```

## 4. Argumentos Opcionais (Com Valores Padrão)

Em Python, podemos definir valores **padrão** para parâmetros, tornando-os opcionais ao chamar a função.

```python
def saudacao(nome="aluno"):
    print(f"Olá, {nome}!")

saudacao()  # Saída: Olá, aluno!
saudacao("Daniel")  # Saída: Olá, Daniel!
```

## 5. Argumentos Arbitrários

Às vezes, não sabemos quantos argumentos serão passados para a função. Podemos usar `*args` para receber múltiplos argumentos posicionais e `**kwargs` para múltiplos argumentos nomeados.

### Usando `*args`

```python
def lista_amigos(*amigos):
    for amigo in amigos:
        print(f"Olá, {amigo}!")

lista_amigos("Ana", "Bruno", "Carlos") 
# Saída:
# Olá, Ana!
# Olá, Bruno!
# Olá, Carlos!
```

### Usando `**kwargs`

```python
def informacoes_pessoais(**info):
    for chave, valor in info.items():
        print(f"{chave.capitalize()}: {valor}")

informacoes_pessoais(nome="Daniel", idade=28, cidade="São Leopoldo")
# Saída:
# Nome: Daniel
# Idade: 28
# Cidade: São Leopoldo
```

## 6. Escopo de Variáveis

As variáveis definidas dentro de uma função têm **escopo local**, o que significa que só podem ser acessadas dentro dessa função. Variáveis definidas fora de funções têm **escopo global**.

```python
def minha_funcao():
    x = 10  # Variável local
    print(x)

minha_funcao()
print(x)  # Erro: 'x' não está definido no escopo global
```

## 7. Funções Lambda

As **funções lambda** são funções anônimas, úteis para operações simples. Elas são definidas com a palavra-chave `lambda` e geralmente são usadas para funções de uma linha.

```python
# Função lambda para somar dois números
soma = lambda x, y: x + y
print(soma(5, 7))  # Saída: 12
```

## Exemplos Práticos

### Exemplo 1: Calculadora Simples

```python
def calculadora(a, b, operacao):
    if operacao == "soma":
        return a + b
    elif operacao == "subtracao":
        return a - b
    elif operacao == "multiplicacao":
        return a * b
    elif operacao == "divisao":
        if b != 0:
            return a / b
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"

resultado = calculadora(10, 2, "multiplicacao")
print(f"Resultado: {resultado}")
```

### Exemplo 2: Função para Contar Ocorrências

```python
def contar_ocorrencias(texto, palavra):
    return texto.lower().count(palavra.lower())

texto = "Python é muito divertido. Aprender Python é ótimo!"
print(contar_ocorrencias(texto, "Python"))  # Saída: 2
```

## Exercícios Práticos

### Exercícios Fáceis

1. **Saudação Personalizada**
   - Crie uma função chamada `saudacao` que recebe um nome e exibe uma mensagem de boas-vindas com esse nome.

2. **Multiplicação Simples**
   - Escreva uma função `multiplicar` que receba dois números e retorne o produto deles.

3. **Cálculo de Média**
   - Crie uma função chamada `calcular_media` que recebe uma lista de números e retorna a média deles.

4. **Verificar Palíndromo (Desafio)**
   - Escreva uma função `palindromo` que verifica se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços).
