#VENTANA_BASICA
# Abir una ventana de Tkinter con un titulo, tamaño y color de fondo especificados
# Luis Yahir Cortes Burgos
import sqlite3
import tkinter as tk
#Crea una ventana de Tkinter 
ventana = tk.Tk()
ventana.title("Mi primera ventana") # Titulo de la ventana
ventana.geometry("400x300")# Tamaño de la ventana
ventana.configure (bg="lightgray")# Color de fondo de la ventana
ventana.mainloop() # Mantiene la ventana abierta hasta que el usuario la cierre