# Estrutura de Repetição `while` em Python

## Objetivo da Aula

Nesta aula, vamos aprender sobre a **estrutura de repetição `while`** no Python. Vamos entender como ela funciona, para que serve e ver exemplos práticos e exercícios legais para praticar o conceito.

## O que é o Laço `while`?

O `while` é uma estrutura de repetição que executa um bloco de código enquanto uma condição é verdadeira. Diferente do `for`, que geralmente é usado quando sabemos quantas vezes o laço deve ser executado, o `while` é ideal para situações em que **não sabemos ao certo quantas repetições serão necessárias**. Ele continua repetindo o bloco de código até que a condição seja falsa.

### Analogia

Imagine que você está jogando um videogame onde precisa atravessar uma fase cheia de obstáculos. Enquanto você tiver "vida" no jogo, você continua jogando. Assim que a "vida" acaba, você para de jogar. Esse "enquanto você tiver vida" é o conceito do `while`.

## Sintaxe Básica do `while`

A sintaxe do `while` em Python é simples. Abaixo está a estrutura básica:

```python
while condição:
    # bloco de código a ser repetido
```

- O **bloco de código** é executado enquanto a **condição** é verdadeira.
- Assim que a condição se torna falsa, o loop para de executar.

## Exemplo Básico: Contagem com `while`

Vamos começar com um exemplo básico onde usamos o `while` para fazer uma contagem de 1 a 5.

```python
contador = 1
while contador <= 5:
    print(contador)
    contador += 1  # aumenta o valor de contador a cada repetição
```

**Explicação**:

- A variável `contador` começa em 1.
- O `while` verifica se `contador` é menor ou igual a 5.
- Se a condição for verdadeira, ele imprime o valor e aumenta o `contador` em 1.
- O loop para de executar quando `contador` se torna 6.

## Exercícios Práticos com `while`

1. **Adivinhação de Número**

   - Crie um programa que peça ao usuário para adivinhar um número entre 1 e 10.
   - O programa deve continuar pedindo até que o usuário adivinhe o número correto.
   - Quando o número for adivinhado, exiba uma mensagem de "Parabéns! Você acertou!".

2. **Contagem Regressiva**

   - Peça ao usuário um número e exiba uma contagem regressiva até o zero.
   - Quando a contagem terminar, exiba a mensagem "Boom!".

3. **Senha Correta**

   - Crie um programa que simule um sistema de login.
   - Peça ao usuário uma senha e continue pedindo até que ele digite a senha correta, que pode ser, por exemplo, `"python123"`.
   - Ao final, mostre uma mensagem de "Acesso concedido".

4. **Calculadora de Tabuada**

   - Crie um programa que peça ao usuário um número e exiba a tabuada desse número de 1 a 10.
   - O usuário deve poder digitar um novo número para ver a tabuada até que ele escolha sair.

5. **Jogo de Adivinhação com Tentativas**

   - Crie um jogo de adivinhação onde o usuário precisa adivinhar um número entre 1 e 20.
   - Ele tem no máximo 5 tentativas para acertar. Se errar todas, o jogo acaba com a mensagem "Você perdeu!".

6. **Simulador de Caixinha de Dinheiro**

   - Simule uma caixinha de dinheiro. Pergunte ao usuário quanto ele quer colocar ou retirar do saldo inicial, que começa em R$100.
   - O usuário pode colocar ou retirar quantas vezes quiser, mas o programa deve impedir retiradas que deixem o saldo negativo.
   - O loop termina quando o usuário digita "sair".

7. **Sorteio de Números**

   - Crie um programa que sorteia números entre 1 e 100 e pergunta ao usuário se ele quer continuar ou parar.
   - Se o usuário digitar “parar” e o número sorteado for `par`, ele ganha um ponto. Caso contrário, ele perde um ponto.
   - O programa termina se o usuário digitar “parar” ou com um número impar sorteado.

8. **Histórico de Mensagens em um Chat**

   - Simule um chat onde o usuário pode enviar mensagens digitando-as.
   - O programa armazena as mensagens enviadas e as exibe ao usuário.
   - O chat termina quando o usuário digita “sair”, e o programa exibe o histórico completo.
