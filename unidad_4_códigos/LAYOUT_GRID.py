#LAYOUT_GRID
#GUARDAR INFORMACION 
#Luis Yahir Cortes Burgos

import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario")
ventana.geometry("400x300")
ventana.configure(bg="lightgray")

etiqueta_nombre = tk.Label(ventana, text="Nombre:", bg="lightgray")
etiqueta_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0, column=1, padx=10, pady=10)

etiqueta_edad = tk.Label(ventana, text="Edad:", bg="lightgray")
etiqueta_edad.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entrada_edad = tk.Entry(ventana)
entrada_edad.grid(row=1, column=1, padx=10, pady=10)

etiqueta_correo = tk.Label(ventana, text="Correo:", bg="lightgray")
etiqueta_correo.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entrada_correo = tk.Entry(ventana)
entrada_correo.grid(row=2, column=1, padx=10, pady=10)

# Guardar la informacion
boton_guardar = tk.Button(ventana, text="Guardar", command=lambda: messagebox.showinfo("Informacion", f"Nombre: {entrada_nombre.get()}\nEdad: {entrada_edad.get()}\nCorreo: {entrada_correo.get()}"))
boton_guardar.grid(row=3, column=1, padx=10, pady=10)

ventana.mainloop()