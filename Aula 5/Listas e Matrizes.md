# Listas e Matrizes em Python

## Objetivo da Aula

Hoje, vamos explorar como trabalhar com **listas** e **matrizes** em Python, que são tipos de dados muito úteis para armazenar e organizar informações. Vamos ver como criar, acessar, modificar e percorrer listas e matrizes, e entender suas principais diferenças.

## O que são Listas?

Listas são estruturas de dados que armazenam uma coleção de elementos. Elas são **mutáveis**, o que significa que você pode alterar, adicionar ou remover elementos depois de criá-las. Listas permitem armazenar qualquer tipo de dado (números, strings, outras listas, etc.).

### Criando uma Lista

Para criar uma lista em Python, basta colocar os elementos entre colchetes `[ ]`, separados por vírgulas:

```python
frutas = ["maçã", "banana", "laranja"]
```

### Acessando Elementos de uma Lista

Para acessar um elemento específico de uma lista, usamos seu índice. O índice do primeiro elemento é `0`, o segundo é `1`, e assim por diante.

```python
print(frutas[0])  # Saída: maçã
print(frutas[1])  # Saída: banana
```

### Modificando Elementos

Como listas são mutáveis, é fácil modificar um valor atribuindo um novo valor ao índice desejado:

```python
frutas[1] = "morango"
print(frutas)  # Saída: ['maçã', 'morango', 'laranja']
```

### Adicionando e Removendo Elementos

- **Adicionar**: usamos o método `append()` para adicionar um elemento ao final da lista.
- **Remover**: usamos o método `remove()` ou `pop()` para remover elementos.

```python
frutas.append("abacaxi")
print(frutas)  # Saída: ['maçã', 'morango', 'laranja', 'abacaxi']

frutas.remove("morango")
print(frutas)  # Saída: ['maçã', 'laranja', 'abacaxi']
```

---

## Estruturas de Repetição `for` com Listas

É muito comum usar laços de repetição `for` para iterar por cada elemento de uma lista.

### Exemplo: Imprimindo Todos os Elementos de uma Lista

```python
for fruta in frutas:
    print(fruta)
```

Isso imprime cada elemento da lista `frutas` em uma linha separada.

### Exemplo Prático: Filtrando Itens

Suponha que queremos imprimir apenas as frutas cujo nome tem mais de 5 letras.

```python
for fruta in frutas:
    if len(fruta) > 5:
        print(fruta)
```

---

## O que são Matrizes?

Matrizes são listas de listas. Elas são úteis para armazenar dados em forma de **linhas e colunas** e são usadas em problemas que envolvem tabelas ou grades de informações (por exemplo, um tabuleiro de jogo).

### Criando uma Matriz

Para criar uma matriz, colocamos listas dentro de outra lista. Cada lista interna representa uma linha da matriz.

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Nesse caso, temos uma matriz 3x3 (3 linhas e 3 colunas).

### Acessando Elementos de uma Matriz

Para acessar um elemento, primeiro referenciamos a linha e depois a coluna:

```python
print(matriz[0][0])  # Saída: 1
print(matriz[1][2])  # Saída: 6
```

---

## Percorrendo Matrizes com `for`

Para percorrer uma matriz, geralmente usamos dois laços `for` aninhados: um para as linhas e outro para as colunas.

### Exemplo: Imprimindo Cada Elemento da Matriz

```python
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()  # Cria uma nova linha após cada linha da matriz
```

Isso imprime a matriz em um formato mais organizado, assim:

```bash
1 2 3
4 5 6
7 8 9
```

## Manipulando Matrizes com Laços de Repetição

Em uma matriz, temos que lidar com `linhas` e `colunas`, o que geralmente exige o uso de laços `for` aninhados.

### Exemplo: Modificando Cada Elemento da Matriz

Suponha que queremos adicionar `1` a cada elemento da matriz. Podemos fazer isso percorrendo cada linha e coluna com dois laços `for` aninhados:

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Percorrendo cada linha e cada coluna
for i in range(len(matriz)):            # Percorre as linhas
    for j in range(len(matriz[i])):     # Percorre as colunas dentro da linha
        matriz[i][j] += 1               # Soma 1 ao valor do elemento atual

# Exibindo a matriz modificada
for linha in matriz:
    print(linha)
```

## Exercícios Práticos

1. **Multiplicação de Matrizes Simples**: Multiplique cada número de uma matriz 2x2 por um valor específico e imprima a matriz resultante.

    ```python
    matriz = [
        [1, 2],
        [3, 4]
    ]
    ```

2. **Buscar em uma Matriz**: Dada uma matriz de nomes, escreva um código que verifica se um nome específico está presente.

    ```python
    matriz_nomes = [
        ["Alice", "Bob"],
        ["Carol", "Dave"]
    ]
    ```

3. **Exibir Diagonal de uma Matriz Quadrada**: Dada uma matriz quadrada (número de linhas igual ao número de colunas), imprima a diagonal principal.

    ```python
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    ```
