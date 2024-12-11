# **Templates Jinja2 no Flask**

## Introdução ao Jinja2

O **Jinja2** é o mecanismo de template usado pelo Flask para integrar lógica Python com HTML. Ele permite que você adicione variáveis, controle de fluxo (condições e laços), e outros elementos dinâmicos em páginas HTML. Isso é especialmente útil para gerar conteúdo dinâmico no front-end.

# Estruturas de Condição no Jinja2

As estruturas de condição no Jinja2 são implementadas com `{% if %}` e `{% elif %}` (equivalente ao `else if`) e finalizadas com `{% endif %}`. Essas estruturas permitem que o HTML seja renderizado de acordo com uma lógica condicional.

### Exemplo 1: Condições Básicas

```html
<h1>Bem-vindo!</h1>

{% if user %}
    <p>Olá, {{ user }}! Você está logado.</p>
{% else %}
    <p>Olá, visitante! Por favor, faça login.</p>
{% endif %}
```

**Explicação:**
- **`{% if user %}`**: Verifica se a variável `user` tem um valor atribuído.
- **`{{ user }}`**: Renderiza o valor da variável Python no HTML.
- **`{% endif %}`**: Fecha o bloco condicional.

## Estruturas de Repetição no Jinja2

As estruturas de repetição no Jinja2 são feitas com `{% for %}` e finalizadas com `{% endfor %}`. 

### Exemplo 2: Iterando em uma Lista

```html
<h2>Lista de tarefas:</h2>
<ul>
    {% for tarefa in tarefas %}
        <li>{{ tarefa }}</li>
    {% endfor %}
</ul>
```

**Explicação:**
- **`{% for tarefa in tarefas %}`**: Itera sobre cada item da lista `tarefas`.
- **`{{ tarefa }}`**: Renderiza cada item da lista como um elemento `<li>`.

### Exemplo 3: Controle com `else` em Laços

Você pode adicionar um bloco `else` para lidar com listas vazias:

```html
<h2>Lista de tarefas:</h2>
<ul>
    {% for tarefa in tarefas %}
        <li>{{ tarefa }}</li>
    {% else %}
        <li>Sem tarefas para hoje!</li>
    {% endfor %}
</ul>
```

## Filtros no Jinja2

No Jinja2, você utiliza o operador **`|`** (pipe) para aplicar filtros às variáveis. Um filtro comum é `length` (equivalente a `len` no Python), que retorna o tamanho de uma lista ou string.

#### Exemplo 4: Usando o Filtro `length`

```html
<p>Você tem {{ tarefas|length }} tarefas pendentes.</p>
```

**Explicação:**
- **`tarefas|length`**: Calcula o tamanho da lista `tarefas`.
- O operador `|` é usado para aplicar filtros.

## Blocos e `extend`

O conceito de blocos permite reutilizar um mesmo layout base para múltiplas páginas. Com `extend`, você pode herdar o layout base em páginas específicas.

### Exemplo 5: Template Base com Blocos

```html
<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{% block title %}Título padrão{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Meu site</h1>
    </header>
    <main>
        {% block content %}
        <!-- Conteúdo será inserido aqui -->
        {% endblock %}
    </main>
    <footer>
        <p>&copy; 2024</p>
    </footer>
</body>
</html>
```

### Exemplo 6: Herança com `extend`

```html
<!-- pagina.html -->
{% extends 'base.html' %}

{% block title %}Página Inicial{% endblock %}

{% block content %}
    <h2>Bem-vindo à Página Inicial!</h2>
{% endblock %}
```

**Explicação:**
- **`{% extends 'base.html' %}`**: Herda o layout de `base.html`.
- **`{% block title %}`** e **`{% block content %}`**: Sobrescrevem os blocos definidos no template base.

## Redirecionamento de Rotas com `redirect` e `url_for`

O Flask oferece a função `redirect` para redirecionar o usuário para outra rota e `url_for` para gerar URLs dinamicamente.

### Exemplo 7: Redirecionamento Simples

```python
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return 'Página de Login'
```

**Explicação:**
- **`redirect(url_for('login'))`**: Redireciona o usuário para a rota `/login`.
- **`url_for('nome_da_funcao')`**: Gera a URL correspondente à função associada à rota.

### Exemplo 8: URL Dinâmica

```python
@app.route('/user/<username>')
def profile(username):
    return f'Perfil de {username}'

@app.route('/go_to_profile')
def go_to_profile():
    return redirect(url_for('profile', username='Daniel'))
```

**Explicação:**
- **`url_for('profile', username='Daniel')`**: Passa o parâmetro `username` dinamicamente para a rota `/user/<username>`.

## Mensagens Flash

Mensagens flash são usadas para enviar mensagens temporárias entre diferentes páginas. Para isso, usamos as funções `flash` e `get_flashed_messages`.

### Exemplo 9: Usando Mensagens Flash

```python
from flask import Flask, flash, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = 'chave-secreta'

@app.route('/')
def home():
    flash('Bem-vindo ao site!')
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
```

**Template: `dashboard.html`**

```html
<h1>Dashboard</h1>
<ul>
    {% for message in get_flashed_messages() %}
        <li>{{ message }}</li>
    {% endfor %}
</ul>
```

**Explicação:**
- **`flash('Bem-vindo ao site!')`**: Envia uma mensagem flash.
- **`get_flashed_messages()`**: Recupera e exibe as mensagens flash.

## Exercícios

- Coloque em prática o que aprendemos com os [exercícios](./Exercícios.md).
