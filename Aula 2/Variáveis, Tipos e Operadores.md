# Aula 2: Variáveis, Tipos de Dados e Operações Básicas

## Conceito de Variáveis e Tipos de Dados

### O que são Variáveis?

- **Definição**: Um espaço na memória do computador que armazena valores que podem ser utilizados e modificados durante a execução do programa.
- **Exemplo Prático**: Imagine uma “caixa” que guarda um valor específico — como a idade ou o nome de uma pessoa.

- **Regras para criar variáveis**:

  - Podem conter letras, números e o caractere `_`, mas não podem começar com números.
  - São sensíveis a maiúsculas e minúsculas (idade é diferente de Idade).
  - Evite usar palavras reservadas como `class`, `def`, `if`, etc.

### Tipos de Dados em Python

| Tipo           | Exemplo               | Descrição                                                                                   |
|:----------------:|:-----------------------:|:---------------------------------------------------------------------------------------------:|
| `int`          | `x = 5`              | Números inteiros, positivos ou negativos, sem parte decimal.                                |
| `float`        | `y = 3.14`           | Números de ponto flutuante, ou seja, números com parte decimal.                             |
| `str`          | `nome = "Daniel"`    | Cadeia de caracteres (string), usada para representar texto.                                |
| `bool`         | `flag = True`        | Tipo booleano, pode ser `True` (verdadeiro) ou `False` (falso).                             |
| `list`         | `lista = [1, 2, 3]`  | Lista de itens, que podem ser de tipos diferentes, e é mutável (pode ser alterada).         |
| `tuple`        | `tupla = (1, 2, 3)`  | Semelhante a uma lista, mas é imutável (não pode ser alterada).                             |
| `set`          | `conjunto = {1, 2, 3}`| Conjunto de elementos únicos, não possui ordem específica e não permite duplicatas.         |
| `dict`         | `dicionario = {"nome": "Daniel", "idade": 30}` | Estrutura de mapeamento de pares chave-valor, similar a um objeto JSON.                     |
| `NoneType`     | `variavel = None`    | Representa a ausência de valor ou um valor nulo.                                            |

### Exemplo de Código

```python
nome = "Daniel"     # Uma variável do tipo string
idade = 28          # Uma variável do tipo inteiro
altura = 1.77       # Uma variável do tipo float
eh_estudante = True # Uma variável do tipo bool
```

Para verificar o tipo de uma variável, você pode usar a função `type()`:

**Exemplo**:

```python
numero = 10           # int
pi = 3.14159          # float
mensagem = "Olá"      # str
ativo = True          # bool

print(type(numero))   # <class 'int'>
print(type(pi))       # <class 'float'>
print(type(mensagem)) # <class 'str'>
print(type(ativo))    # <class 'bool'>
```

## Operações Básicas em Python

### Operações Matemáticas

O Python permite realizar várias operações com variáveis, como:

**Operações Matemáticas**:

- Soma (`+`): Adiciona dois números.
- Subtração (`-`): Subtrai um número de outro.
- Multiplicação (`*`): Multiplica dois números.
- Divisão (`/`): Divide um número por outro (resultado sempre em float).
- Divisão Inteira (`//`): Divide e retorna apenas a parte inteira do resultado.
- Módulo (`%`): Retorna o resto da divisão.
- Exponenciação (`**`): Eleva um número à potência de outro.

**Exemplo**:

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.3333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

**Operações com Strings**:

- Concatenar (`+`): Une duas strings.
- Repetir (`*`): Repete uma string.

**Exemplo**:

```python
nome = "Daniel"
saudacao = "Olá, " + nome
print(saudacao)  # "Olá, Daniel"

risada = "Ha" * 3
print(risada)  # "HaHaHa"
```

**Funções Úteis**: `upper()`, `lower()`, `len()`.

- `upper()`: Retorna todos os caracteres maiúsculos.
- `lower()`: Retorna todos os caracteres minúsculos.
- `len()`: Retorna a quantidade de caracteres.

**Exemplo**:

```python
palavra = "Python"
print(palavra.upper())  # Saída: PYTHON
print(palavra.lower())  # Saída: python
print(palavra.len())    # Saída: 6
```

## Interação com o usuário: `input()`

Em Python, usamos a função `input()` para coletar informações diretamente do usuário. O valor digitado é sempre retornado como uma `string` (texto), então, se você precisa de outro tipo, é necessário fazer uma conversão.

```python
nome = input("Qual é o seu nome? ")
print("Olá, " + nome + "!")
```

Nesse exemplo, pedimos para o usuário digitar o nome, e o valor é armazenado na variável nome. Em seguida, usamos `print()` para exibir uma mensagem personalizada.

**Convertendo Tipos com input**:

Como o `input()` retorna sempre uma `string`, se precisarmos de um número, devemos converter o valor.

**Exemplo**:

```python
idade = input("Qual é a sua idade? ")
idade = int(idade)  # Convertendo o valor para inteiro
print("Você tem", idade, "anos.")
```

## Exercícios Práticos

### Exercício 1: Coletando dados do usuário

- **Descrição**: Crie um programa que peça para o usuário digitar:
  - Nome (string)
  - Idade (inteiro)
  - Altura (float)
  - Exiba todas as informações coletadas em uma frase completa.

### Exercício 2: Calculadora Simples

- **Descrição**: Crie um programa que pede ao usuário para inserir dois números e exibe a soma, subtração, multiplicação e divisão desses números.

### Exercício 3: Manipulação de Texto

- **Descrição**: Peça ao usuário para inserir uma palavra e, em seguida, mostre:
  - Quantas letras a palavra possui.
  - A palavra com todas as letras em maiúsculas.

### Exercício 4: Cálculo de IMC

- **Descrição**: Peça para o usuário digitar o peso (em kg) e a altura (em metros).

  - Calcule o IMC usando a fórmula: `IMC = peso / (altura ** 2)`.
  - Exiba o valor do IMC.
