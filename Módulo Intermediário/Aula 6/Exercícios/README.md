# Explicação das atividades

## Exercício 1

<details>
<summary>Explicação</summary>
Este código implementa uma **calculadora simples** com interface gráfica usando o módulo `tkinter` em Python. Vou explicar detalhadamente como ele funciona:

### 1. **Importações e Definição da Classe**

```python
import tkinter as tk
from tkinter import ttk
```

- `tkinter`: Módulo de interface gráfica para Python, usado para criar janelas e widgets (botões, entradas, etc.).
- `ttk`: Submódulo de `tkinter` que fornece widgets com uma aparência mais moderna e estilizada (como a `Combobox` e os botões estilizados).

```python
class Calculadora:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Calculadora Básica")
```

- A classe `Calculadora` define a lógica e a interface gráfica do programa. O método `__init__` é o construtor da classe, e ele é chamado quando uma instância da classe é criada.
- A janela principal (`janela`) é passada como argumento, e o título da janela é configurado como "Calculadora Básica".

### 2. **Construção da Interface Gráfica**

O layout da interface gráfica é feito utilizando o método `grid`, que organiza os widgets em uma tabela com linhas e colunas.

#### Campos de Entrada

```python
# Números
ttk.Label(janela, text="Número 1:").grid(row=0, column=0, padx=5, pady=5)
self.num1 = ttk.Entry(janela)
self.num1.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(janela, text="Número 2:").grid(row=1, column=0, padx=5, pady=5)
self.num2 = ttk.Entry(janela)
self.num2.grid(row=1, column=1, padx=5, pady=5)
```

- São criados dois **rótulos** (`Label`), um para o "Número 1" e outro para o "Número 2", com campos de entrada (`Entry`) ao lado de cada um.
  - `num1` e `num2` são variáveis que armazenam as entradas de texto onde o usuário insere os números.
  - O `grid(row=x, column=y)` posiciona esses widgets nas linhas e colunas correspondentes. Por exemplo, o primeiro rótulo é posicionado na linha 0, coluna 0, e a caixa de entrada do número 1 é posicionada na linha 0, coluna 1.

#### Seleção da Operação

```python
# Operação
ttk.Label(janela, text="Operação:").grid(row=2, column=0, padx=5, pady=5)
self.operacao = ttk.Combobox(janela, values=["Soma", "Subtração", "Multiplicação", "Divisão"])
self.operacao.grid(row=2, column=1, padx=5, pady=5)
self.operacao.set("Soma")
```

- Um **rótulo** ("Operação:") e uma **caixa de seleção** (`Combobox`) são criados. O `Combobox` permite ao usuário escolher uma operação entre as opções: "Soma", "Subtração", "Multiplicação" e "Divisão".
  - O método `set("Soma")` define a operação padrão como "Soma".

#### Botão de Calcular

```python
# Botão calcular
self.botao_calcular = ttk.Button(janela, text="Calcular", command=self.calcular)
self.botao_calcular.grid(row=3, column=0, columnspan=2, pady=10)
```

- Um **botão** é criado com o texto "Calcular". Quando o botão for pressionado, o método `calcular` será chamado. O parâmetro `command=self.calcular` associa o evento de clique do botão à função `calcular`.

#### Exibição do Resultado

```python
# Resultado
self.resultado = ttk.Label(janela, text="Resultado: ")
self.resultado.grid(row=4, column=0, columnspan=2, pady=5)
```

- Um **rótulo** (`Label`) é criado para exibir o resultado do cálculo. Inicialmente, ele exibe o texto "Resultado: ", mas esse texto será atualizado com o resultado da operação.

### 3. **Método `calcular` (A Lógica do Cálculo)**

```python
def calcular(self):
    try:
        n1 = float(self.num1.get())
        n2 = float(self.num2.get())
        op = self.operacao.get()

        match(op):
            case "Soma":
                res = n1 + n2
            case "Subtração":
                res = n1 - n2
            case "Multiplicação":
                res = n1 * n2
            case "Divisão":
                if n2 == 0:
                    self.resultado.config(text="Erro: Divisão por zero")
                    return
                res = n1 / n2
            case _:
                res = "Operação inválida"

        self.resultado.config(text=f"Resultado: {res}")
    except ValueError:
        self.resultado.config(text="Erro: Insira números válidos")
```

Este é o método que é chamado quando o usuário clica no botão "Calcular". Ele realiza as seguintes etapas:

1. **Captura os valores inseridos pelo usuário**:
   - `n1 = float(self.num1.get())`: Obtém o valor do primeiro número e o converte para `float`.
   - `n2 = float(self.num2.get())`: Obtém o valor do segundo número e o converte para `float`.
   - `op = self.operacao.get()`: Obtém a operação escolhida no `Combobox`.

