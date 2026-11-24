#LUIS YAHIR CORTES BURGOS
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Ranking Treeview")

# Definir columnas
columnas = ("posicion", "jugador", "puntaje")
tree = ttk.Treeview(ventana, columns=columnas, show="headings")

# Encabezados
tree.heading("posicion", text="Posición")
tree.heading("jugador", text="Jugador")
tree.heading("puntaje", text="Puntaje")

# Ajustar tamaño de columnas
tree.column("posicion", width=80)
tree.column("jugador", width=150)
tree.column("puntaje", width=100)

# Insertar 5 registros de ejemplo
tree.insert("", "end", values=(1, "Carlos", 950))
tree.insert("", "end", values=(2, "Ana", 890))
tree.insert("", "end", values=(3, "Luis", 820))
tree.insert("", "end", values=(4, "María", 760))
tree.insert("", "end", values=(5, "Jorge", 710))

# Hacer que el Treeview se ajuste a la ventana
tree.pack(fill="both", expand=True)

ventana.mainloop()