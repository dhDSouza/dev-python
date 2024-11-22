# Funções de Alinhamento e Manipulação de Dados no Tkinter

Na aula anterior, vimos como criar uma interface gráfica simples com **Tkinter**, incluindo como adicionar elementos básicos como *Labels* e *Buttons*. Agora, vamos explorar conceitos mais avançados e práticos para tornar nossas aplicações mais dinâmicas:

- **Funções de alinhamento**: organizar os elementos na janela de forma clara e intuitiva.

- **Interação com o usuário**: coletar e utilizar informações inseridas nos widgets como *Entry* e *Text*.

- **Criação de novos frames**: dividir a interface em seções para melhorar a organização.

---

## 1. **Funções de Alinhamento**

`Tkinter` oferece três métodos principais para posicionar elementos:

1. **Pack**: Organiza widgets em sequência (vertical ou horizontal).
2. **Grid**: Posiciona widgets em um sistema de linhas e colunas, como em uma tabela.
3. **Place**: Permite posicionar widgets usando coordenadas exatas.

---

### **Exemplo com Pack**

O método `pack` organiza widgets de forma sequencial e é fácil de usar.

```python
import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo Pack")

# Widgets
label1 = tk.Label(janela, text="Topo", bg="red", height=2)
label1.pack(side="top", fill="x")  # Atributos de alinhamento

label2 = tk.Label(janela, text="Esquerda", bg="blue", width=15)
label2.pack(side="left", fill="y")

label3 = tk.Label(janela, text="Direita", bg="green", width=15)
label3.pack(side="right", fill="y")

label4 = tk.Label(janela, text="Base", bg="yellow", height=2)
label4.pack(side="bottom", fill="x")

janela.mainloop()
```

<details>
<summary>Explicação dos atributos usados</summary>

- **`side`**: Define a posição do widget no contêiner (`"top"`, `"bottom"`, `"left"`, `"right"`).
- **`fill`**: Faz o widget expandir horizontalmente (`"x"`), verticalmente (`"y"`) ou ambos (`"both"`).
- **`height` e `width`**: Controlam a altura e largura do widget em unidades de linhas e caracteres, respectivamente.
</details>

---

### **Exemplo com Grid**

O método `grid` organiza widgets como células de uma tabela.

```python
import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo Grid")

# Widgets
label_nome = tk.Label(janela, text="Nome:")
label_nome.grid(row=0, column=0)

entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

label_email = tk.Label(janela, text="E-mail:")
label_email.grid(row=1, column=0)

entry_email = tk.Entry(janela)
entry_email.grid(row=1, column=1)

botao = tk.Button(janela, text="Enviar")
botao.grid(row=2, column=0, columnspan=2)

janela.mainloop()
```

<details>
<summary>Explicação dos atributos usados</summary>

- **`row`** e **`column`**: Especificam a linha e a coluna onde o widget será posicionado.
- **`columnspan`**: Permite que o widget ocupe várias colunas.
- **`rowspan`**: (não usado aqui) Faz o widget ocupar várias linhas.
</details>

---

### **Exemplo com Place**

O método `place` permite posicionar widgets usando coordenadas exatas.

```python
import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo Place")

# Widgets
label = tk.Label(janela, text="Texto Posicionado", bg="orange", width=20)
label.place(x=50, y=50)

botao = tk.Button(janela, text="Clique Aqui")
botao.place(x=100, y=100)

janela.geometry("300x200")
janela.mainloop()
```

<details>
<summary>Explicação dos atributos usados</summary>

- **`x`** e **`y`**: Especificam as coordenadas horizontais e verticais do widget, a partir do canto superior esquerdo da janela.
</details>

---

## 2. **Pegando Dados de Entry e Text**

Os widgets *Entry* e *Text* são usados para coletar dados do usuário.

### **Exemplo com Entry**

```python
import tkinter as tk

def mostrar_nome():
    nome = entry_nome.get()
    label_resultado.config(text=f"Olá, {nome}!")

janela = tk.Tk()
janela.title("Entrada de Nome")

# Widgets
label_nome = tk.Label(janela, text="Digite seu nome:")
label_nome.pack()

entry_nome = tk.Entry(janela)
entry_nome.pack()

botao = tk.Button(janela, text="Enviar", command=mostrar_nome)
botao.pack()

label_resultado = tk.Label(janela, text="")
label_resultado.pack()

janela.mainloop()
```

<details>
<summary>Explicação de `get`</summary>

- **`get`**: Recupera o valor digitado no widget *Entry*.
</details>

---

### **Exemplo com Text**

```python
import tkinter as tk

def mostrar_texto():
    texto = text_box.get("1.0", tk.END)  # Lê do início até o fim
    label_resultado.config(text=f"Texto inserido:\n{texto.strip()}")

janela = tk.Tk()
janela.title("Entrada de Texto")

# Widgets
text_box = tk.Text(janela, height=5, width=40)
text_box.pack()

botao = tk.Button(janela, text="Exibir Texto", command=mostrar_texto)
botao.pack()

label_resultado = tk.Label(janela, text="")
label_resultado.pack()

janela.mainloop()
```

<details>
<summary>Explicação de `get`</summary>

- **`get(start, end)`**: Retorna o texto entre o índice inicial (`start`) e final (`end`).
  - `start` pode ser `"1.0"` para a primeira linha e primeira coluna.
  - `end` pode ser `tk.END` para capturar até o final do texto.
</details>

---

## 3. **Dividindo a Interface com Frames**

Os *Frames* ajudam a organizar widgets em seções.

### **Exemplo com Frames**

```python
import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo com Frames")

# Frame superior
frame_topo = tk.Frame(janela, bg="lightblue", height=100)
frame_topo.pack(fill="x")

label_topo = tk.Label(frame_topo, text="Frame Superior", bg="lightblue")
label_topo.pack()

# Frame inferior
frame_inferior = tk.Frame(janela, bg="lightgreen", height=100)
frame_inferior.pack(fill="x")

label_inferior = tk.Label(frame_inferior, text="Frame Inferior", bg="lightgreen")
label_inferior.pack()

janela.geometry("300x200")
janela.mainloop()
```

<details>
<summary>Explicação do Frame</summary>

- **Frame**: Contêiner usado para agrupar outros widgets e organizar a interface.
- **`pack`, `grid` ou `place`**: Podem ser usados dentro do frame para organizar widgets adicionais.
</details>

---

## Exercícios

1. **Contador de Cliques**

   Crie uma aplicação com um botão que, a cada clique, incrementa e exibe um contador em um rótulo.

2. **Desafio de Alinhamento**:

   Crie uma janela com três botões:
   - Um alinhado ao topo.
   - Um alinhado à esquerda.
   - Um alinhado à direita.

3. **Desafio de Captura de Dados**:

   Crie um formulário que peça:
   - Nome (*Entry*).
   - Comentários (*Text*).
   - Ao clicar em um botão, exiba as informações capturadas em um *Label*.

4. **Desafio com Frames**:

   Divida a janela em três seções:
   - Topo (contendo um título).
   - Meio (formulário com *Entry* e *Text*).
   - Base (botões para limpar e enviar os dados).

5. **Aplicação de Login**  

   Desenvolva uma interface simples com:
   - Dois campos de entrada: um para "Usuário" e outro para "Senha".
   - Um botão "Login".
   - Ao clicar no botão, exiba uma mensagem no console dizendo "Login bem-sucedido!" ou "Login falhou!", dependendo se os dados digitados são iguais aos valores pré-definidos no código.
