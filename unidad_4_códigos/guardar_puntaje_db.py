import tkinter as tk
from tkinter import messagebox
import db

# Crear la tabla al iniciar
db.crear_tabla()

def boton_guardar():
    nombre = entry_nombre.get().strip()
    puntaje_texto = entry_puntaje.get().strip()

    if nombre == "" or puntaje_texto == "":
        messagebox.showerror("Error", "No dejes campos vacíos")
        return

    try:
        puntaje = int(puntaje_texto)
    except ValueError:
        messagebox.showerror("Error", "El puntaje debe ser un número")
        return

    db.guardar_puntaje(nombre, puntaje)
    messagebox.showinfo("Éxito", "Puntaje guardado correctamente")

ventana = tk.Tk()
ventana.title("Guardar Puntaje SQLite")

tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Puntaje:").grid(row=1, column=0)
entry_puntaje = tk.Entry(ventana)
entry_puntaje.grid(row=1, column=1)

tk.Button(ventana, text="Guardar", command=boton_guardar).grid(row=2, column=1)

ventana.mainloop()