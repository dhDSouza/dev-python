# Widgets Avançados e Personalização no Tkinter

Nesta aula, abordaremos widgets mais avançados disponíveis no **Tkinter**, além de explorar formas de personalizar a aparência da interface e tornar suas aplicações mais interativas e dinâmicas.

---

## Widgets Avançados

O **Tkinter** oferece diversos widgets que permitem criar interfaces robustas e funcionais. Vamos explorar os principais:

### 1. **Checkbutton**

O widget **Checkbutton** é usado para selecionar ou desmarcar opções, ideal para configurações ou filtros.

**Exemplo:**

```python
import tkinter as tk

def mostrar_selecao():
    texto = "Opção selecionada!" if var_opcao.get() else "Nenhuma opção selecionada!"
    label_resultado.config(text=texto)

janela = tk.Tk()
janela.title("Exemplo de Checkbutton")

var_opcao = tk.BooleanVar()  # Variável que armazena o estado (True/False)
checkbutton = tk.Checkbutton(janela, text="Selecionar opção", variable=var_opcao, command=mostrar_selecao)
checkbutton.pack()

label_resultado = tk.Label(janela, text="")
label_resultado.pack()

janela.mainloop()
```

---

### 2. **Radiobutton**

O **Radiobutton** permite selecionar uma única opção entre várias disponíveis.

**Exemplo:**

```python
import tkinter as tk

def mostrar_escolha():
    label_resultado.config(text=f"Você escolheu: {var_opcao.get()}")

janela = tk.Tk()
janela.title("Exemplo de Radiobutton")

var_opcao = tk.StringVar(value="Nenhuma")  # Variável que armazena a opção selecionada

tk.Radiobutton(janela, text="Opção 1", variable=var_opcao, value="Opção 1", command=mostrar_escolha).pack()
tk.Radiobutton(janela, text="Opção 2", variable=var_opcao, value="Opção 2", command=mostrar_escolha).pack()
tk.Radiobutton(janela, text="Opção 3", variable=var_opcao, value="Opção 3", command=mostrar_escolha).pack()

label_resultado = tk.Label(janela, text="Nenhuma opção selecionada")
label_resultado.pack()

janela.mainloop()
```

---

### 3. **Combobox**

A **Combobox** (fornecida pelo módulo `ttk`) é uma lista suspensa que permite selecionar uma opção.

**Exemplo:**

```python
import tkinter as tk
from tkinter import ttk

def mostrar_selecao(event):
    label_resultado.config(text=f"Você escolheu: {combobox.get()}")

janela = tk.Tk()
janela.title("Exemplo de Combobox")

opcoes = ["Opção 1", "Opção 2", "Opção 3"]
combobox = ttk.Combobox(janela, values=opcoes, state="readonly")
combobox.bind("<<ComboboxSelected>>", mostrar_selecao)
combobox.pack()

label_resultado = tk.Label(janela, text="Nenhuma opção selecionada")
label_resultado.pack()

janela.mainloop()
```

---

### 4. **Spinbox**

O **Spinbox** é usado para selecionar valores em um intervalo predefinido.

**Exemplo:**

```python
import tkinter as tk

def mostrar_valor():
    label_resultado.config(text=f"Valor selecionado: {spinbox.get()}")

janela = tk.Tk()
janela.title("Exemplo de Spinbox")

spinbox = tk.Spinbox(janela, from_=0, to=10, command=mostrar_valor)
spinbox.pack()

label_resultado = tk.Label(janela, text="Valor selecionado: 0")
label_resultado.pack()

janela.mainloop()
```

---

### 5. **Scrollbar**

A **Scrollbar** é usada para adicionar barras de rolagem a widgets como *Text* ou listas.

**Exemplo:**

```python
import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo de Scrollbar")

text_box = tk.Text(janela, height=10, width=40)
scrollbar = tk.Scrollbar(janela, command=text_box.yview)
text_box.configure(yscrollcommand=scrollbar.set)

text_box.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

janela.mainloop()
```

---

## Personalização de Estilo

O **Tkinter** permite customizar a aparência dos widgets, alterando cores, fontes e tamanhos.

### Alterando cores

Podemos personalizar a cor de fundo (*background*) e a cor do texto (*foreground*) de muitos widgets.

**Exemplo:**

```python
import tkinter as tk

janela = tk.Tk()
janela.title("Personalização de Cores")

label = tk.Label(janela, text="Texto colorido!", bg="black", fg="white", font=("Arial", 16))
label.pack(pady=10)

janela.mainloop()
```

---

### Alterando fontes

Podemos definir o tipo de fonte, tamanho e estilo.

**Exemplo:**

```python
import tkinter as tk

janela = tk.Tk()
janela.title("Personalização de Fontes")

label = tk.Label(janela, text="Fonte Personalizada", font=("Courier", 18, "bold"))
label.pack(pady=10)

janela.mainloop()
```

---

### Temas com `ttk`

O módulo **ttk** traz widgets estilizados e permite aplicar temas modernos à aplicação.

**Exemplo:**

```python
import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Uso de Temas")

style = ttk.Style()
style.theme_use("clam")  # Alterar para outros temas: 'default', 'alt', 'classic', etc.

botao = ttk.Button(janela, text="Botão Estilizado")
botao.pack(pady=20)

janela.mainloop()
```

---

## Exercícios

1. **Preferências do Usuário**
   Crie uma interface que pergunte ao usuário:
   - Se deseja receber notificações (*Checkbutton*).
   - O método preferido de contato (*Radiobutton*: E-mail ou Telefone).
   - Um horário preferido (*Combobox*).

2. **Gerenciador de Tarefas**
   Desenvolva uma aplicação com:
   - Um campo de texto (*Text*) para adicionar tarefas.
   - Um botão para salvar a tarefa em uma lista.
   - Uma barra de rolagem para navegar pelas tarefas salvas.

3. **Personalização Avançada**
   Crie uma janela com:
   - Um tema escolhido no `ttk`.
   - Um botão estilizado com uma fonte específica.
   - Um texto colorido exibindo o tema aplicado.
