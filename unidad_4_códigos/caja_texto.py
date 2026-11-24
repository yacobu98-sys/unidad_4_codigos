#CAJA DE TEXTO 
#Crea una ventana de Tkinter con una caja de texto, una etiqueta y un boton
# luis yahir cortes burgos

import tkinter as tk

#Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi tercera ventana") # Titulo de la ventana
ventana.geometry("400x300") # Tamaño de la ventana
ventana.configure(bg="lightgray") # Color de fondo de la ventana

escribir_texto = tk.Entry(ventana) # Crea una caja de texto
escribir_texto.pack(padx=10, pady=5) # Publica la caja de texto en la ventana

label = tk.Label(ventana, text = "") # Crea una etiqueta
label.pack(padx=10, pady=5) # Publica la etiqueta en la ventana

boton = tk.Button(ventana, text = "Mostrar texto", command = lambda: label.config(text = escribir_texto.get())) # Crea un boton que al hacer click muestra el texto de la caja de texto en la etiqueta
boton.pack(padx=10, pady=5) # Publica el boton en la ventana

ventana.mainloop() # Mantiene la ventana abierta hasta que el usuario la cierre