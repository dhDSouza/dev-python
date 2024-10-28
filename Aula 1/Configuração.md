# Configuração do Ambiente de Desenvolvimento para Python

Este guia irá ajudá-lo a configurar um ambiente de desenvolvimento para Python em seu computador, seja você um usuário de **Windows**, **macOS**, ou **Linux**. Além disso, vamos configurar um editor de código e um ambiente virtual para garantir que todos os projetos estejam bem organizados.

## 1. Instalação do Python

### 1.1 Verificando se o Python já está instalado

Antes de instalar o Python, verifique se ele já está presente no seu sistema:

- **Windows**:
   1. Abra o Prompt de Comando (digite `cmd` na barra de pesquisa).
   2. Digite o seguinte comando e pressione Enter:

      ```bash
      py --version
      ```

   3. Se o Python estiver instalado, a versão instalada será exibida (ex: `Python 3.9.7`). Caso contrário, siga os passos de instalação abaixo.

- **macOS / Linux**:
   1. Abra o Terminal.
   2. Digite o seguinte comando e pressione Enter:

      ```bash
      python3 --version
      ```

   3. Se o Python estiver instalado, você verá a versão exibida. Se não estiver, siga os passos a seguir para instalar.

### 1.2 Instalando o Python

- **Windows**:
   1. Acesse o site oficial do Python: [https://www.python.org/downloads/](https://www.python.org/downloads/).
   2. Baixe a versão mais recente (certifique-se de selecionar a versão 3.x).
   3. Durante a instalação, **marque a opção “Add Python to PATH”** para garantir que o Python seja acessível de qualquer lugar no sistema.
   4. Finalize a instalação e teste novamente no Prompt de Comando:

      ```bash
      python --version
      ```

- **macOS**:
   1. Acesse [https://www.python.org/downloads/](https://www.python.org/downloads/) e baixe o instalador mais recente.
   2. Execute o instalador e siga as instruções na tela.
   3. Depois de instalado, abra o Terminal e digite:

      ```bash
      python3 --version
      ```

   4. Se preferir, você também pode instalar o Python usando o Homebrew:

      ```bash
      brew install python
      ```

- **Linux (Ubuntu/Debian)**:
   1. Abra o Terminal.
   2. Atualize os repositórios de software:

      ```bash
      sudo apt update
      ```

   3. Instale o Python:

      ```bash
      sudo apt install python3
      ```

   4. Verifique a instalação:

      ```bash
      python3 --version
      ```

## 2. Escolhendo um Editor de Código

### 2.1 Visual Studio Code (VS Code)

O VS Code é um editor de código leve, gratuito e com muitos recursos úteis para desenvolvimento em Python. Vamos configurá-lo!

1. **Instalação**:
   - Acesse: [https://code.visualstudio.com/](https://code.visualstudio.com/) e baixe a versão para o seu sistema operacional.
   - Siga as instruções para instalar o VS Code.

2. **Extensão para Python**:
   - Abra o VS Code.
   - No menu lateral esquerdo, clique em **Extensões** (ícone de quadrado).
   - Pesquise por “Python” e instale a extensão oficial da Microsoft.

3. **Configuração do Interpretador Python**:
   - Abra qualquer arquivo `.py` no VS Code.
   - Você verá uma notificação pedindo para selecionar o interpretador Python. Escolha a versão que você instalou anteriormente (`Python 3.x`).

### 2.2 Outros Editores (Opcional)

Se você preferir, pode usar outros editores, como:

- **PyCharm**: Um IDE mais robusto para Python. Baixe em [https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/).
- **Jupyter Notebook**: Bom para prototipagem e notebooks interativos. Pode ser instalado com `pip install jupyter`.

## 3. Criando um Ambiente Virtual

Ambientes virtuais são úteis para gerenciar dependências específicas de cada projeto, isolando pacotes e versões que você usar.

### 3.1 Criando um Ambiente Virtual

1. Abra o Terminal (ou Prompt de Comando no Windows).
2. Navegue até o diretório onde você deseja criar seu projeto usando o comando `cd`.
3. Digite o seguinte comando para criar um ambiente virtual:

   ```bash
      python -m venv nome_do_ambiente
   ```

   - Substitua `nome_do_ambiente` pelo nome que preferir (ex: `venv` ou `meu_ambiente`).

### 3.2 Ativando o Ambiente Virtual

- **Windows**:

   ```bash
      nome_do_ambiente\Scripts\activate
   ```

- **macOS / Linux**:

   ```bash
      source nome_do_ambiente/bin/activate
   ```

Após ativar o ambiente, você verá o nome do ambiente aparecendo no terminal, indicando que ele está ativo.

### 3.3 Instalando Pacotes no Ambiente

Agora que o ambiente está ativo, você pode instalar pacotes usando o `pip`. Por exemplo, para instalar o Flask (framework web), use:

```bash
pip install flask
```

Para verificar todos os pacotes instalados no ambiente:

```bash
pip list
```

### 3.4 Desativando o Ambiente Virtual

Quando terminar de trabalhar no seu projeto, desative o ambiente:

```bash
deactivate
```

## 4. Testando o Ambiente

Para garantir que tudo está configurado corretamente, crie um arquivo chamado `teste.py` no diretório do seu projeto e adicione o seguinte código:

```python
print("Hello, World!")
```

- **Explicação**: `print()` é uma função que exibe uma mensagem na tela. O exemplo acima é um clássico usado para garantir que tudo está configurado corretamente.

Execute o arquivo no terminal (ou no VS Code):

```bash
python teste.py
```

Se a mensagem **“Hello, World!”** aparecer, tudo está funcionando!

## 5. Próximos Passos

- Agora que o ambiente está configurado, vamos começar a programar! Na próxima aula, vamos explorar variáveis, tipos de dados e as operações básicas em Python.
