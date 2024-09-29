import socket
import json

class Cliente:
    """
    Clase Cliente para interactuar con el servidor de la aplicación de lociones.
    Maneja la comunicación y las operaciones relacionadas con las lociones.
    """

    def __init__(self, host='localhost', puerto=12345):
        """
        Inicializa un cliente con la dirección del host y el puerto especificados.
        
        :param host: Dirección del servidor (por defecto 'localhost')
        :param puerto: Número de puerto para la conexión (por defecto 12345)
        """
        self.host = host
        self.puerto = puerto

    def enviar_solicitud(self, solicitud):
        """
        Envía una solicitud al servidor y recibe la respuesta.
        
        :param solicitud: Diccionario con la información de la solicitud
        :return: Respuesta del servidor como string
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.puerto))
            s.sendall(json.dumps(solicitud).encode())
            return s.recv(1024).decode()

    def agregar_locion(self, nombre, marca):
        """
        Envía una solicitud para agregar una nueva loción.
        
        :param nombre: Nombre de la loción
        :param marca: Marca de la loción
        :return: Respuesta del servidor
        """
        solicitud = {'accion': 'agregar_locion', 'nombre': nombre, 'marca': marca}
        return self.enviar_solicitud(solicitud)

    def calificar_locion(self, id, calificacion):
        """
        Envía una solicitud para calificar una loción existente.
        
        :param id: ID de la loción a calificar
        :param calificacion: Calificación a asignar
        :return: Respuesta del servidor
        """
        solicitud = {'accion': 'calificar', 'id': id, 'calificacion': calificacion}
        return self.enviar_solicitud(solicitud)

    def obtener_promedio(self, id):
        """
        Solicita el promedio de calificaciones para una loción específica.
        
        :param id: ID de la loción
        :return: Promedio de calificaciones de la loción
        """
        solicitud = {'accion': 'obtener_promedio', 'id': id}
        return self.enviar_solicitud(solicitud)

    def listar_lociones(self):
        """
        Solicita la lista de todas las lociones disponibles.
        
        :return: Lista de lociones del servidor
        """
        solicitud = {'accion': 'listar_lociones'}
        return self.enviar_solicitud(solicitud)
