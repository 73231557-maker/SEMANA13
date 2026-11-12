import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora - Semana 13")
        self.ventana.geometry("400x400")
        self.ventana.resizable(False, False)

        # Display
        self.display = tk.Entry(
            self.ventana,
            font=("Arial", 24),
            justify="right",
            bd=5
        )
        self.display.grid(
            row=0, column=0, columnspan=4,
            sticky="nsew", padx=5, pady=5
        )
#Paso 3: Agregar los botones
        # Definir botones en una matriz
        botones = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('C', '0', '=', '+'),
        ]

        for i, fila in enumerate(botones):
            for j, texto in enumerate(fila):
                btn = tk.Button(
                    self.ventana,
                    text=texto,
                    font=("Arial", 18),
                    width=4,
                    height=2,
                    command=lambda t=texto: self.click(t)
                )
                btn.grid(row=i+1, column=j, padx=2, pady=2)
#Paso 4: Implementar la lógica de eventos
    def click(self, valor):
        if valor == 'C':
            self.display.delete(0, tk.END)
        elif valor == '=':
            try:
                expresion = self.display.get()
                resultado = eval(expresion)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(resultado))
            except Exception:
                messagebox.showerror("Error", "Expresión inválida")
                self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, valor)

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    Calculadora().run()
