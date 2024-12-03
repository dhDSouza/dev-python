# **Introdução ao Desenvolvimento Web**

Vamos começar com uma base sólida sobre como funciona o desenvolvimento web e suas principais áreas de atuação. Em seguida, exploraremos ferramentas e tecnologias práticas para criar páginas e sistemas simples.

## **Front-end, Back-end e Full-stack**

### **1. O que é Front-end?**

O **Front-end** é a interface do site, tudo o que o usuário vê e interage. Inclui design, botões, imagens, tabelas, formulários e animações.

- **Principais Tecnologias**:
  - **HTML**: A estrutura da página.
  - **CSS**: O estilo visual.
  - **JavaScript**: A interação e dinamicidade.

### **2. O que é Back-end?**

O **Back-end** é o cérebro por trás do site, lidando com lógica, bancos de dados e processamento de informações.

- **Principais Tecnologias**:
  - Linguagens como **Python**, **PHP** e **Java**.
  - Bancos de dados como **MySQL**, **PostgreSQL**, **SQLite**.

### **3. O que é Full-stack?**

O **Full-stack** combina as duas áreas. É quando o desenvolvedor atua tanto no front-end quanto no back-end, criando interfaces e configurando os sistemas que as suportam.

## **Por que Python e o Flask?**

Python é muito usado em desenvolvimento web devido à sua simplicidade e à quantidade de bibliotecas e frameworks disponíveis.

### **Frameworks Populares de Python**

1. **Django**: Um framework completo, ideal para grandes projetos.
2. **Flask**: Leve e flexível, ideal para aprender ou criar projetos menores.

**Por que usar Flask nesta aula?**

- É simples e direto para iniciantes.
- Permite entender conceitos fundamentais antes de adicionar complexidade.

## **HTML: Estruturando uma Página**

### **Exemplo: Estrutura Básica**

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Aula introdutória ao desenvolvimento web.">
    <title>Página Inicial</title>
</head>
<body>
    <header>
        <h1>Minha Primeira Página</h1>
        <p>Bem-vindo ao mundo do desenvolvimento web!</p>
    </header>
    <main>
        <section>
            <h2>Conteúdo Principal</h2>
            <p>Aqui você aprende como estruturar páginas usando HTML.</p>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 - Aula de Introdução ao Desenvolvimento Web</p>
    </footer>
</body>
</html>
```

<details>

<summary>Explicação do Código</summary>

- **`<html lang="pt-br">`**: Informa o idioma do conteúdo (melhora acessibilidade e SEO).
- **`<meta charset="UTF-8">`**: Define suporte para caracteres especiais.
- **`<header>`, `<main>`, `<section>`, `<footer>`**: Elementos semânticos que melhoram organização e SEO.
- **`<meta name="description">`**: Adiciona uma descrição para os motores de busca.

</details>

## **CSS: Estilizando a Página**

### **Exemplo: Estilo Básico**

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    color: #333;
    margin: 0;
    padding: 0;
}

header {
    background-color: #4CAF50;
    color: white;
    padding: 1em;
    text-align: center;
}

main {
    padding: 20px;
}

footer {
    background-color: #333;
    color: white;
    text-align: center;
    padding: 10px 0;
}
```

<details>

<summary>Explicação do Código</summary>

- **`font-family`**: Define a fonte padrão do texto.
- **`background-color`**: Altera a cor de fundo dos elementos.
- **`padding`**: Define espaços internos entre o conteúdo e as bordas.
- **`text-align`**: Centraliza textos em blocos.

</details>

## **Adicionando Formulários**

Formulários são fundamentais para coletar dados de usuários.

### **Exemplo: Formulário Simples**

```html
<form action="/submit" method="POST">
    <label for="nome">Nome:</label>
    <input type="text" id="nome" name="nome" required>

    <label for="email">E-mail:</label>
    <input type="email" id="email" name="email" required>

    <label for="mensagem">Mensagem:</label>
    <textarea id="mensagem" name="mensagem" rows="4" required></textarea>

    <button type="submit">Enviar</button>
</form>
```

<details>

<summary>Explicação do Código</summary>

- **`<form>`**: Define o formulário. Atributos importantes:
  - **`action`**: Define o destino dos dados submetidos.
  - **`method`**: Define o método de envio (GET ou POST).
