#LISTBOX_PREGUNTAS
#CREAMOS UNA LISTA DE PREGUNTAS CON INTERFAZ GRAFICA
#Luis Yahir Cortes Burgos

import tkinter as tk

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Preguntas")
ventana.geometry("400x300")
ventana.configure(bg="lightblue")

lista = tk.Listbox(ventana, width=40, height=8)
lista.pack(pady=10)

def preguntas():
    preguntas = [
        "¿Capital de Francia?",
        "¿Capital de España?",
        "¿2+2?",
        "¿Año de la independencia de México?",
        "¿Capital de Italia?"
    ]
    return preguntas

# Agregamos las preguntas a la lista
for pregunta in preguntas():
    lista.insert(tk.END, pregunta)

etiqueta = tk.Label(ventana, text="Selecciona una pregunta de la lista", bg="lightblue", font=("Arial", 12))
etiqueta.pack(pady=10)

def mostrar_seleccion(evento):
    seleccion = lista.curselection()
    if seleccion:
        pregunta_seleccionada = lista.get(seleccion[0])
        etiqueta.config(text=f"Pregunta seleccionada: {pregunta_seleccionada}")
    else:
        etiqueta.config(text="No se ha seleccionado ninguna pregunta")

lista.bind("<<ListboxSelect>>", mostrar_seleccion)

ventana.mainloop()