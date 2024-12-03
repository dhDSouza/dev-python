# 🛒 Trabalho Avaliativo Prático de Python - POO + Tkinter

**📚 Tema:** Criação de um Sistema de Loja com Interface Gráfica

**🎯 Objetivo:**

Desenvolver um sistema de loja que permita cadastrar produtos, visualizar o estoque e realizar vendas. O sistema deve aplicar os conceitos de **Programação Orientada a Objetos (POO)** e usar a biblioteca **Tkinter** para criar a interface gráfica.

---

### **📄 Descrição do Trabalho**

Você irá criar um programa que simula o funcionamento básico de um sistema de gerenciamento de loja. O sistema terá as seguintes funcionalidades:

1. 🏷️ **Cadastro de produtos**.

2. 📋 **Exibição da lista de produtos cadastrados**.

3. 💸 **Realização de vendas**, com cálculo do total e atualização do estoque.

---

### **⚙️ Requisitos do Sistema**

#### **1. Estrutura do Programa (POO):**

1. **Classe Produto:**

   - **Atributos:** código, nome, preço, quantidade em estoque.  
   - **Métodos:**  
     - `__init__`: Inicializa os atributos do produto.  
     - `exibir_detalhes`: Retorna uma string com as informações do produto.  
     - `reduzir_estoque`: Reduz a quantidade de estoque após uma venda.  

2. **Classe Loja:**

   - **Atributos:** lista de produtos.  
   - **Métodos:**  
     - `adicionar_produto`: Adiciona um novo produto à lista.  
     - `exibir_produtos`: Retorna todos os produtos cadastrados.  
     - `realizar_venda`: Procura um produto pelo código e reduz o estoque.  

---

#### **2. Funcionalidades com Tkinter:**  

1. **🖥️ Janela Principal com Menu:**

   - Opções para acessar as funcionalidades do sistema (cadastrar produto, listar produtos e realizar venda).  

2. **🏷️ Cadastro de Produto:**

   - Campos para inserir nome, preço e quantidade inicial.  
   - Botão **"Cadastrar"** que adiciona o produto à loja.  

3. **📃 Exibição de Produtos:**

   - Mostra uma lista dos produtos cadastrados, incluindo código, nome, preço e quantidade disponível.  

4. **💰 Realização de Venda:**

   - Campo para inserir o código do produto e a quantidade desejada.  
   - Botão **"Realizar Venda"** que atualiza o estoque e exibe o total da compra.  
   - Exibir mensagens de erro caso:  
     - O código do produto não exista.  
     - A quantidade solicitada seja maior que o estoque disponível.

---

### **🛠️ Etapas de Desenvolvimento**

1. **📝 Configuração Inicial:**

   - Crie um arquivo Python e importe a biblioteca **Tkinter**.  
   - Estruture as classes `Produto` e `Loja`.  
   - Instancie um objeto da classe **Loja** no início do programa.

2. **💻 Interface Gráfica (Tkinter):**

   - Configure a janela principal com o menu e botões para acessar cada funcionalidade.  
   - Crie janelas secundárias para cada funcionalidade (ex.: cadastro, listagem e venda).  

3. **🏷️ Funcionalidade: Cadastro de Produtos:**

   - Use widgets como **`Entry`** para entrada de dados e **`Button`** para confirmar o cadastro.  
   - Após o cadastro, os produtos devem ser adicionados à lista da loja.  

4. **📋 Funcionalidade: Listagem de Produtos:**

   - Use um widget como **`Text`** ou **`Label`** para exibir a lista dos produtos.  
   - Mostre todos os atributos do produto.  

5. **💵 Funcionalidade: Venda de Produtos:**

   - Crie campos para entrada do código do produto e quantidade desejada.  
   - Exiba o total da venda ou mensagens de erro.  

6. **⚠️ Tratamento de Erros:**

   - Certifique-se de lidar com entradas inválidas (ex.: campos vazios, letras em campos numéricos).

---

### **📊 Critérios de Avaliação**

1. **🗂️ Estrutura de Código:**

   - Uso correto de POO (classes, métodos, atributos, encapsulamento).  
   - Organização e clareza do código.

2. **✅ Funcionalidade:**

   - Todas as funcionalidades solicitadas devem estar implementadas corretamente.  
   - O sistema deve funcionar sem erros de execução.

3. **🖼️ Interface Gráfica:**

   - A interface deve ser funcional e intuitiva.  
   - Deve permitir navegar entre as funcionalidades de forma fácil.

---

**💡 Exemplo Básico de Código Inicial:**

```python
from tkinter import Tk, Label, Entry, Button, Text, messagebox

class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_detalhes(self):
        return f"{self.codigo} - {self.nome} - R${self.preco:.2f} - {self.quantidade} unidades"

class Loja:
    def __init__(self):
        self.produtos = []
        self.proximo_codigo = 1

    def adicionar_produto(self, nome, preco, quantidade):
        produto = Produto(self.proximo_codigo, nome, preco, quantidade)
        self.produtos.append(produto)
        self.proximo_codigo += 1

    def exibir_produtos(self):
        return [produto.exibir_detalhes() for produto in self.produtos]
```

>[!WARNING]
><h3><strong>📅 Prazo de Entrega</strong></h3>
>
><p>O trabalho deve ser entregue até <em><strong>(03/11/2024)</strong></em>, em formato zipado <em><strong>(.zip)</strong></em> e enviado por e-mail.</p>
>
><p>Envie para <a href="mailto:dhs.danielsouza@gmail.com">dhs.danielsouza@gmail.com</a>.</p>
>
>Coloque no assunto <strong>Trabalho 2 Python - "nome completo"</strong>.
