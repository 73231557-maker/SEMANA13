import tkinter as tk
from tkinter import messagebox
import re

class FormularioRegistro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Registro de Usuario")
        self.root.geometry("500x600")

        # Variables de los campos
        self.nombre = tk.StringVar()
        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.confirm_pass = tk.StringVar()
        self.edad = tk.StringVar()
        self.genero = tk.StringVar(value="")
        self.acepto = tk.BooleanVar()

        self.crear_widgets()

    def crear_widgets(self):
        # Frame principal con padding
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(fill="both", expand=True)

        # Título
        tk.Label(
            frame, text="Registro de Usuario",
            font=("Arial", 16, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=(0, 15))

        # Campos de texto
        campos = [
            ("Nombre completo:", self.nombre, False),
            ("Email:", self.email, False),
            ("Contraseña:", self.password, True),
            ("Confirmar contraseña:", self.confirm_pass, True),
            ("Edad:", self.edad, False),
        ]

        for i, (label, var, oculto) in enumerate(campos):
            tk.Label(frame, text=label, anchor="e").grid(
                row=i+1, column=0, sticky="e", pady=5, padx=(0,10)
            )
            entry = tk.Entry(
                frame, textvariable=var, width=35,
                show="*" if oculto else ""
            )
            entry.grid(row=i+1, column=1, pady=5, sticky="w")
#Paso 3: Agregar radio buttons, checkbox y botones
        # Género (radio buttons)
        tk.Label(frame, text="Género:").grid(
            row=6, column=0, sticky="e", pady=5
        )
        genero_frame = tk.Frame(frame)
        genero_frame.grid(row=6, column=1, sticky="w")
        for opcion in ["Masculino", "Femenino", "Otro"]:
            tk.Radiobutton(
                genero_frame, text=opcion,
                variable=self.genero, value=opcion
            ).pack(side="left", padx=5)

        # Checkbox de términos
        tk.Checkbutton(
            frame, text="Acepto los términos y condiciones",
            variable=self.acepto
        ).grid(row=7, column=0, columnspan=2, pady=10)

        # Botones
        btn_frame = tk.Frame(frame)
        btn_frame.grid(row=8, column=0, columnspan=2, pady=15)
        tk.Button(
            btn_frame, text="Registrar",
            command=self.validar, width=15,
            bg="#4CAF50", fg="white"
        ).pack(side="left", padx=10)
        tk.Button(
            btn_frame, text="Limpiar",
            command=self.limpiar, width=15
        ).pack(side="left", padx=10)
#Paso 4: Implementar la validación
    def validar(self):
        errores = []

        # Nombre obligatorio
        if not self.nombre.get().strip():
            errores.append("El nombre es obligatorio")

        # Email con formato válido
        email = self.email.get().strip()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errores.append("Email inválido (debe contener @ y dominio)")

        # Contraseña mínimo 8 caracteres
        if len(self.password.get()) < 8:
            errores.append("La contraseña debe tener mínimo 8 caracteres")

        # Contraseñas coinciden
        if self.password.get() != self.confirm_pass.get():
            errores.append("Las contraseñas no coinciden")

        # Edad válida
        try:
            edad = int(self.edad.get())
            if edad < 15 or edad > 99:
                errores.append("La edad debe estar entre 15 y 99")
        except ValueError:
            errores.append("La edad debe ser un número")

        # Género seleccionado
        if not self.genero.get():
            errores.append("Seleccione un género")

        # Términos aceptados
        if not self.acepto.get():
            errores.append("Debe aceptar los términos")

        if errores:
            messagebox.showerror(
                "Errores de validación",
                "\n".join(f"• {e}" for e in errores)
            )
        else:
            messagebox.showinfo(
                "Registro exitoso",
                f"¡Bienvenido {self.nombre.get()}!\n"
                f"Email: {self.email.get()}"
            )

    def limpiar(self):
        for var in [self.nombre, self.email, self.password,
                    self.confirm_pass, self.edad, self.genero]:
            var.set("")
        self.acepto.set(False)

if __name__ == "__main__":
    app = FormularioRegistro()
    app.root.mainloop()
