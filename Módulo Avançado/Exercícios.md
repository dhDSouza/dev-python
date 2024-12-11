# Lista de exercícios

## Exercício 1: Estruturas de Condição

Crie um template que exibe uma mensagem diferente dependendo da idade de um usuário. Se a idade for maior ou igual a 18, deve exibir "Você é maior de idade". Caso contrário, exibir "Você é menor de idade".

**Requisitos:**

- A idade deve ser uma variável dinâmica passada para o template.
- Use a estrutura `{% if %}` e `{% else %}` para a condição.

## Exercício 2: Laços de Repetição com Listas

Crie uma página que exibe uma lista de cursos oferecidos por uma escola. Caso a lista de cursos esteja vazia, exiba a mensagem "Nenhum curso disponível no momento".

**Requisitos:**

- A lista de cursos deve ser passada como variável para o template.
- Use o laço `{% for %}` com `{% else %}`.

## Exercício 3: Filtros do Jinja2

Crie uma página que exibe o comprimento de uma lista de tarefas e se a lista está vazia ou não.

**Requisitos:**

- Use o filtro `length` para exibir o número de tarefas.
- Use uma estrutura condicional para exibir uma mensagem diferente caso a lista de tarefas esteja vazia.

## Exercício 4: Herança de Templates

Crie um layout base para o site e depois crie duas páginas que herdem desse layout. Cada página deve sobrescrever o título e o conteúdo.

**Requisitos:**

- Use a tag `{% extends 'base.html' %}` e os blocos `{% block %}` para sobrescrever conteúdo.
- O layout base deve ter um título e um corpo com áreas para os títulos e conteúdo dinâmico.

## Exercício 5: Redirecionamento com `url_for`

Crie uma página inicial com um link para a página de login. Quando o usuário acessar a página inicial, ele deve ser redirecionado automaticamente para a página de login.

**Requisitos:**

- Use `redirect` e `url_for` para fazer o redirecionamento.
- Crie uma rota para a página de login.

## Exercício 6: Mensagens Flash

Crie uma página de login onde, ao enviar um formulário sem preencher o nome de usuário ou senha, o usuário verá uma mensagem de erro utilizando a função `flash`.

**Requisitos:**

- Use `flash` para enviar uma mensagem de erro.
- Use `get_flashed_messages()` para exibir a mensagem no template.