2. **Determina a operação a ser realizada**:
   - O comando `match(op)` é usado para verificar qual operação foi escolhida. Dependendo do valor de `op`, ele executa a operação correspondente:
     - Se a operação for "Soma", o resultado é a soma dos dois números.
     - Se a operação for "Subtração", o resultado é a diferença.
     - Se a operação for "Multiplicação", o resultado é o produto.
     - Se a operação for "Divisão", ele verifica se o divisor (`n2`) é zero. Se for, exibe um erro de "Divisão por zero". Caso contrário, realiza a divisão.
   
3. **Exibe o resultado**:
   - Se a operação for bem-sucedida, o resultado é mostrado no rótulo `self.resultado` com o texto `Resultado: {res}`.
   - Se ocorrer um erro, como a tentativa de inserir texto ou caracteres não numéricos, a exceção `ValueError` é capturada e uma mensagem de erro ("Erro: Insira números válidos") é exibida.

### 4. **Execução do Programa**

```python
if __name__ == "__main__":
    janela = tk.Tk()
    app = Calculadora(janela)
    janela.mainloop()
```

- A linha `if __name__ == "__main__":` garante que o código a seguir só será executado se o script for executado diretamente (não se for importado como módulo).
- `janela = tk.Tk()` cria a janela principal da aplicação.
- `app = Calculadora(janela)` cria uma instância da classe `Calculadora`, passando a janela principal como argumento.
- `janela.mainloop()` inicia o loop de eventos, mantendo a interface gráfica aberta e aguardando a interação do usuário.

### Resumo

- O código cria uma calculadora simples com uma interface gráfica.
- O usuário insere dois números, escolhe uma operação (soma, subtração, multiplicação ou divisão) e clica em "Calcular".
- O resultado da operação é exibido na janela. Se o usuário inserir dados inválidos ou tentar dividir por zero, uma mensagem de erro será exibida.
</details>

## Exercício 2

<details>
<summary>Explicação</summary>
Esse código cria uma aplicação simples de **Jogo da Adivinhação** usando o módulo `tkinter` para a interface gráfica em Python. Vou explicar o funcionamento do código detalhadamente, dividindo-o em partes.

### 1. **Importações e Definição da Classe**

```python
import tkinter as tk
from tkinter import ttk
import random
```

- `tkinter`: Módulo de interface gráfica do usuário (GUI) em Python.
- `ttk`: Submódulo do `tkinter` que fornece widgets com uma aparência mais moderna e estilizada.
- `random`: Módulo usado para gerar números aleatórios.

```python
class JogoAdivinhacao:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Jogo da Adivinhação")
```

Aqui, é definida uma classe `JogoAdivinhacao`, que irá controlar a lógica do jogo e a interface gráfica. O método `__init__` é o construtor da classe, chamado quando a classe é instanciada. Ele recebe um argumento `janela`, que é a janela principal da interface.

Dentro do método `__init__`:
- A janela recebe o título "Jogo da Adivinhação".
- A variável `self.numero` é criada e recebe um número aleatório entre 1 e 100, que o jogador tentará adivinhar.

### 2. **Construção da Interface Gráfica**

```python
# Número aleatório
ttk.Label(janela, text="Tente adivinhar o número (1-100):").grid(row=0, column=0, columnspan=2, pady=5)
self.entrada = ttk.Entry(janela)
self.entrada.grid(row=1, column=0, padx=5, pady=5)
```

- Um **rótulo** (`Label`) é criado para mostrar o texto que orienta o jogador: "Tente adivinhar o número (1-100)".
  - O `grid` é usado para posicionar o widget na interface. Ele posiciona o rótulo na linha 0 e na coluna 0, e o `columnspan=2` faz com que ocupe duas colunas.
  - `pady=5` adiciona um pequeno espaçamento vertical.

- Uma **caixa de entrada** (`Entry`) é criada onde o jogador pode digitar seu palpite. O `grid` posiciona a entrada na linha 1, coluna 0, com espaçamento horizontal de 5 (`padx=5`) e vertical de 5 (`pady=5`).

```python
# Botão para enviar
self.botao_tentar = ttk.Button(janela, text="Tentar", command=self.tentar)
self.botao_tentar.grid(row=1, column=1, padx=5, pady=5)
```

- Um **botão** (`Button`) é criado com o texto "Tentar". O parâmetro `command=self.tentar` especifica que o método `tentar` será chamado quando o botão for pressionado. 
- O botão é posicionado ao lado da caixa de entrada na linha 1, coluna 1.

```python
# Mensagem de feedback
self.mensagem = ttk.Label(janela, text="")
self.mensagem.grid(row=2, column=0, columnspan=2, pady=5)
```

- Outro **rótulo** (`Label`) é criado para exibir mensagens de feedback, como "Mais alto!", "Mais baixo!" ou "Acertou!". Inicialmente, o texto está vazio.
- Esse rótulo é posicionado abaixo da caixa de entrada e do botão.

