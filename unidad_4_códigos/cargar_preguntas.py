#LUIS YAHIR CORTES BURGOS
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json

def cargar_preguntas():
    ruta_archivo = filedialog.askopenfilename(
        title="Seleccionar archivo JSON",
        filetypes=[("Archivos JSON", "*.json")]
    )
    if not ruta_archivo:
        return

    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)

        # Limpiar el Treeview antes de cargar nuevos datos
        for item in tree.get_children():
            tree.delete(item)

        # Insertar cada pregunta
        for pregunta in datos:
            texto = pregunta.get("Texto", "")
            dificultad = pregunta.get("Dificultad", "")
            tipo = pregunta.get("Tipo", "")
            tree.insert("", "end", values=(texto, dificultad, tipo))

    except json.JSONDecodeError:
        messagebox.showerror("Error", "El archivo no es un JSON válido.")
    except Exception as e:
        messagebox.showerror("Error", f"Formato incorrecto: {str(e)}")


ventana = tk.Tk()
ventana.title("Cargar Preguntas JSON")

# Botón
tk.Button(ventana, text="Cargar Preguntas", command=cargar_preguntas).pack(pady=10)

# Treeview
columnas = ("texto", "dificultad", "tipo")
tree = ttk.Treeview(ventana, columns=columnas, show="headings")

tree.heading("texto", text="Texto")
tree.heading("dificultad", text="Dificultad")
tree.heading("tipo", text="Tipo")

tree.column("texto", width=250)
tree.column("dificultad", width=100)
tree.column("tipo", width=100)

tree.pack(fill="both", expand=True, padx=5, pady=5)

ventana.mainloop()