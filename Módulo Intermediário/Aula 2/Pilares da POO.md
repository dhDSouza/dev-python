# Pilares da Programação Orientada a Objetos

## Objetivo da Aula

Entender e aplicar os quatro pilares da POO: **Encapsulamento, Polimorfismo, Herança e Abstração**. Esses pilares são fundamentais para construir programas organizados, reutilizáveis e fáceis de manter.

## 1. **Abstração**

**O que é?**

A Abstração é o processo de esconder detalhes complexos e mostrar apenas o necessário. Em outras palavras, é como simplificar a visão de algo, focando no que realmente importa para quem vai usar.

**Exemplo:**

Imagina que você tem uma Pokédex (do universo Pokémon). A Pokédex mostra apenas informações úteis sobre cada Pokémon, como nome, tipo e poderes. Não mostra todos os detalhes internos (como a genética exata ou composição celular), apenas o que um treinador precisa saber.

**Em Python:**

```python
class Pokemon:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def atacar(self):
        print(f"{self.nome} usou um ataque do tipo {self.tipo}!")

# Exemplo de uso
pikachu = Pokemon("Pikachu", "Elétrico")
pikachu.atacar()  # Saída: Pikachu usou um ataque do tipo Elétrico!
```

Aqui, o objeto `pikachu` abstrai tudo que é desnecessário para o treinador e mostra apenas as informações importantes.

## 2. **Encapsulamento**

**O que é?**

Encapsulamento é a prática de proteger e controlar o acesso aos dados de um objeto. Em POO, isso é feito usando variáveis privadas e métodos específicos para acessar ou modificar esses dados.

**Exemplo:**  

Imagine o Homem de Ferro. A armadura dele é super complexa e tem vários segredos, como a fonte de energia e sistemas de ataque, mas só ele (ou quem ele autorizar) pode usar esses sistemas. No código, isso seria feito tornando algumas partes privadas.

**Em Python:**

```python
class Armadura:
    def __init__(self, nome, poder):
        self.nome = nome
        self.__poder = poder  # atributo privado

    def mostrar_poder(self):
        return self.__poder  # acessar o poder de maneira controlada

# Exemplo de uso
armadura_tony = Armadura("Mark 50", "Explosão de energia")
print(armadura_tony.nome)  # Saída: Mark 50
print(armadura_tony.mostrar_poder())  # Saída: Explosão de energia
```

Aqui, o poder da armadura está encapsulado (ou seja, protegido) e só pode ser acessado pelo método `mostrar_poder()`.

## 3. **Herança**

**O que é?**  

Herança permite que uma classe (subclasse) herde características e comportamentos de outra classe (superclasse). Isso evita duplicação de código e permite reaproveitar funcionalidades.

**Exemplo:**  

Em “Star Wars”, um Jedi tem características e habilidades especiais (como o uso da Força e habilidades de combate). Os aprendizes (Padawans) herdam essas habilidades de seus mestres Jedi, mas também podem ter habilidades únicas.

**Em Python:**

```python
class Jedi:
    def __init__(self, nome):
        self.nome = nome

    def usar_forca(self):
        print(f"{self.nome} usou a Força!")

class Padawan(Jedi):
    def treinar(self):
        print(f"{self.nome} está treinando para ser um Jedi.")

# Exemplo de uso
anakin = Padawan("Anakin Skywalker")
anakin.usar_forca()  # Saída: Anakin Skywalker usou a Força!
anakin.treinar()  # Saída: Anakin Skywalker está treinando para ser um Jedi.
```

Aqui, `Padawan` herda de `Jedi`, podendo usar os métodos da classe `Jedi` e também definir novos comportamentos próprios.

## 4. **Polimorfismo**

**O que é?**  

Polimorfismo permite que diferentes objetos realizem a mesma ação de maneiras diferentes. Em outras palavras, você pode ter métodos com o mesmo nome que se comportam de maneira diferente dependendo do objeto que os usa.

**Exemplo:**  

No universo de super-heróis, vários personagens têm uma habilidade chamada “ataque especial”, mas cada um faz isso de um jeito único: o Goku usa o Kamehameha, o Homem de Ferro usa o raio repulsor, e o Thor usa o martelo Mjolnir.

**Em Python:**

```python
class Personagem:
    def ataque_especial(self):
        pass  # método vazio, será implementado nas subclasses

class Goku(Personagem):
    def ataque_especial(self):
        print("Goku usou o Kamehameha!")

class Thor(Personagem):
    def ataque_especial(self):
        print("Thor usou o Mjolnir!")

# Exemplo de uso
personagens = [Goku(), Thor()]
for personagem in personagens:
    personagem.ataque_especial()
```

Neste exemplo, tanto `Goku` quanto `Thor` têm o mesmo método `ataque_especial`, mas com comportamentos diferentes. Isso é polimorfismo em ação.

## Resumo dos Pilares

1. **Abstração**: Mostra só o essencial e esconde a complexidade. Ex.: Pokédex simplificando a informação dos Pokémon.
2. **Encapsulamento**: Protege dados e controla o acesso a eles. Ex.: Homem de Ferro mantendo sistemas da armadura protegidos.
3. **Herança**: Permite que uma classe herde características de outra. Ex.: Padawans herdam habilidades de Jedi.
4. **Polimorfismo**: Permite que objetos diferentes usem métodos com o mesmo nome de maneiras diferentes. Ex.: Goku e Thor usando o `ataque_especial` de formas distintas.

## Exercício Prático

1. **Desafio de Herança e Polimorfismo:** Crie uma classe `PersonagemDeAnime` com um método `poder_especial`. Em seguida, crie classes como `Naruto` e `Luffy` que herdam de `PersonagemDeAnime`, cada uma implementando `poder_especial` de forma única (ex.: Naruto usa Rasengan, Luffy usa Gomu Gomu no Pistol).
  
2. **Desafio de Encapsulamento:** Crie uma classe `SegredoDoHerói` que possui um atributo privado `identidade_secreta`. Implemente métodos para acessar e modificar a identidade secreta de forma controlada.

## Conclusão

Esses quatro pilares formam a base da POO e ajudam a organizar o código de forma mais lógica e reutilizável. Cada conceito tem uma aplicação prática e facilita a criação de sistemas mais robustos e modulares.