### 3. **Método `tentar` (A Lógica do Jogo)**

```python
def tentar(self):
    try:
        tentativa = int(self.entrada.get())
        if tentativa < self.numero:
            self.mensagem.config(text="Mais alto!")
        elif tentativa > self.numero:
            self.mensagem.config(text="Mais baixo!")
        else:
            self.mensagem.config(text="Acertou! Reiniciando...")
            self.numero = random.randint(1, 100)
    except ValueError:
        self.mensagem.config(text="Erro: Insira um número válido")
```

O método `tentar` é chamado sempre que o jogador clica no botão "Tentar". Ele realiza as seguintes ações:

1. **Captura o valor da entrada**:
   - `self.entrada.get()` obtém o valor digitado pelo jogador na caixa de entrada.
   - O valor é convertido para um número inteiro usando `int()`. Caso o valor não seja um número válido, um erro `ValueError` será gerado, e uma mensagem de erro será exibida.

2. **Compara a tentativa com o número aleatório**:
   - Se a tentativa for **menor** que o número sorteado, a mensagem "Mais alto!" será exibida, sugerindo ao jogador que tente um número maior.
   - Se a tentativa for **maior** que o número sorteado, a mensagem "Mais baixo!" será exibida, sugerindo ao jogador que tente um número menor.
   - Se o jogador acertar o número, a mensagem "Acertou! Reiniciando..." será exibida, e um novo número aleatório será gerado.

3. **Tratamento de erro**:
   - Se o jogador não digitar um número válido (por exemplo, texto ou caracteres não numéricos), um erro será exibido com a mensagem "Erro: Insira um número válido".

### 4. **Execução do Programa**

```python
if __name__ == "__main__":
    janela = tk.Tk()
    app = JogoAdivinhacao(janela)
    janela.mainloop()
```

- `if __name__ == "__main__":` garante que o código abaixo será executado apenas quando o script for rodado diretamente (não quando importado como módulo).
- `janela = tk.Tk()` cria a janela principal da interface.
- `app = JogoAdivinhacao(janela)` cria uma instância da classe `JogoAdivinhacao`, passando a janela principal como argumento.
- `janela.mainloop()` inicia o loop de eventos do `tkinter`, que mantém a interface aberta e aguarda interações do usuário.

### Resumo

- O código implementa um simples jogo da adivinhação onde o jogador deve tentar adivinhar um número entre 1 e 100.
- A interface é criada usando o `tkinter`, com um campo de entrada, um botão para enviar as tentativas e um rótulo para mostrar o feedback.
- A lógica do jogo compara o número sorteado com a tentativa do jogador e dá pistas sobre se o número deve ser maior ou menor.
- Se o jogador acertar, o número sorteado é alterado, e o jogo reinicia automaticamente.

Esse é o funcionamento básico de como o código cria e gerencia o jogo da adivinhação.
</details>

## Exercício 3

<details>
<summary>Explicação</summary>
Este código implementa um **Gerenciador de Pokémons** usando o módulo `tkinter` para criar uma interface gráfica simples. Vou explicar detalhadamente como o código funciona, parte por parte.

### 1. **Importações e Definição da Classe**

```python
import tkinter as tk
from tkinter import ttk
```

- `tkinter`: Biblioteca de interface gráfica para Python.
- `ttk`: Submódulo do `tkinter` que oferece widgets com uma aparência mais moderna e estilizada, como a `Treeview` (para listas), `Button` e `Label`.

```python
class GerenciadorPokemons:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Gerenciador de Pokémons")
```

- A classe `GerenciadorPokemons` é responsável por controlar a interface gráfica e a lógica do programa. 
- O método `__init__` é o construtor da classe, chamado quando uma instância da classe é criada. Ele recebe o parâmetro `janela`, que é a janela principal da interface gráfica.
- Dentro do `__init__`, o título da janela é configurado para "Gerenciador de Pokémons".

### 2. **Construção da Interface Gráfica**

#### Campos de Entrada

```python
# Entradas
ttk.Label(janela, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
self.nome = ttk.Entry(janela)
self.nome.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(janela, text="Tipo:").grid(row=1, column=0, padx=5, pady=5)
self.tipo = ttk.Entry(janela)
self.tipo.grid(row=1, column=1, padx=5, pady=5)
```

- São criados **rótulos** (`Label`) para os campos "Nome" e "Tipo", com **campos de entrada** (`Entry`) ao lado de cada um.
  - O campo `self.nome` permite ao usuário digitar o nome do Pokémon.
  - O campo `self.tipo` permite ao usuário digitar o tipo do Pokémon (por exemplo, "Fogo", "Água", etc.).
- Os widgets são posicionados na janela usando o método `grid()`. O `padx` e `pady` adicionam um espaçamento horizontal e vertical de 5 pixels entre os elementos.

