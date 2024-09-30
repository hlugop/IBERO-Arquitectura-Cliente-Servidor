import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import sys
import tkinter as tk
from tkinter import messagebox
from cliente import Cliente
from servidor import Servidor
import threading
import time

class App:
    """
    Clase que representa la interfaz gráfica de usuario para el Sistema de Calificación de Lociones.
    
    Esta clase implementa una aplicación de escritorio que permite a los usuarios interactuar
    con un sistema de calificación de lociones. La interfaz está diseñada para ser simple y
    fácil de usar, con características orientadas al cliente.

    Atributos:
        cliente (Cliente): Instancia de la clase Cliente para comunicarse con el servidor.
        master (tk.Tk): Ventana principal de la aplicación.
        frame (tk.Frame): Frame principal que contiene todos los widgets.
        tipos_perfume (list): Lista de tipos de perfumes disponibles.
        nombre_entry (tk.Entry): Campo de entrada para el nombre de la loción.
        marca_entry (tk.Entry): Campo de entrada para la marca de la loción.
        tipo_combobox (tk.StringVar): Variable para almacenar el tipo de perfume seleccionado.
        id_entry (tk.Entry): Campo de entrada para el ID de la loción.
        calificacion_entry (tk.Entry): Campo de entrada para la calificación.
        promedio_id_entry (tk.Entry): Campo de entrada para el ID al obtener el promedio.
        resultado_text (tk.Text): Área de texto para mostrar resultados.

    Métodos:
        crear_widgets(): Crea y configura todos los widgets de la interfaz.
        agregar_locion(): Maneja la acción de agregar una nueva loción.
        calificar_locion(): Maneja la acción de calificar una loción existente.
        obtener_promedio(): Maneja la acción de obtener el promedio de calificaciones de una loción.
        listar_lociones(): Maneja la acción de listar todas las lociones.
    """

    def __init__(self, master):
        """
        Inicializa la aplicación.

        Args:
            master (tk.Tk): Ventana principal de la aplicación.
        """
        self.cliente = Cliente()
        self.master = master
        master.title("Sistema de Calificación de Lociones")
        master.geometry("400x600")

        self.frame = tk.Frame(master)
        self.frame.pack(expand=True, fill=tk.BOTH)

        self.tipos_perfume = [
            "Parfum (Perfume)",
            "Eau de Parfum (EDP)",
            "Eau de Toilette (EDT)",
            "Eau de Cologne (EDC)",
            "Eau Fraiche"
        ]

        self.crear_widgets()

    def crear_widgets(self):
        """
        Crea y configura todos los widgets de la interfaz.

        Este método configura la disposición de los elementos en la interfaz,
        incluyendo etiquetas, campos de entrada, botones y área de resultados.
        """
        # Agregar loción
        tk.Label(self.frame, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self.frame)
        self.nombre_entry.pack()

        tk.Label(self.frame, text="Marca:").pack()
        self.marca_entry = tk.Entry(self.frame)
        self.marca_entry.pack()

        tk.Label(self.frame, text="Tipo:").pack()
        self.tipo_combobox = tk.StringVar(self.frame)
        self.tipo_combobox.set(self.tipos_perfume[0])
        tk.OptionMenu(self.frame, self.tipo_combobox, *self.tipos_perfume).pack()

        tk.Button(self.frame, text="Agregar", command=self.agregar_locion).pack()

        # Calificar loción
        tk.Label(self.frame, text="ID:").pack()
        self.id_entry = tk.Entry(self.frame)
        self.id_entry.pack()

        tk.Label(self.frame, text="Calificación:").pack()
        self.calificacion_entry = tk.Entry(self.frame)
        self.calificacion_entry.pack()

        tk.Button(self.frame, text="Calificar", command=self.calificar_locion).pack()

        # Obtener promedio
        tk.Label(self.frame, text="ID para promedio:").pack()
        self.promedio_id_entry = tk.Entry(self.frame)
        self.promedio_id_entry.pack()

        tk.Button(self.frame, text="Obtener Promedio", command=self.obtener_promedio).pack()

        # Listar lociones
        tk.Button(self.frame, text="Listar Lociones", command=self.listar_lociones).pack()

        # Área de texto para mostrar resultados
        self.resultado_text = tk.Text(self.frame, height=10, width=50)
        self.resultado_text.pack()

    def agregar_locion(self):
        """
        Maneja la acción de agregar una nueva loción.

        Recoge los datos ingresados por el usuario y los envía al servidor
        a través del cliente para agregar una nueva loción al sistema.
        """
        nombre = self.nombre_entry.get()
        marca = self.marca_entry.get()
        tipo = self.tipo_combobox.get()
        if nombre and marca and tipo:
            resultado = self.cliente.agregar_locion(f"{nombre} ({tipo})", marca)
            self.resultado_text.insert(tk.END, resultado + "\n")
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def calificar_locion(self):
        """
        Maneja la acción de calificar una loción existente.

        Recoge el ID de la loción y la calificación ingresados por el usuario
        y los envía al servidor a través del cliente para actualizar la calificación.
        """
        id = self.id_entry.get()
        calificacion = self.calificacion_entry.get()
        if id and calificacion:
            try:
                id = int(id)
                calificacion = float(calificacion)
                resultado = self.cliente.calificar_locion(id, calificacion)
                self.resultado_text.insert(tk.END, resultado + "\n")
            except ValueError:
                messagebox.showwarning("Advertencia", "Por favor, ingrese un ID y una calificación válidos.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese ID y calificación.")

    def obtener_promedio(self):
        """
        Maneja la acción de obtener el promedio de calificaciones de una loción.

        Recoge el ID de la loción ingresado por el usuario y solicita al servidor
        el promedio de calificaciones a través del cliente.
        """
        id = self.promedio_id_entry.get()
        if id:
            try:
                id = int(id)
                resultado = self.cliente.obtener_promedio(id)
                self.resultado_text.insert(tk.END, resultado + "\n")
            except ValueError:
                messagebox.showwarning("Advertencia", "Por favor, ingrese un ID válido.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese ID.")

    def listar_lociones(self):
        """
        Maneja la acción de listar todas las lociones.

        Solicita al servidor la lista de todas las lociones registradas
        y las muestra en el área de resultados.
        """
        resultado = self.cliente.listar_lociones()
        self.resultado_text.insert(tk.END, resultado + "\n")

def iniciar_servidor():
    servidor = Servidor()
    servidor.iniciar()

if __name__ == "__main__":
    # Iniciar el servidor en un hilo separado
    hilo_servidor = threading.Thread(target=iniciar_servidor)
    hilo_servidor.daemon = True
    hilo_servidor.start()

    # Esperar un momento para asegurarse de que el servidor esté listo
    time.sleep(1)

    # Iniciar la interfaz gráfica
    root = tk.Tk()
    app = App(root)
    print("Justo antes de mainloop")
    root.mainloop()
    print("Después de mainloop")