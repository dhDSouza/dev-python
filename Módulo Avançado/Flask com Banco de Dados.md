# 🌟 **Aula sobre Flask, Banco de Dados e SQLite**

Nessa aula, vamos explorar um código Flask que implementa um simples sistema de "to-do list" (lista de tarefas) com funcionalidades como criar, listar, concluir e excluir tarefas. Vamos focar especialmente no uso de banco de dados SQLite, já que seus alunos têm experiência com Flask e Python, mas ainda não têm conhecimento sobre banco de dados.

**🧑‍💻 Visão Geral do Código**

Esse código é um exemplo de aplicação web em Flask que se conecta a um banco de dados SQLite. O banco de dados armazena informações sobre tarefas, e o Flask permite que os usuários interajam com essas tarefas por meio de uma interface web. As principais funcionalidades são:

- **📋 Visualizar tarefas**
- **➕ Adicionar uma nova tarefa**
- **✔️ Marcar uma tarefa como concluída**
- **❌ Excluir uma tarefa**

Agora, vamos detalhar cada parte do código, com foco no banco de dados, e explicar como ele funciona.

## **1. 📥 Importação de Bibliotecas**

```python
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
```

- **Flask**: Framework que estamos usando para criar a aplicação web.
- **render_template**: Função usada para renderizar os arquivos HTML.
- **request**: Usada para pegar dados do usuário via formulários.
- **redirect**: Redireciona o usuário para outra página.
- **url_for**: Gera URLs para outras rotas.
- **sqlite3**: Biblioteca que permite a conexão e interação com o banco de dados SQLite.

## **2. 🏗️ Função `init_db()` — Criando o Banco de Dados**

```python
def init_db():
    conn = sqlite3.connect("todo.db")  # Cria o arquivo do banco se não existir
    cursor = conn.cursor()

    # Criando a tabela 'tasks'
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            done BOOLEAN NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()
```

Aqui, temos a função `init_db()`, que é responsável por criar o banco de dados e a tabela de tarefas.

### **Explicação detalhada do banco de dados:**

1. **`sqlite3.connect("todo.db")`**:
   - Abre uma conexão com o banco de dados SQLite chamado `todo.db`. Se o arquivo não existir, ele será criado automaticamente.
   
2. **`conn.cursor()`**:
   - Cria um "cursor" que é usado para executar comandos SQL no banco de dados.

3. **`CREATE TABLE IF NOT EXISTS tasks (...)`**:
   - Aqui estamos criando a tabela `tasks` caso ela não exista. A tabela terá:
     - **id**: Um identificador único para cada tarefa. O tipo `INTEGER PRIMARY KEY AUTOINCREMENT` significa que o valor dessa coluna será gerado automaticamente e será único.
     - **title**: O título da tarefa, que não pode ser nulo (`NOT NULL`).
     - **description**: A descrição da tarefa, que pode ser nula.
     - **done**: Indica se a tarefa foi concluída ou não. É um valor booleano, onde `0` significa "não concluída" e `1` significa "concluída". O valor padrão é `0`.

4. **`conn.commit()`**:
   - Finaliza a transação no banco de dados e garante que as mudanças (neste caso, a criação da tabela) sejam salvas.

5. **`conn.close()`**:
   - Fecha a conexão com o banco de dados.

## **3. 🔌 Função `get_db_connection()` — Conectando-se ao Banco de Dados**

```python
def get_db_connection():
    conn = sqlite3.connect("todo.db")
    conn.row_factory = sqlite3.Row  # Permite acessar as colunas como dicionários
    return conn
```

Essa função é chamada para obter uma conexão com o banco de dados. O que é importante aqui:

- **`conn.row_factory = sqlite3.Row`**: 
  - Isso configura a conexão para que as consultas retornem os resultados como objetos tipo `Row`. Isso permite acessar as colunas da tabela como se fossem chaves de um dicionário (por exemplo, `row['title']` ao invés de acessar pela posição da coluna).

## **4. 📝 Rota Principal: Listando as Tarefas**

```python
@app.route("/")
def index():
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)
```

- **`@app.route("/")`**: Define a rota principal da aplicação, que será acessada ao visitar o endereço raiz (`/`).
- **`conn.execute("SELECT * FROM tasks").fetchall()`**: 
  - Executa uma consulta SQL para selecionar todas as tarefas da tabela `tasks`.
  - O método `fetchall()` retorna todas as linhas da tabela.
- **`render_template("index.html", tasks=tasks)`**:
  - Renderiza o arquivo `index.html`, passando as tarefas recuperadas para o template. O `tasks` será um objeto que contém todas as tarefas retornadas pelo banco de dados.

## **5. ➕ Rota para Adicionar uma Nova Tarefa**

```python
@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]

        conn = get_db_connection()
        conn.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (title, description))
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    return render_template("add_task.html")
```

- **`@app.route("/add", methods=["GET", "POST"])`**: Define uma rota que lida tanto com requisições GET (para mostrar o formulário) quanto POST (para processar o envio do formulário).
- **`request.form["title"]` e `request.form["description"]`**:
  - Captura os dados enviados no formulário (título e descrição da tarefa).
- **`conn.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (title, description))`**:
  - Insere uma nova tarefa na tabela `tasks`, usando os valores de `title` e `description`. O `?` é um marcador de posição para evitar SQL Injection (uma prática de segurança importante).
- **`conn.commit()`**: Confirma a transação de inserção no banco de dados.
- **`redirect(url_for("index"))`**: Redireciona o usuário para a página inicial, onde as tarefas serão exibidas.

## **6. ✅ Rota para Concluir uma Tarefa**

```python
@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    conn = get_db_connection()
    conn.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))
```

- **`@app.route("/complete/<int:task_id>")`**: Define uma rota dinâmica onde `<int:task_id>` captura o ID da tarefa a ser marcada como concluída.
- **`conn.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))`**:
  - Atualiza a coluna `done` da tarefa com o `id` correspondente, definindo-a como `1` (concluída).
- **`conn.commit()`**: Confirma a atualização no banco de dados.

## **7. 🗑️ Rota para Deletar uma Tarefa**

```python
@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))
```

- **`@app.route("/delete/<int:task_id>")`**: Define uma rota dinâmica para deletar uma tarefa com base no seu ID.
- **`conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))`**:
  - Executa um comando SQL para excluir a tarefa com o `id` correspondente.
- **`conn.commit()`**: Confirma a exclusão no banco de dados.

## **🎉 Conclusão**

Este código utiliza o Flask para criar uma aplicação web simples que se conecta a um banco de dados SQLite. O banco de dados armazena informações sobre tarefas e permite que os usuários realizem operações como criar, visualizar, concluir e excluir tarefas.
As principais interações com o banco de dados são feitas por meio de comandos SQL como `SELECT`, `INSERT`, `UPDATE` e `DELETE`. A biblioteca `sqlite3` é usada para fazer a conexão com o banco de dados e executar esses comandos de forma segura.
