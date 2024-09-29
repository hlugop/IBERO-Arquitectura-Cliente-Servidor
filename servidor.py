import socket
import json
from locion import Locion

# Clase Servidor: Maneja las operaciones del servidor para el sistema de calificación de lociones
class Servidor:
    def __init__(self, host='localhost', puerto=12345):
        """
        Inicializa el servidor con host y puerto especificados.
        
        :param host: Dirección del host del servidor (por defecto 'localhost')
        :param puerto: Número de puerto para el servidor (por defecto 12345)
        """
        self.host = host
        self.puerto = puerto
        self.lociones = {}

    def iniciar(self):
        """
        Inicia el servidor y maneja las conexiones entrantes de los clientes.
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.puerto))
            s.listen()
            print(f"Servidor de calificaciones de lociones escuchando en {self.host}:{self.puerto}")
            
            while True:
                conn, addr = s.accept()
                with conn:
                    print(f"Conexión establecida desde {addr}")
                    data = conn.recv(1024).decode()
                    respuesta = self.procesar_solicitud(data)
                    conn.sendall(respuesta.encode())

    def procesar_solicitud(self, data):
        """
        Procesa la solicitud recibida del cliente y ejecuta la acción correspondiente.
        
        :param data: Datos recibidos del cliente en formato JSON
        :return: Respuesta a la solicitud del cliente
        """
        solicitud = json.loads(data)
        accion = solicitud['accion']
        
        if accion == 'agregar_locion':
            return self.agregar_locion(solicitud['nombre'], solicitud['marca'])
        elif accion == 'calificar':
            return self.calificar_locion(solicitud['id'], solicitud['calificacion'])
        elif accion == 'obtener_promedio':
            return self.obtener_promedio(solicitud['id'])
        elif accion == 'listar_lociones':
            return self.listar_lociones()
        else:
            return "Acción no reconocida"

    def agregar_locion(self, nombre, marca):
        """
        Agrega una nueva loción al sistema.
        
        :param nombre: Nombre de la loción
        :param marca: Marca de la loción
        :return: Mensaje de confirmación
        """
        id = len(self.lociones) + 1
        locion = Locion(id, nombre, marca)
        self.lociones[id] = locion
        return f"Loción agregada: {locion}"

    def calificar_locion(self, id, calificacion):
        """
        Agrega una calificación a una loción existente.
        
        :param id: ID de la loción
        :param calificacion: Calificación a agregar
        :return: Mensaje de confirmación o error
        """
        if id in self.lociones:
            self.lociones[id].agregar_calificacion(calificacion)
            return f"Calificación {calificacion} agregada a la loción {id}"
        return f"Loción {id} no encontrada"

    def obtener_promedio(self, id):
        """
        Obtiene el promedio de calificaciones de una loción.
        
        :param id: ID de la loción
        :return: Promedio de calificaciones o mensaje de error
        """
        if id in self.lociones:
            return f"Promedio de la loción {id}: {self.lociones[id].promedio:.2f}"
        return f"Loción {id} no encontrada"

    def listar_lociones(self):
        """
        Lista todas las lociones en el sistema.
        
        :return: Lista de lociones como cadena de texto
        """
        return "\n".join(str(locion) for locion in self.lociones.values())
