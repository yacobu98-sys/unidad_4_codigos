#LUIS YAHIR CORTES BURGOS
import tkinter as tk
from tkinter import messagebox

def guardar_datos():
    nombre = entry_nombre.get().strip()
    edad_texto = entry_edad.get().strip()
    correo = entry_correo.get().strip()

    # Validación 1: Nombre no vacío
    if nombre == "":
        messagebox.showerror("Error", "El nombre no puede estar vacío.")
        return

    # Validación 2: Edad entero entre 1 y 120
    try:
        edad = int(edad_texto)
    except ValueError:
        messagebox.showerror("Error", "La edad debe ser un número entero.")
        return

    if edad < 1 or edad > 120:
        messagebox.showerror("Error", "La edad debe estar entre 1 y 120.")
        return

    # Validación 3: Correo contiene @
    if "@" not in correo:
        messagebox.showerror("Error", "El correo debe contener '@'.")
        return

    # Si todo está bien
    mensaje = f"¡Datos válidos!\nNombre: {nombre}\nEdad: {edad}\nCorreo: {correo}"
    messagebox.showinfo("Éxito", mensaje)


ventana = tk.Tk()
ventana.title("Formulario con Validaciones")

# Fila 0
tk.Label(ventana, text="Nombre").grid(row=0, column=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

# Fila 1
tk.Label(ventana, text="Edad").grid(row=1, column=0)
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1)

# Fila 2
tk.Label(ventana, text="Correo").grid(row=2, column=0)
entry_correo = tk.Entry(ventana)
entry_correo.grid(row=2, column=1)

# Fila 3
tk.Button(ventana, text="Guardar", command=guardar_datos).grid(row=3, column=1)

ventana.mainloop()
