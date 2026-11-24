# LUIS YAHIR CORTES BURGOS
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

#  CLASE PREGUNTA 
class Pregunta:
    def __init__(self, texto, opciones, respuesta_correcta, tipo):
        self.texto = texto
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta
        self.tipo = tipo

#  CLASE BASE DE DATOS 
class BaseDatos:
    def __init__(self, nombre_db="puntajes.db"):
        self.conn = sqlite3.connect(nombre_db)
        self.crear_tabla()

    def crear_tabla(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS jugadores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                puntaje INTEGER
            )
        """)
        self.conn.commit()

    def guardar_puntaje(self, nombre, puntaje):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO jugadores(nombre, puntaje) VALUES (?, ?)", (nombre, puntaje))
        self.conn.commit()

    def obtener_top5(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT nombre, puntaje FROM jugadores ORDER BY puntaje DESC LIMIT 5")
        return cursor.fetchall()

    def cerrar(self):
        self.conn.close()

#  CLASE VENTANA PRINCIPAL
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game Completo")
        self.db = BaseDatos()

        # Variables del juego
        self.puntaje = 0
        self.indice_pregunta = 0
        self.lista_preguntas = [
            Pregunta("¿Cuánto es 2+2?", ["3", "4", "5"], "4", "multiple"),
            Pregunta("Python es un lenguaje interpretado", ["Verdadero", "Falso"], "Verdadero", "vf"),
            Pregunta("¿Qué significa GUI?", ["Interfaz gráfica", "Base de datos"], "Interfaz gráfica", "multiple")
        ]
        self.respuesta_seleccionada = tk.StringVar()

        # Crear menú superior
        menu_principal = tk.Menu(self.root)
        menu_principal.add_command(label="Inicio", command=self.mostrar_inicio)
        menu_principal.add_command(label="Jugar", command=self.mostrar_jugar)
        menu_principal.add_command(label="Ranking", command=self.mostrar_ranking)
        menu_principal.add_command(label="Salir", command=self.root.quit)
        self.root.config(menu=menu_principal)

        # Frame principal
        self.frame_principal = tk.Frame(self.root)
        self.frame_principal.pack(fill="both", expand=True)

        self.mostrar_inicio()

    def limpiar_frame(self):
        # Borrar todos los widgets del frame
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

    def mostrar_inicio(self):
        self.limpiar_frame()
        tk.Label(self.frame_principal, text="🎮 Quiz Game", font=("Arial", 24)).pack(pady=30)
        tk.Button(self.frame_principal, text="Comenzar", font=("Arial",16), command=self.mostrar_jugar).pack(pady=10)

    def mostrar_jugar(self):
        self.limpiar_frame()
        self.puntaje = 0
        self.indice_pregunta = 0
        self.siguiente_pregunta()

    def siguiente_pregunta(self):
        self.limpiar_frame()
        if self.indice_pregunta >= len(self.lista_preguntas):
            # Terminar juego, guardar puntaje
            nombre = tk.simpledialog.askstring("Fin del juego", f"Tu puntaje: {self.puntaje}\nIngresa tu nombre:")
            if nombre:
                self.db.guardar_puntaje(nombre, self.puntaje)
            messagebox.showinfo("Fin", f"Juego terminado!\nPuntaje: {self.puntaje}")
            self.mostrar_inicio()
            return

        preg = self.lista_preguntas[self.indice_pregunta]
        tk.Label(self.frame_principal, text=f"Puntaje: {self.puntaje}", font=("Arial",14)).pack()
        tk.Label(self.frame_principal, text=preg.texto, font=("Arial",16), wraplength=400).pack(pady=15)

        # Mostrar opciones
        self.respuesta_seleccionada.set("")
        for opcion in preg.opciones:
            tk.Radiobutton(self.frame_principal, text=opcion, variable=self.respuesta_seleccionada, value=opcion, font=("Arial",12)).pack(anchor="w", padx=40)

        tk.Button(self.frame_principal, text="Responder", command=self.verificar_respuesta, font=("Arial",14)).pack(pady=15)

    def verificar_respuesta(self):
        preg = self.lista_preguntas[self.indice_pregunta]
        elegida = self.respuesta_seleccionada.get()
        if elegida == "":
            messagebox.showwarning("Aviso", "Selecciona una respuesta")
            return

        if elegida == preg.respuesta_correcta:
            self.puntaje += 10
        self.indice_pregunta += 1
        self.siguiente_pregunta()

    def mostrar_ranking(self):
        self.limpiar_frame()
        tk.Label(self.frame_principal, text="🏆 Top 5 Jugadores", font=("Arial",18)).pack(pady=10)

        columnas = ("nombre", "puntaje")
        tree = ttk.Treeview(self.frame_principal, columns=columnas, show="headings")
        tree.heading("nombre", text="Jugador")
        tree.heading("puntaje", text="Puntaje")
        tree.column("nombre", width=180)
        tree.column("puntaje", width=100)

        top5 = self.db.obtener_top5()
        for fila in top5:
            tree.insert("", "end", values=fila)

        tree.pack(fill="both", expand=True, padx=10, pady=10)

#  EJECUCIÓN 
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.geometry("500x400")
    root.mainloop()