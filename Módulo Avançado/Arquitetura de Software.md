# Aula sobre Arquitetura de Software em Python 🏗️

**Objetivo:** Vamos aprender sobre como organizar um projeto de desenvolvimento web com **Flask**, entender como funcionam os diferentes tipos de arquitetura e ver como aplicar isso em um projeto real. 

Neste caso, vamos focar em duas arquiteturas muito comuns no desenvolvimento web:

- **MVC (Model-View-Controller)** 
- **Arquitetura de Camadas (Models, Views, Controllers, Repositories, Services, etc.)**

---

## O que é Arquitetura de Software? 🏛️

A arquitetura de software é como você organiza as diferentes partes de um sistema de software, para que ele seja fácil de entender, modificar e manter no futuro. Imagina um prédio: o arquiteto desenha o prédio de uma maneira que todos os pedreiros e engenheiros saibam onde cada parte deve ser colocada para que o prédio fique de pé. No software, a arquitetura faz a mesma coisa.

---

## Arquitetura MVC 🖥️🏗️

O padrão **MVC (Model-View-Controller)** é uma forma muito popular de organizar o código de um sistema. Ele divide a aplicação em 3 partes principais:

1. **Model (Modelo)**: Onde ficam os dados e a lógica de como eles são manipulados.
2. **View (Visão)**: A interface com o usuário. O que ele vê e interage.
3. **Controller (Controlador)**: Recebe as ações do usuário, interage com o modelo e decide o que mostrar na visão.

### Explicação Simples:
- **Model:** É como o cérebro da aplicação. Ele conhece tudo sobre os dados, como buscar, adicionar ou alterar.
- **View:** É como o rosto da aplicação. Ela mostra para o usuário o que está acontecendo.
- **Controller:** É como o mestre de cerimônias. Ele coordena as ações entre o cérebro (Model) e o rosto (View).

### Exemplo de um simples aplicativo de notas com Flask:

Imagine que temos um aplicativo onde as pessoas podem adicionar e listar suas notas de estudo.

#### Estrutura de diretórios:

```
meu_app/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── controllers.py
│   └── database.py
├── run.py
```

#### 1. **Model (models.py)**

O **Model** vai ser responsável pela interação com o banco de dados, ou seja, vamos criar a estrutura que vai guardar e recuperar as notas.

```python
# models.py

import sqlite3

def get_db():
    conn = sqlite3.connect('app.db')
    return conn

def criar_tabela():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS notas (id INTEGER PRIMARY KEY, nota TEXT)''')
    conn.commit()

def adicionar_nota(nota):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO notas (nota) VALUES (?)', (nota,))
    conn.commit()

def listar_notas():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notas')
    return cursor.fetchall()
```

#### 2. **View (views.py)**

A **View** vai ser a responsável por mostrar para o usuário o que está acontecendo.

```python
# views.py

from flask import render_template

def mostrar_notas(notas):
    return render_template('notas.html', notas=notas)
```

Aqui, usamos um arquivo HTML (que seria o `notas.html`) para exibir as notas.

#### 3. **Controller (controllers.py)**

O **Controller** vai ser responsável por decidir o que acontece quando o usuário faz algo (exemplo: quando ele adiciona uma nova nota ou pede para listar as notas).

```python
# controllers.py

from flask import Flask, request, redirect, url_for
from models import adicionar_nota, listar_notas
from views import mostrar_notas

app = Flask(__name__)

@app.route('/')
def home():
    notas = listar_notas()
    return mostrar_notas(notas)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nota = request.form['nota']
    adicionar_nota(nota)
    return redirect(url_for('home'))
```

#### 4. **Run (run.py)**

Este arquivo vai inicializar a aplicação.

```python
# run.py

from app.controllers import app
from app.models import criar_tabela

criar_tabela()
app.run(debug=True)
```

#### 5. **notas.html**

