import tkinter as tk
from tkinter import ttk
import random

class JogoAdivinhacao:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Jogo da Adivinhação")

        # Número aleatório
        self.numero = random.randint(1, 100)

        # Número do usuário
        ttk.Label(janela, text="Tente adivinhar o número (1-100):").grid(row=0, column=0, columnspan=2, pady=5)
        self.entrada = ttk.Entry(janela)
        self.entrada.grid(row=1, column=0, padx=5, pady=5)

        # Botão para enviar
        self.botao_tentar = ttk.Button(janela, text="Tentar", command=self.tentar)
        self.botao_tentar.grid(row=1, column=1, padx=5, pady=5)

        # Mensagem de feedback
        self.mensagem = ttk.Label(janela, text="")
        self.mensagem.grid(row=2, column=0, columnspan=2, pady=5)

    def tentar(self):
        try:
            tentativa = int(self.entrada.get())
            if tentativa < self.numero:
                self.mensagem.config(text="Mais alto!")
            elif tentativa > self.numero:
                self.mensagem.config(text="Mais baixo!")
            else:
                self.mensagem.config(text="Acertou! Reiniciando...")
                self.numero = random.randint(1, 100)
        except ValueError:
            self.mensagem.config(text="Erro: Insira um número válido")

if __name__ == "__main__":
    janela = tk.Tk()
    app = JogoAdivinhacao(janela)
    janela.mainloop()