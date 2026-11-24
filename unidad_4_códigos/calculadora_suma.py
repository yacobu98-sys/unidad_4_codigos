#LUIS YAHIR CORTES BURGOS

import tkinter as tk
def sumar():
    try:
        # Intentamos convertir los valores a float
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        # Si ocurre un error de conversión, mostramos un mensaje de error
        label_resultado.config(text="Error: Por favor ingresa números válidos")
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de suma")
# Crear los elementos de la interfaz
entry_num1 = tk.Entry(ventana, width=15)
entry_num1.grid(row=0, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(ventana, width=15)
entry_num2.grid(row=0, column=1, padx=5, pady=5)
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.grid(row=0, column=2, padx=5, pady=5)
label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.grid(row=1, column=0, columnspan=3, pady=10)
# Ejecutar el ciclo principal de la ventana
ventana.mainloop()