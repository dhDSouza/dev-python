# Orientação a Objetos com Tkinter

Usar OO *(Orientação a Objetos)* nos ajuda a organizar o código, especialmente em aplicativos maiores.

**Exemplo de Tkinter com OO:**

```python
import tkinter as tk
from tkinter import ttk

class Aplicacao:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Minha GUI com Classe")
        
        # Adicionando widgets
        self.botao = ttk.Button(self.janela, text="Clique aqui!", command=self.dizer_ola)
        self.botao.pack()

    def dizer_ola(self):
        print("Olá! Você clicou no botão.")

# Criando a aplicação
if __name__ == "__main__":
    janela = tk.Tk()
    app = Aplicacao(janela)
    janela.mainloop()
```

**Explicação:**

1. Criamos uma classe chamada **`Aplicacao`**.
2. **`__init__`** inicializa a interface, adicionando widgets.
3. O método **`dizer_ola`** é executado quando o botão é clicado.
4. Criamos a janela principal (`janela`) e passamos para a classe.

## Adicionando Widgets e Layout

Vamos adicionar mais widgets (como caixas de texto, labels e botões) e organizar a interface com **Grid**.

**Um simples formulário de login:**

```python
import tkinter as tk
from tkinter import ttk

class LoginApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Login")

        # Labels
        ttk.Label(janela, text="Usuário:").grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(janela, text="Senha:").grid(row=1, column=0, padx=10, pady=10)

        # Entradas
        self.entrada_usuario = ttk.Entry(janela)
        self.entrada_usuario.grid(row=0, column=1, padx=10, pady=10)

        self.entrada_senha = ttk.Entry(janela, show="*")
        self.entrada_senha.grid(row=1, column=1, padx=10, pady=10)

        # Botão
        self.botao_login = ttk.Button(janela, text="Entrar", command=self.fazer_login)
        self.botao_login.grid(row=2, column=0, columnspan=2, pady=10)

    def fazer_login(self):
        usuario = self.entrada_usuario.get()
        senha = self.entrada_senha.get()

        if usuario == "admin" and senha == "123":
            print("Login bem-sucedido!")
        else:
            print("Usuário ou senha incorretos.")

if __name__ == "__main__":
    janela = tk.Tk()
    app = LoginApp(janela)
    janela.mainloop()
```

## Exercícios

### **1. Criando uma Calculadora Básica**

**Descrição:**

Crie uma calculadora gráfica que permita:

- Inserir dois números.
- Escolher uma operação (soma, subtração, multiplicação, divisão).
- Exibir o resultado.

>[!TIP]
>
>Use <code>ttk.Combobox</code> para selecionar a operação.
>Mostre o resultado em um <code>ttk.Label</code>.

### **2. Jogo da Adivinhação**

**Descrição:**

Crie um pequeno jogo onde:

- O programa escolhe um número aleatório.
- O usuário tenta adivinhar o número.
- Mostre mensagens de "Mais alto", "Mais baixo" ou "Acertou!".

>[!TIP]
>
>Use o método <code>random.randint()</code> para gerar o número.
>Adicione entradas de texto para as tentativas e mensagens com <code>ttk.Label</code>.

### **Gerenciador de Pokémons**

**Descrição:**

Crie um aplicativo onde o usuário possa:

- Adicionar Pokémons (nome e tipo).
- Exibir uma lista dos Pokémons cadastrados.
- Remover Pokémons da lista.

>[!TIP]
>
>Use listas para armazenar os dados.
>Exiba os Pokémons em um <code>ttk.Treeview</code> (uma tabela).