#### Botões de Ação

```python
# Botões
self.botao_adicionar = ttk.Button(janela, text="Adicionar", command=self.adicionar_pokemon)
self.botao_adicionar.grid(row=2, column=0, padx=5, pady=5)

self.botao_remover = ttk.Button(janela, text="Remover", command=self.remover_pokemon)
self.botao_remover.grid(row=2, column=1, padx=5, pady=5)
```

- São criados dois **botões** (`Button`): "Adicionar" e "Remover".
  - O botão "Adicionar" chama o método `adicionar_pokemon` quando pressionado.
  - O botão "Remover" chama o método `remover_pokemon` quando pressionado.
- Os botões são posicionados na segunda linha da janela, nas colunas 0 e 1, respectivamente.

#### Lista de Pokémons

```python
# Lista de Pokémons
self.lista = ttk.Treeview(janela, columns=("Nome", "Tipo"), show="headings")
self.lista.heading("Nome", text="Nome")
self.lista.heading("Tipo", text="Tipo")
self.lista.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
```

- Um **widget `Treeview`** é criado para exibir a lista de Pokémons registrados. O `Treeview` é um widget de tabela que pode exibir dados em formato de linhas e colunas.
  - `columns=("Nome", "Tipo")`: Define duas colunas: uma para o nome e outra para o tipo do Pokémon.
  - `show="headings"`: Exibe apenas os cabeçalhos das colunas, sem a coluna adicional de índice.
  - As colunas são nomeadas "Nome" e "Tipo" usando o método `heading()`.
  - O `Treeview` é posicionado na linha 3 da janela, com `columnspan=2`, o que faz com que ocupe duas colunas.

### 3. **Métodos de Ação**

#### Método `adicionar_pokemon`

```python
def adicionar_pokemon(self):
    nome = self.nome.get().strip()
    tipo = self.tipo.get().strip()
    if nome and tipo:
        self.lista.insert("", "end", values=(nome, tipo))
        self.nome.delete(0, tk.END)
        self.tipo.delete(0, tk.END)
```

- O método `adicionar_pokemon` é chamado quando o botão "Adicionar" é pressionado. Ele realiza as seguintes etapas:
  1. **Obter os valores**:
     - `nome = self.nome.get().strip()`: Obtém o texto inserido no campo "Nome" e remove espaços extras no início e no final da string.
     - `tipo = self.tipo.get().strip()`: Obtém o texto inserido no campo "Tipo" e remove espaços extras.
  2. **Verificação**:
     - Se ambos os campos (`nome` e `tipo`) não estiverem vazios, o Pokémon é adicionado à lista. Caso contrário, nada acontece.
  3. **Inserção na lista**:
     - `self.lista.insert("", "end", values=(nome, tipo))`: Insere um novo item na lista do `Treeview`. O item é adicionado no final da lista (`"end"`), e os valores (nome e tipo) são passados para as colunas da lista.
  4. **Limpar os campos de entrada**:
     - Após a inserção, os campos de entrada são limpos usando `self.nome.delete(0, tk.END)` e `self.tipo.delete(0, tk.END)`.

#### Método `remover_pokemon`

```python
def remover_pokemon(self):
    for item in self.lista.selection():
        self.lista.delete(item)
```

- O método `remover_pokemon` é chamado quando o botão "Remover" é pressionado. Ele realiza as seguintes etapas:
  1. **Selecionar o Pokémon**:
     - `self.lista.selection()` retorna a lista de itens selecionados no `Treeview`.
  2. **Remover o item selecionado**:
     - Para cada item selecionado, o método `self.lista.delete(item)` remove o item da lista.

### 4. **Execução do Programa**

```python
if __name__ == "__main__":
    janela = tk.Tk()
    app = GerenciadorPokemons(janela)
    janela.mainloop()
```

- A linha `if __name__ == "__main__":` garante que o código dentro dela só será executado quando o script for rodado diretamente (não quando for importado como módulo).
- `janela = tk.Tk()` cria a janela principal.
- `app = GerenciadorPokemons(janela)` cria uma instância da classe `GerenciadorPokemons`, passando a janela principal como argumento.
- `janela.mainloop()` inicia o loop de eventos da interface gráfica, mantendo a janela aberta e interativa.

### Resumo

- Este código cria uma interface gráfica para gerenciar uma lista de Pokémons, onde o usuário pode adicionar e remover Pokémons com base em seu nome e tipo.
- A interface consiste em campos de entrada para o nome e tipo do Pokémon, dois botões ("Adicionar" e "Remover") e uma lista (`Treeview`) para exibir os Pokémons registrados.
- O método `adicionar_pokemon` insere um novo Pokémon na lista, e o método `remover_pokemon` exclui os Pokémons selecionados da lista.
</details>