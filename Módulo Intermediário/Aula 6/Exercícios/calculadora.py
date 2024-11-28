import tkinter as tk
from tkinter import ttk

class Calculadora:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Calculadora Básica")

        # Números
        ttk.Label(janela, text="Número 1:").grid(row=0, column=0, padx=5, pady=5)
        self.num1 = ttk.Entry(janela)
        self.num1.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(janela, text="Número 2:").grid(row=1, column=0, padx=5, pady=5)
        self.num2 = ttk.Entry(janela)
        self.num2.grid(row=1, column=1, padx=5, pady=5)

        # Operações
        ttk.Label(janela, text="Operação:").grid(row=2, column=0, padx=5, pady=5)
        self.operacao = ttk.Combobox(janela, values=["Soma", "Subtração", "Multiplicação", "Divisão"])
        self.operacao.grid(row=2, column=1, padx=5, pady=5)
        self.operacao.set("Soma")

        # Botão calcular
        self.botao_calcular = ttk.Button(janela, text="Calcular", command=self.calcular)
        self.botao_calcular.grid(row=3, column=0, columnspan=2, pady=10)

        # Resultado
        self.resultado = ttk.Label(janela, text="Resultado: ")
        self.resultado.grid(row=4, column=0, columnspan=2, pady=5)

    def calcular(self):
        try:
            n1 = float(self.num1.get())
            n2 = float(self.num2.get())
            op = self.operacao.get()

            match(op):
                case "Soma":
                    res = n1 + n2
                case "Subtração":
                    res = n1 - n2
                case "Multiplicação":
                    res = n1 * n2
                case "Divisão":
                    if n2 == 0:
                        self.resultado.config(text="Erro: Divisão por zero")
                        return
                    res = n1 / n2
                case _:
                    res = "Operação inválida"

            self.resultado.config(text=f"Resultado: {res}")
        except ValueError:
            self.resultado.config(text="Erro: Insira números válidos")

if __name__ == "__main__":
    janela = tk.Tk()
    app = Calculadora(janela)
    janela.mainloop()