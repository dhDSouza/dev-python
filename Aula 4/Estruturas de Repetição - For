# Estruturas de Repetição `for` em Python

## Objetivo da Aula

Nesta aula, vamos aprender sobre o **laço de repetição `for`** no Python. Exploraremos como ele funciona, quais são as suas aplicações, e veremos exemplos práticos que ajudam a entender como usá-lo para resolver problemas que envolvem repetição de tarefas.

## O que é o Laço de Repetição `for`?

Um laço de repetição, ou `loop`, é uma estrutura que permite executar um bloco de código repetidamente. O laço `for` é usado quando sabemos antecipadamente quantas vezes o loop precisa ser repetido. Ele é excelente para iterar sobre coleções (como listas, strings, dicionários) ou executar um bloco de código um número específico de vezes.

### Analogia

Imagine que você está organizando um evento e precisa entregar 100 convites, um por um. Usar um laço de repetição seria como automatizar esse processo, fazendo com que, a cada iteração, um convite seja entregue, sem que você precise realizar a tarefa manualmente várias vezes.

## Sintaxe Básica do `for` no Python

A sintaxe do `for` no Python é bastante simples e intuitiva. Ela pode ser usada para percorrer uma sequência, como uma lista ou uma string.

```python
for variavel in sequencia:
    # bloco de código a ser repetido
```

Aqui, `variavel` é o elemento atual da `sequencia` e o bloco de código dentro do laço será executado repetidamente para cada item da sequência.

### Exemplo Simples: Percorrendo uma Lista

Vamos começar com um exemplo simples onde percorremos uma lista de números e imprimimos cada um deles.

```python
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)
```

**Explicação**:

- A variável `numero` assume o valor de cada elemento na lista `numeros` a cada iteração do loop.
- O bloco de código `print(numero)` é executado uma vez para cada valor da lista.

### Função `range()`: Repetições com Contagem

Se quisermos repetir um bloco de código um número fixo de vezes, usamos a função `range()`. O `range()` gera uma sequência de números, começando por padrão em 0 e indo até um valor especificado.

#### Exemplo: Usando `range()`

```python
for i in range(5):
    print(f"Contagem: {i}")
```

**Explicação**:

- `range(5)` gera uma sequência de números de 0 a 4 (não inclui o 5).
- A variável `i` assume cada valor da sequência, e o código `print(f"Contagem: {i}")` é executado em cada iteração, mostrando a contagem de 0 a 4.

### Argumentos de `range()`

A função `range()` pode receber até três argumentos:

1. **`start` (início):** o valor inicial da sequência (inclusivo).
2. **`stop` (fim):** o valor final (não inclusivo).
3. **`step` (passo):** o intervalo entre os números.

#### Exemplo: Usando `start`, `stop` e `step`

```python
for i in range(1, 10, 2):
    print(i)
```

**Explicação**:

- `range(1, 10, 2)` começa em 1, vai até 9 (não inclui o 10) e incrementa de 2 em 2.
- O loop imprime os números: 1, 3, 5, 7, 9.

### Percorrendo Strings com `for`

O laço `for` também pode ser usado para percorrer strings, permitindo que cada caractere seja processado individualmente.

#### Exemplo: Percorrendo uma String

```python
palavra = "Python"

for letra in palavra:
    print(letra)
```

**Explicação**:

- A variável `letra` assume o valor de cada caractere na string `palavra`.
- O código imprime cada letra da palavra "Python", uma por linha.

### Laços Aninhados (Nested Loops)

Você pode colocar um laço `for` dentro de outro laço `for`, o que é útil para trabalhar com estruturas de dados mais complexas, como listas de listas (matrizes).

#### Exemplo: Laços Aninhados

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()  # para criar uma nova linha após cada linha da matriz
```

**Explicação**:

- O primeiro `for` percorre cada linha da matriz.
- O segundo `for` percorre cada elemento da linha atual.
- O resultado será a impressão da matriz no formato original.

### Controle do Laço com `break` e `continue`

#### `break` - Interrompe o laço

O comando `break` pode ser usado para **parar** o laço prematuramente, assim que uma condição específica for satisfeita.

```python
for i in range(10):
    if i == 5:
        break  # Interrompe o laço quando i for 5
    print(i)
```

**Explicação**:

- O laço imprime números de 0 a 4. Quando `i` é igual a 5, o `break` interrompe o loop.

#### `continue` - Pula para a Próxima Iteração

O comando `continue` pode ser usado para **pular** o restante do código na iteração atual e passar para a próxima.

```python
for i in range(5):
    if i == 3:
        continue  # Pula a iteração quando i for 3
    print(i)
```

**Explicação**:

- O laço imprime 0, 1, 2, 4 (pulando o 3, por causa do `continue`).

### Exemplo Prático: Tabuada com `for`

Vamos usar o laço `for` para criar uma tabuada simples do número 5.

```python
numero = 5

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
```

**Explicação**:

- O laço `for` itera de 1 a 10.
- Em cada iteração, multiplicamos o `numero` (5) pelo valor de `i` e imprimimos o resultado.

### Exercícios Práticos

1. **Contagem Regressiva:** Crie um programa que faça uma contagem regressiva de 10 até 0 e, ao final, exiba a mensagem "Lançamento!".

2. **Números Pares:** Escreva um programa que imprime todos os números pares entre 1 e 20 usando um `for`.

3. **Somatório:** Crie um programa que solicita ao usuário um número inteiro positivo e, em seguida, calcula e exibe a soma de todos os números de 1 até o número fornecido.

4. **Tabuada:** Crie um programa que recebe um número do usuário e imprime a tabuada desse número de 1 a 10.

5. **Percorrendo Listas de Nomes:** Faça um programa que peça ao usuário para inserir 5 nomes em uma lista e, em seguida, use um laço `for` para exibir cada nome da lista.

6. **Matriz:** Crie um programa que imprime uma matriz 3x3 de números (de 1 a 9) usando dois laços `for` aninhados.
