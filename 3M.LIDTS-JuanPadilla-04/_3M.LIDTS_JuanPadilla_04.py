import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Actividad 04 - Formulario Juan Padilla")
ventana.geometry("450x550")
ventana.configure(bg="#e0f3ff")
ventana.resizable(False, False)

rbGenero = tk.StringVar()

def borrar():
    entryNombre.delete(0, tk.END)
    entryApellido.delete(0, tk.END)
    entryEdad.delete(0, tk.END)
    entryEstatura.delete(0, tk.END)
    entryTelefono.delete(0, tk.END)
    rbGenero.set(None)
    entryNombre.focus()

def enviar():
    if (entryNombre.get() == "" or
        entryApellido.get() == "" or
        entryEdad.get() == "" or
        entryEstatura.get() == "" or
        entryTelefono.get() == "" or
        rbGenero.get() == ""):
        
        messagebox.showwarning("Error", "Completa todos los campos")
    else:
        info = (f"Nombre: {entryNombre.get()}\n"
                f"Apellido: {entryApellido.get()}\n"
                f"Edad: {entryEdad.get()}\n"
                f"Estatura: {entryEstatura.get()}\n"
                f"Teléfono: {entryTelefono.get()}\n"
                f"Género: {rbGenero.get()}")
        
        messagebox.showinfo("Datos registrados", info)

contenedor = tk.Frame(ventana, bg="white", padx=25, pady=25)
contenedor.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(contenedor, text="Formulario de Registro", font=("Segoe UI", 16, "bold"), bg="white", fg="#1565C0").grid(row=0, column=0, columnspan=2, pady=(0, 20))

tk.Label(contenedor, text="Nombre:", bg="white").grid(row=1, column=0, sticky="w", pady=5)
entryNombre = tk.Entry(contenedor, width=25)
entryNombre.grid(row=1, column=1, pady=5)

tk.Label(contenedor, text="Apellido:", bg="white").grid(row=2, column=0, sticky="w", pady=5)
entryApellido = tk.Entry(contenedor, width=25)
entryApellido.grid(row=2, column=1, pady=5)

tk.Label(contenedor, text="Edad:", bg="white").grid(row=3, column=0, sticky="w", pady=5)
entryEdad = tk.Entry(contenedor, width=25)
entryEdad.grid(row=3, column=1, pady=5)

tk.Label(contenedor, text="Estatura (m):", bg="white").grid(row=4, column=0, sticky="w", pady=5)
entryEstatura = tk.Entry(contenedor, width=25)
entryEstatura.grid(row=4, column=1, pady=5)

tk.Label(contenedor, text="Teléfono:", bg="white").grid(row=5, column=0, sticky="w", pady=5)
entryTelefono = tk.Entry(contenedor, width=25)
entryTelefono.grid(row=5, column=1, pady=5)

tk.Label(contenedor, text="Género:", bg="white").grid(row=6, column=0, sticky="w", pady=10)
frameGenero = tk.Frame(contenedor, bg="white")
frameGenero.grid(row=6, column=1, pady=10, sticky="w")

tk.Radiobutton(frameGenero, text="Masculino", variable=rbGenero, value="Masculino", bg="white").pack(side="left", padx=5)
tk.Radiobutton(frameGenero, text="Femenino", variable=rbGenero, value="Femenino", bg="white").pack(side="left", padx=5)

btnRegistrar = tk.Button(contenedor, text="Registrar", bg="#1976D2", fg="white", width=12, command=enviar)
btnRegistrar.grid(row=7, column=0, pady=20)

btnBorrar = tk.Button(contenedor, text="Borrar", bg="#f44336", fg="white", width=12, command=borrar)
btnBorrar.grid(row=7, column=1, pady=20)

ventana.mainloop()