Aqui, a **View** usa um arquivo HTML para mostrar as notas ao usuário:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Notas</title>
</head>
<body>
    <h1>Minhas Notas</h1>
    <ul>
        {% for nota in notas %}
            <li>{{ nota[1] }}</li>
        {% endfor %}
    </ul>

    <form action="/adicionar" method="POST">
        <input type="text" name="nota" placeholder="Adicionar uma nova nota">
        <button type="submit">Adicionar</button>
    </form>
</body>
</html>
```

### Resumo do MVC:
- **Model**: interage com o banco de dados.
- **View**: exibe as informações ao usuário.
- **Controller**: coordena as ações entre o Model e o View.

---

## Arquitetura de Camadas 🏗️

A **Arquitetura de Camadas** é muito semelhante ao MVC, mas aqui dividimos as responsabilidades em mais "camadas". Algumas dessas camadas podem ser:

- **Models**: Representação dos dados.
- **Views**: Interface com o usuário.
- **Controllers**: Controla a lógica de aplicação.
- **Repositories**: Faz a parte de persistência de dados.
- **Services**: Contém regras de negócio.

### Exemplificando com as mesmas notas:

#### 1. **Models (models.py)**

Os **Models** continuam como na arquitetura MVC. Eles lidam com os dados e as operações no banco.

```python
# models.py
class Nota:
    def __init__(self, id, nota):
        self.id = id
        self.nota = nota
```

#### 2. **Repositories (repositories.py)**

Os **Repositories** são responsáveis por interagir diretamente com o banco de dados. Eles separaram a parte de acesso aos dados da lógica de negócio.

```python
# repositories.py
from models import Nota
import sqlite3

def get_db():
    conn = sqlite3.connect('app.db')
    return conn

def adicionar_nota(nota):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO notas (nota) VALUES (?)', (nota,))
    conn.commit()

def listar_notas():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notas')
    notas = cursor.fetchall()
    return [Nota(id=nota[0], nota=nota[1]) for nota in notas]
```

#### 3. **Services (services.py)**

Os **Services** contêm a lógica de negócio da aplicação, como validar as notas antes de inseri-las, por exemplo.

```python
# services.py
from repositories import adicionar_nota

def adicionar_nota_service(nota):
    if len(nota) > 5:  # Exemplo de validação de nota
        adicionar_nota(nota)
    else:
        raise ValueError("A nota precisa ter mais de 5 caracteres")
```

#### 4. **Controllers (controllers.py)**

Os **Controllers** vão usar os **Repositories** e **Services** para controlar o fluxo de dados.

```python
# controllers.py
from flask import Flask, request, redirect, url_for
from services import adicionar_nota_service
from repositories import listar_notas
from views import mostrar_notas

app = Flask(__name__)

@app.route('/')
def home():
    notas = listar_notas()
    return mostrar_notas(notas)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nota = request.form['nota']
    try:
        adicionar_nota_service(nota)
    except ValueError as e:
        return str(e), 400
    return redirect(url_for('home'))
```

---

## Exercícios ✍️

1. **Criar Nova Rota**: Crie uma nova rota que permita ao usuário excluir uma nota específica.
2. **Adicionar Validação**: Faça a validação para que o usuário não possa adicionar notas vazias.
3. **Criar Camada de Serviço para Listagem**: Crie uma camada de **Service** para listar as notas e refatore o código para utilizá-la.
4. **Melhorar a Interface**: Tente adicionar um layout mais bonito para a página de notas, como usar o Bootstrap para melhorar o visual.

---

### Conclusão 🎉

A arquitetura de software é fundamental para o sucesso e a manutenção de um projeto. Com o **MVC** ou a **Arquitetura de Camadas**, conseguimos separar bem as responsabilidades de cada parte do sistema, o que torna o código mais organizado e fácil de entender.

Essa estrutura ajuda você a crescer como desenvolvedor, mantendo o código mais limpo e escalável. Com o Flask, podemos aplicar esses conceitos de maneira simples e poderosa.

Bons estudos! 😄