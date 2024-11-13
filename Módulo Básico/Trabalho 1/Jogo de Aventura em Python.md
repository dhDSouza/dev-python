# Trabalho Avaliativo: Criando um Jogo de Aventura em Python

**Objetivo:**

O objetivo deste trabalho é aplicar os conhecimentos adquiridos até agora sobre programação em Python para desenvolver um jogo simples de aventura no estilo de um RPG, onde o jogador precisa tomar decisões e interagir com o ambiente, usando variáveis, tipos de dados, estruturas condicionais, loops, listas, funções e entrada de dados (input). O jogo será baseado em um cenário fictício inspirado em jogos de aventura e cultura pop.

**Enunciado:**

Você vai criar um jogo interativo de aventura no qual o jogador assume o papel de um herói em uma missão importante. Durante o jogo, o jogador precisará tomar decisões que irão afetar o rumo da história e determinar se ele vai ser bem-sucedido ou falhar.

## Requisitos

1. **Configuração do Jogo:**

   - O jogo começa com uma introdução que descreve brevemente o cenário. O jogador deve ser apresentado ao contexto da aventura e escolher um personagem inicial, que pode ter diferentes habilidades (força, inteligência, agilidade, etc.). Use uma **lista** para armazenar esses personagens e suas habilidades.

2. **História e Escolhas:**

   - O jogo deve ser estruturado por uma série de **condições** e **escolhas**. O jogador, em determinado momento, será apresentado a situações e precisará tomar decisões, como escolher para onde ir ou o que fazer em determinadas situações. Essas escolhas devem ser feitas usando o comando `input()`.
   - Para cada escolha, o jogador pode ser direcionado para diferentes partes do jogo, onde novos desafios ou perguntas serão feitas.

3. **Sistema de Batalha:**

   - Durante o jogo, o personagem pode enfrentar inimigos (criaturas, vilões, etc.). Para isso, crie uma **função** que simula uma batalha. A batalha deve levar em consideração a habilidade do personagem (como força ou inteligência), e o inimigo terá um "poder" ou "vida" que pode ser derrotado com o tempo.
   - O jogador deve ter a opção de atacar ou fugir. O resultado da batalha deve ser afetado pelas escolhas do jogador e pelas características do personagem (isso pode ser feito com uma fórmula simples, mas envolvente).

4. **Exploração e Itens:**

   - Ao longo do jogo, o jogador pode encontrar itens ou **armas** que o ajudarão na jornada. Crie uma **lista** de itens, como "espada", "pocão de cura", etc. Os itens podem ser coletados ao longo do caminho e o jogador pode usá-los durante batalhas.
   - Implementar um comando que permita ao jogador "usar" um item durante o jogo, afetando a história ou o combate.

5. **Condições e Loops:**

   - O jogo deve usar **estruturas de repetição** (`for` ou `while`) para permitir que o jogador faça escolhas repetidas até alcançar um resultado (vencer ou falhar).
   - Utilize **condicionais** (`if`, `elif`, `else`) para verificar as escolhas feitas pelo jogador e direcioná-lo conforme o progresso da história.

6. **Pontuação e Fim de Jogo:**

   - Crie um sistema de **pontuação** ou **progressão** que indique se o jogador está indo bem ou mal. A pontuação pode ser alterada com base em decisões, batalhas vencidas ou itens adquiridos.
   - O jogo deve ter um fim, que pode ser um final bom ou ruim dependendo das escolhas feitas pelo jogador durante a aventura.

## Exemplos de Funções e Estruturas Esperadas

- **Função de batalha:**

  ```python
  def batalha(player_poder, inimigo_poder):
      if player_poder > inimigo_poder:
          return "Vitória!"
      elif player_poder == inimigo_poder:
          return "Empate!"
      else:
          return "Derrota!"
  ```

- **Função para coletar itens:**

  ```python
  def coletar_item(item, inventario):
      inventario.append(item)
      print(f"Você coletou um(a) {item}. Seu inventário agora: {inventario}")
  ```

- **Função para iniciar a jornada:**

  ```python
  def iniciar_jogo():
      print("Bem-vindo à aventura!")
      personagem = escolher_personagem()
      explorar_mundo(personagem)
  ```

### Detalhamento do Jogo

1. **Introdução ao Jogo:**

   - O jogo começa com um texto que descreve o cenário de uma cidade em perigo, onde um herói é necessário. O jogador pode escolher entre diferentes personagens (por exemplo, Guerreiro, Mago, Arqueiro).

2. **Escolha de Personagem:**

   - O jogador escolhe seu personagem, e cada personagem tem atributos únicos, como força, agilidade e inteligência. Esses atributos podem influenciar os resultados das batalhas e das decisões.

3. **Primeira Missão:**

   - O jogador deve enfrentar uma criatura (um monstro simples) e deve decidir como atacá-la ou se proteger. O uso de itens (como uma espada ou uma poção de cura) pode ser essencial para a vitória.

4. **Decisões Críticas:**

   - Ao longo da jornada, o jogador precisa tomar decisões importantes. Por exemplo, ao entrar em uma caverna, ele pode decidir seguir em frente ou voltar. Cada decisão leva a resultados diferentes. O uso de loops e condicionais será fundamental para gerenciar essas decisões.

5. **Batalhas e Desafios:**

   - Ao longo do caminho, o jogador enfrentará inimigos mais fortes. O sistema de combate será baseado em escolhas, onde o jogador pode usar sua força, magia ou itens do inventário para tentar derrotar os inimigos.

6. **Final do Jogo:**

   - O jogo terminará de forma diferente, dependendo das escolhas do jogador. Ele pode terminar com o personagem derrotado, ou o jogador pode ser bem-sucedido na missão, salvando a cidade.

## Requisitos Técnicos

- **Estruturas de Dados:**

  - Use **listas** para armazenar personagens, itens e inimigos.
  - Use **dicionários** para associar atributos aos personagens (por exemplo, força, inteligência, agilidade).

- **Funções:**

  - Use **funções** para modularizar o código. Cada tarefa importante (como batalha, escolha de personagem, exploração) deve ser implementada como uma função separada.

- **Entrada e Saída:**

  - Utilize **input()** para receber escolhas do jogador.
  - Utilize **print()** para fornecer feedback ao jogador sobre o que está acontecendo no jogo.

## Entregáveis

- O código Python completo com os requisitos acima implementados.
- Um relatório explicando como o jogo funciona e como cada parte do código foi implementada.

**Forma de Entrega:**

- Compacte o código e o relatório, em uma pasta zipada `(.zip)` renomeie a pasta para `"Trabalho 1 Python - <seu nome completo>"`.
- Envie a pasta zipada por e-mail para [dhs.danielsouza@gmail.com](dhs.danielsouza@gmail.com).
- Coloque no assunto do e-mail: `Trabalho 1 Python - <seu nome completo>`

**`ATENÇÃO! O PRAZO DE ENTREGA É ATÉ DIA 11/11 (SEGUNDA-FEIRA)`**

**Critérios de Avaliação:**

- Funcionalidade: O jogo funciona conforme descrito, com diferentes possibilidades e um final condicional.
- Uso correto de variáveis, tipos de dados, estruturas de repetição, condicionais, listas e funções.
- Criatividade e engajamento: A história, as escolhas e a jogabilidade devem ser interessantes e dinâmicas.

Boa sorte, aventureiros! Que vençam os melhores codificadores!
