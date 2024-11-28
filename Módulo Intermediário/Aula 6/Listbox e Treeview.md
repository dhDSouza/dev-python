# Tutorial: Usando Listbox e Treeview no Tkinter

Este tutorial cobre os widgets **Listbox** e **Treeview** do Tkinter, explicando seus atributos, funções embutidas e fornecendo exemplos práticos.

---

## **Listbox**  
O widget **Listbox** permite exibir uma lista de itens para o usuário, onde é possível selecionar um ou mais itens.

### Criando um Listbox Básico

```python
import tkinter as tk

root = tk.Tk()
root.title("Exemplo de Listbox")

# Criando o Listbox
listbox = tk.Listbox(root, height=6, selectmode=tk.SINGLE)  # SINGLE, BROWSE, MULTIPLE ou EXTENDED
listbox.pack(padx=10, pady=10)

# Adicionando itens
itens = ["Python", "Java", "C++", "JavaScript", "Go", "Ruby"]
for item in itens:
    listbox.insert(tk.END, item)

# Função para capturar a seleção
def mostrar_selecionado():
    selecionado = listbox.get(listbox.curselection())
    print(f"Você selecionou: {selecionado}")

botao = tk.Button(root, text="Mostrar Seleção", command=mostrar_selecionado)
botao.pack(pady=10)

root.mainloop()
```

### Atributos Comuns
| Atributo          | Descrição                                                                 |
|--------------------|-------------------------------------------------------------------------|
| `height`          | Número de linhas visíveis no widget.                                   |
| `width`           | Número de caracteres visíveis por linha.                               |
| `selectmode`      | Define o modo de seleção: SINGLE, BROWSE, MULTIPLE ou EXTENDED.        |
| `bg`, `fg`        | Cor de fundo e do texto, respectivamente.                             |

### Métodos Úteis
| Método                     | Descrição                                                                 |
|----------------------------|-------------------------------------------------------------------------|
| `insert(index, item)`      | Insere um item no índice especificado.                                  |
| `delete(start, end=None)`  | Remove itens de `start` até `end` (ou apenas `start`).                 |
| `get(start, end=None)`     | Retorna o item ou itens no intervalo especificado.                     |
| `curselection()`           | Retorna o índice do(s) item(ns) selecionado(s).                        |
| `size()`                   | Retorna o número total de itens.                                       |

---

## **Treeview**

O widget **Treeview** é mais avançado, permitindo exibir dados em formato de árvore ou tabela.

### Criando um Treeview Básico

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Exemplo de Treeview")

# Criando o Treeview
tree = ttk.Treeview(root, columns=("Nome", "Idade"), show="headings", height=5)
tree.pack(padx=10, pady=10)

# Configurando colunas
tree.heading("Nome", text="Nome")
tree.heading("Idade", text="Idade")
tree.column("Nome", width=150, anchor=tk.CENTER)
tree.column("Idade", width=100, anchor=tk.CENTER)

# Adicionando dados
dados = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
for nome, idade in dados:
    tree.insert("", tk.END, values=(nome, idade))

# Função para capturar a seleção
def mostrar_selecionado():
    item = tree.selection()[0]
    valores = tree.item(item, "values")
    print(f"Você selecionou: {valores}")

botao = tk.Button(root, text="Mostrar Seleção", command=mostrar_selecionado)
botao.pack(pady=10)

root.mainloop()
```

### Atributos Comuns
| Atributo      | Descrição                                                                 |
|---------------|-------------------------------------------------------------------------|
| `columns`     | Define as colunas adicionais.                                          |
| `show`        | Define quais elementos mostrar: `"tree"` (apenas árvore), `"headings"`.|
| `height`      | Define a quantidade de linhas visíveis.                                |

### Métodos Úteis
| Método                     | Descrição                                                                 |
|----------------------------|-------------------------------------------------------------------------|
| `insert(parent, index, iid=None, values=())` | Insere um novo item.                                |
| `delete(item)`             | Remove o item especificado.                                            |
| `item(item, option)`       | Obtém ou define informações do item (ex.: valores).                    |
| `selection()`              | Retorna os IDs dos itens selecionados.                                |

---

>[!TIP]
>O <code>Treeview</code> é ótimo para exibir tabelas com múltiplas colunas, enquanto o <code>Listbox</code> é mais adequado para listas simples.

>[!NOTE]
>Por padrão, o <code>Treeview</code> não tem barra de rolagem. Você deve adicionar manualmente uma usando <code>ttk.Scrollbar</code>.

>[!WARNING]
>Evite manipular diretamente os dados de um widget enquanto o programa estiver em execução. Sempre atualize dinamicamente usando métodos como <code>insert</code> ou <code>delete</code>.
