#VENTANA PREGUNTA
#
#Luis YAHIR 

import tkinter as tk
from tkinter import messagebox
from PREGUNTA_VF import PreguntaVF

def mostrar_pregunta_en_gui(pregunta):
    #Creamos una ventana para mostrar la pregunta
    ventana = tk.Toplevel()
    ventana.title("Pregunta")
    ventana.geometry("400x300")

    #Creamos una etiqueta para mostrar la pregunta
    etiqueta_pregunta = tk.Label(ventana, text=pregunta.texto, wraplength=350)
    etiqueta_pregunta.pack(pady=20)

    #Guardamos la respuesta del usuario en una variable de tipo StringVar
    respuesta = tk.StringVar()

    #Creamos dos botones con Radiobutton para seleccionar la respuesta
    boton_verdadero = tk.Radiobutton(ventana, text="Verdadero", variable=respuesta, value="V")
    boton_verdadero.pack(side=tk.LEFT, padx=20)

    boton_falso = tk.Radiobutton(ventana, text="Falso", variable=respuesta, value="F")
    boton_falso.pack(side=tk.RIGHT, padx=20)

    #Creamos una funcion para verificar la respuesta
    def verificar_respuesta():
        seleccion = respuesta.get()

        if seleccion == "":
            messagebox.showwarning("Aviso", "Selecciona una respuesta")
        elif pregunta.esta_correcto(seleccion):
            messagebox.showinfo("Resultado", "¡Respuesta correcta!")
        else:
            messagebox.showinfo("Resultado", "Respuesta incorrecta")

    #Creamos un boton para responder
    boton_responder = tk.Button(ventana, text="Responder", command=verificar_respuesta)
    boton_responder.pack(pady=30)

#Creamos la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Menu de preguntas")
ventana_principal.geometry("300x200")

#Creamos una pregunta
pregunta = PreguntaVF("El sol es una estrella", True)

#Mostramos la pregunta en una ventana secundaria
mostrar_pregunta_en_gui(pregunta)

#Mantenemos la ventana abierta
ventana_principal.mainloop()