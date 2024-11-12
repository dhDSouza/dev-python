# Aula de Python: Funções Úteis e Estruturas

## Objetivo da Aula

Nesta aula, vamos explorar:

- O uso da estrutura `match-case`, que ajuda a organizar melhor certas estruturas de decisão.
- Dicionários, que são estruturas de dados chave-valor muito poderosas.
- Fatiamento de listas, que facilita o acesso a partes específicas de listas.

## 1. `match-case`: Estrutura de Controle de Fluxo

O `match-case` é uma estrutura de decisão introduzida no `Python 3.10` que nos permite comparar valores de forma organizada e elegante, lembrando o `switch-case` que vemos em outras linguagens de programação como o `Java`.

**Por que usar `match-case`?**

Imagine que temos uma série de condições para testar um valor e executar ações específicas para cada caso. Sem o `match-case`, precisaríamos usar vários `if-elif-else`, o que pode deixar o código mais longo e difícil de ler. Com `match-case`, conseguimos organizar essas condições de forma mais clara.

**Exemplo Básico:**

Vamos criar uma função que recebe uma resposta ("sim", "não" ou qualquer outra) e retorna uma mensagem específica para cada caso:

```python
def analisar_resposta(resposta):
    match resposta:
        case "sim":
            return "Você concordou!"
        case "não":
            return "Você discordou!"
        case _:
            return "Resposta não reconhecida."
```

**Explicação:**

- **`match`**: É a palavra-chave que inicia a estrutura.
- **`case`**: Define cada condição que queremos testar.
- **`_`**: Representa o "coringa" e captura qualquer valor que não corresponde a nenhum caso específico. Ideal para tratarmos o que for inesperado.

**Exemplo Prático com Tipos de Dados:**

O `match-case` pode também reconhecer o tipo de variável passado para ele. Isso é útil em funções que aceitam múltiplos tipos:

```python
def identificar_tipo(dado):
    match dado:
        case int():
            return "É um número inteiro."
        case str():
            return "É uma string."
        case list():
            return "É uma lista."
        case _:
            return "Tipo desconhecido."
```

## 2. Dicionários em Python

Dicionários (`dict`) são uma estrutura de dados que armazena pares de `chave-valor`, funcionando como uma espécie de "mapa" de dados, onde cada chave aponta para um valor específico.

**Definindo um Dicionário:**

```python
pessoa = {"nome": "Daniel", "idade": 30, "cidade": "São Leopoldo"}
```

Neste exemplo:

- `"nome"`, `"idade"`, e `"cidade"` são as chaves.
- `"Daniel"`, `30`, e `"São Leopoldo"` são os valores correspondentes.

### Acessando Dados no Dicionário

Para acessar um valor, usamos a chave:

```python
nome = pessoa["nome"]
print(nome)  # Saída: Daniel
```

Ou então, usamos o método `get()`, que é mais seguro:

```python
idade = pessoa.get("idade", "Chave não encontrada")
print(idade)  # Saída: 30
```

O `get()` permite que a gente forneça um valor padrão caso a chave não exista, evitando erros.

### Principais Funções de Dicionários

1. **`keys()`**: Retorna todas as chaves do dicionário.
2. **`values()`**: Retorna todos os valores.
3. **`items()`**: Retorna pares de chave-valor, cada um como uma tupla.

Exemplo de uso:

```python
print(pessoa.keys())   # Saída: dict_keys(['nome', 'idade', 'cidade'])
print(pessoa.values()) # Saída: dict_values(['Daniel', 30, 'São Leopoldo'])
print(pessoa.items())  # Saída: dict_items([('nome', 'Daniel'), ('idade', 30), ('cidade', 'São Leopoldo')])
```

### Modificando o Dicionário

Para adicionar ou modificar valores, basta referenciar a chave e atribuir um valor:

```python
pessoa["idade"] = 31  # Modifica a idade
pessoa["profissão"] = "Programador"  # Adiciona nova chave-valor
print(pessoa)
```

Para remover uma chave, usamos `del`:

```python
del pessoa["cidade"]
print(pessoa)  # Saída: {'nome': 'Daniel', 'idade': 31, 'profissão': 'Programador'}
```

## 3. Fatiamento de Listas

Fatiamento de listas é uma técnica para acessar partes de uma lista usando uma sintaxe específica `[inicio:fim:passo]`.

**Exemplo de Lista:**

```python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Exemplos de Fatiamento

1. **Selecionando Elementos por Intervalo**:

   ```python
   print(numeros[2:5])  # Saída: [2, 3, 4]
   ```

2. **Fatiamento com Passo**:
   O passo define o intervalo entre os elementos do fatiamento:

   ```python
   print(numeros[::2])  # Saída: [0, 2, 4, 6, 8] - De 2 em 2
   print(numeros[::-1]) # Saída: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - Inverte a lista
   ```

3. **Excluir Elementos Usando Fatiamento**:

   Podemos modificar a lista usando fatiamento, eliminando partes dela:

   ```python
   numeros[0:3] = []  # Remove os três primeiros elementos
   print(numeros)     # Saída: [3, 4, 5, 6, 7, 8, 9]
   ```

## Exercícios Práticos

Para reforçar o aprendizado, vamos realizar alguns exercícios usando o que vimos:

1. **Exercício com `match-case`**:

   Crie uma função chamada `classificar_nota` que recebe uma nota (de 0 a 10) e retorne:

   - `"Aprovado"` para notas acima de 7.
   - `"Recuperação"` para notas entre 5 e 7.
   - `"Reprovado"` para notas abaixo de 5.

2. **Exercício com Dicionários**:

   Crie um dicionário chamado `curso` para armazenar informações sobre um curso (ex.: nome, professor, carga horária). Depois, adicione uma nova chave chamada `"nível"` com o valor `"básico"`, `"intermediário"` ou `"avançado"`. Finalmente, acesse e exiba o nome do curso e o nível.

3. **Exercício com Fatiamento de Listas**:

   Dada a lista `numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]`, realize as seguintes operações:

   - Selecione e exiba os números de índice 2 a 5.
   - Exiba todos os números dos índices ímpares usando fatiamento com passo.
   - Inverta a lista e exiba o resultado.

4. **Exercício Completo**:

   Crie uma função `processar_dados` que recebe um dicionário contendo dados variados e uma lista de números. Dentro da função, faça:

   - Um `match-case` que identifique e exiba o tipo de dado em cada chave do dicionário (ex.: `int`, `str`, `list`).
   - Use fatiamento para exibir apenas os três primeiros e os três últimos números da lista.
