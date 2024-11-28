import tkinter as tk
from tkinter import ttk

class GerenciadorPokemons:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Gerenciador de Pokémons")

        # Entradas
        ttk.Label(janela, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
        self.nome = ttk.Entry(janela)
        self.nome.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(janela, text="Tipo:").grid(row=1, column=0, padx=5, pady=5)
        self.tipo = ttk.Entry(janela)
        self.tipo.grid(row=1, column=1, padx=5, pady=5)

        # Botões
        self.botao_adicionar = ttk.Button(janela, text="Adicionar", command=self.adicionar_pokemon)
        self.botao_adicionar.grid(row=2, column=0, padx=5, pady=5)

        self.botao_remover = ttk.Button(janela, text="Remover", command=self.remover_pokemon)
        self.botao_remover.grid(row=2, column=1, padx=5, pady=5)

        # Lista de Pokémons
        self.lista = ttk.Treeview(janela, columns=("Nome", "Tipo"), show="headings")
        self.lista.heading("Nome", text="Nome")
        self.lista.heading("Tipo", text="Tipo")
        self.lista.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def adicionar_pokemon(self):
        nome = self.nome.get().strip()
        tipo = self.tipo.get().strip()
        if nome and tipo:
            self.lista.insert("", "end", values=(nome, tipo))
            self.nome.delete(0, tk.END)
            self.tipo.delete(0, tk.END)

    def remover_pokemon(self):
        for item in self.lista.selection():
            self.lista.delete(item)

if __name__ == "__main__":
    janela = tk.Tk()
    app = GerenciadorPokemons(janela)
    janela.mainloop()