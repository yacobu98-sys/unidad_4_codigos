#ETIQUETA BOTON
# CREAE UNA VENTANA DE TKINTER CON UNA ETIQUETA Y UN BOTON
# luis yahir cortes burgos

import tkinter as tk

#Crea una ventana de Tkinter 
ventana = tk.Tk()
ventana.title("Mi segunda ventana") # Titulo de la ventana
ventana.geometry("400x300") # Tamaño de la ventana
ventana.configure (bg="lightgray") # Color de fondo de la ventana

def cambia_texto ():
    label.config (text = "¿Que dice el hombre?") # Cambia el texto de la etiqueta cuando se hace click en el boton

label = tk.Label (ventana, text = "Haz click en el boton ")
label.pack () # Publica la etiqueta en la ventana

boton = tk.Button (ventana, text = "Saludar", command = cambia_texto)
boton.pack () # Publica el boton en la ventana

ventana.mainloop() # Mantiene la ventana abierta hasta que el usuario la cierre