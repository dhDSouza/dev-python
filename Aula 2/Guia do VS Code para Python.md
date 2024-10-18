# Configurando o Visual Studio Code (VS Code)

O VS Code é um dos editores mais populares e poderosos para desenvolvimento em Python. Vamos configurá-lo com extensões e ajustes que ajudam a aumentar a produtividade.

## 1. Instalação das Extensões Necessárias

Abra o VS Code e vá até a aba de **Extensões** (ícone de quadrado no menu lateral esquerdo). Instale as seguintes extensões:

1. **Python** (Microsoft):
   - Esta é a extensão oficial da `Microsoft` para suporte a Python. Ela fornece `linting`, `IntelliSense` (autocompletar), execução de testes, formatação de código, suporte a notebooks Jupyter e muito mais.

2. **Pylance** (Microsoft):
   - O Pylance trabalha em conjunto com a extensão Python. Ele oferece recursos de autocompletar mais rápidos e precisos e ajuda na análise estática do código.

3. **Python Indent**:
   - Corrige problemas de indentação automática em código Python, um detalhe importante, já que a indentação é fundamental na linguagem.

4. **autopep8** ou **Black Formatter**:
   - Escolha um desses formatadores de código para manter o código limpo e seguindo o padrão PEP8. O autopep8 é mais leve, mas o Black é mais robusto e automático.

5. **Code Runner**:
   - Permite executar rapidamente arquivos ou trechos de código direto no terminal embutido do VS Code, tornando a execução de scripts Python mais prática.

6. **GitLens**:
   - Uma ferramenta poderosa para integração com `Git`. Ajuda a visualizar o histórico de `commits` e o controle de versão direto no editor.

## 2. Configurando o Interpretador Python no VS Code

Após instalar as extensões:

1. **Abrindo o arquivo Python**:

   - Abra qualquer arquivo `.py` no VS Code ou crie um novo. Assim que o arquivo for aberto, uma notificação aparecerá pedindo para selecionar o interpretador Python.
   - Clique na notificação ou vá até a **Barra de Status** (parte inferior) e clique no nome do interpretador que aparece.
   - Escolha a versão que você instalou anteriormente (por exemplo, `Python 3.x`). Se você estiver usando um ambiente virtual, selecione o interpretador dentro desse ambiente para garantir que ele seja usado para o projeto.

## 3. Configuração de Ambientes Virtuais no VS Code

Se você estiver trabalhando com ambientes virtuais (recomendado para cada projeto), o VS Code pode detectá-los automaticamente:

1. Certifique-se de que o ambiente virtual está ativado no terminal do VS Code.
2. Abra o **Command Palette** pressionando `Ctrl + Shift + P` (Windows/Linux) ou `Cmd + Shift + P` (macOS).
3. Digite **Python: Select Interpreter** e selecione o interpretador do ambiente virtual que você criou para o projeto.

> **Dica**: Sempre que iniciar um novo projeto e criar um ambiente virtual, selecione o interpretador correto para garantir que o VS Code use os pacotes e dependências corretas.

## 4. Ajustes de Linting e Formatação

Para garantir que seu código Python siga as boas práticas (PEP8) e que erros sejam detectados automaticamente, siga estes passos:

1. Abra as **Configurações** do VS Code (`Ctrl + ,` ou `Cmd + ,` no macOS).
2. Busque por **Python Linting** e certifique-se de que está habilitado.
3. Escolha uma ferramenta de linting, como `pylint` ou `flake8` (elas precisam estar instaladas no ambiente Python). Essas ferramentas irão verificar seu código em tempo real e alertar sobre possíveis problemas.
4. Para a formatação automática, busque por **Python Formatting Provider** e selecione o formatador instalado (por exemplo, `autopep8` ou `Black`).

## 5. Debugging no VS Code

O VS Code possui um poderoso **Debug Console** para Python:

1. Abra um arquivo Python e adicione um breakpoint clicando à esquerda do número da linha.
2. No menu lateral esquerdo, clique no ícone de **Run and Debug** (triângulo com um inseto) e escolha **Python File**.
3. O VS Code iniciará o debugger e parará nos breakpoints que você definiu, permitindo inspecionar variáveis, alterar valores e passar pelas linhas de código com facilidade.

> **Dica**: Ao configurar scripts mais complexos, você pode usar o arquivo `.vscode/launch.json` para personalizar a execução e os argumentos do script durante o debug.

## 6. Extensões Adicionais (Opcional)

- **Python Docstring Generator**: Gera automaticamente docstrings (documentação inline) para suas funções, facilitando a documentação do seu código.
- **Bracket Pair Colorizer**: Colore os parênteses, colchetes e chaves para facilitar a visualização de blocos de código.
- **Prettier - Code formatter**: Caso você trabalhe com outras linguagens, essa extensão é ótima para padronizar e formatar diversos tipos de arquivos.

### 7. Executando Scripts no VS Code

Com todas as extensões configuradas, você pode facilmente rodar scripts Python:

1. Clique com o botão direito em um arquivo `.py` e selecione **Run Python File in Terminal**.
2. Use a extensão **Code Runner** para selecionar um trecho específico do código e executá-lo no terminal.