- **`<label>`**: Descreve os campos do formulário.
- **`<input>`**: Cria campos de texto, e-mail e outros.
- **`<textarea>`**: Área de texto maior.
- **`<button>`**: Botão para enviar os dados.

</details>

## **Trabalhando com Tabelas**

Tabelas organizam dados tabulares, como relatórios ou cadastros.

### **Exemplo: Tabela Simples**

```html
<table border="1">
    <thead>
        <tr>
            <th>Nome</th>
            <th>E-mail</th>
            <th>Telefone</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>João Silva</td>
            <td>joao@email.com</td>
            <td>(51) 99999-9999</td>
        </tr>
        <tr>
            <td>Ana Costa</td>
            <td>ana@email.com</td>
            <td>(51) 98888-8888</td>
        </tr>
    </tbody>
</table>
```

<details>

<summary>Explicação do Código</summary>

- **`<table>`**: Define a tabela.
- **`<thead>`**: Cabeçalho da tabela.
- **`<tbody>`**: Corpo principal.
- **`<tr>`**: Linhas da tabela.
- **`<th>`**: Células de cabeçalho (em negrito por padrão).
- **`<td>`**: Células de dados.

</details>

## **JavaScript: Adicionando Funcionalidades**

### **Exemplo: Validação Simples de Formulário**

```html
<form id="meuFormulario">
    <label for="nome">Nome:</label>
    <input type="text" id="nome" name="nome" required>
    <button type="button" onclick="validarFormulario()">Enviar</button>
</form>

<script>
function validarFormulario() {
    const nome = document.getElementById('nome').value;
    if (!nome) {
        alert('Por favor, preencha o campo Nome.');
    } else {
        alert('Formulário enviado com sucesso!');
    }
}
</script>
```

<details>

<summary>Explicação do Código</summary>

- **`onclick="validarFormulario()"`**: Aciona a função JavaScript ao clicar no botão.
- **`document.getElementById`**: Acessa elementos da página pelo ID.
- **`alert()`**: Exibe uma mensagem ao usuário.

</details>

---

## **Materiais de Apoio**

### **1. Documentação Oficial**

- **HTML**: [https://developer.mozilla.org/pt-BR/docs/Web/HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML)  
- **CSS**: [https://developer.mozilla.org/pt-BR/docs/Web/CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS)  
- **JavaScript**: [https://developer.mozilla.org/pt-BR/docs/Web/JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)  
- **Flask**: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)

### **2. Cursos Gratuitos**

- [Curso de HTML e CSS - W3Schools](https://www.w3schools.com/html/)  
- [Curso de JavaScript - FreeCodeCamp](https://www.freecodecamp.org/)

#### **3. Vídeos no YouTube**

- [Introdução ao HTML e CSS - Rocketseat](https://www.youtube.com/watch?v=GykTLqODQuU)  

---

## **Exercícios Práticos**

### **Parte 1: HTML e CSS**

1. **Estruture uma página com os seguintes requisitos**:

   - Um cabeçalho com o título da página.
   - Um menu de navegação.
   - Uma seção principal com um artigo e uma lista de tópicos.
   - Um rodapé com informações de contato.

2. **Adicione estilos à sua página**:

   - Aplique uma fonte de sua escolha.
   - Altere as cores do cabeçalho e do rodapé.
   - Crie um layout responsivo com o uso de `flexbox` ou `grid`.
        - Ver [Conteúdo sobre Flexbox](https://github.com/dhDSouza/dev-frontend-3k-talentos-ti/blob/main/Flexbox/Material%20de%20Apoio.md)
        - Ver [Conteúdo sobre Grid Layout](https://github.com/dhDSouza/dev-frontend-3k-talentos-ti/blob/main/Grid%20Layout/Material%20de%20Apoio.md)

### **Exercícios de SEO e Semântica**

1. **Melhore uma página já criada**:

   - Adicione meta tags para título, descrição e palavras-chave.
   - Use tags semânticas como `<header>`, `<main>`, `<article>`, `<section>`.

---

### **Parte 2: JavaScript**

1. **Interatividade com Formulários**:

   - Valide um formulário para garantir que o usuário preencha todos os campos obrigatórios antes de enviar.
   - Adicione uma mensagem de confirmação personalizada ao clicar em um botão de envio.

2. **Criação de Elementos Dinâmicos**:

   - Crie uma página onde o usuário possa adicionar itens a uma lista de tarefas.
   - Permita que os itens sejam marcados como "concluídos" e removidos.
