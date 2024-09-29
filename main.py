# Importamos los módulos necesarios
import threading
from servidor import Servidor  # Importamos la clase Servidor del archivo servidor.py
from cliente import Cliente    # Importamos la clase Cliente del archivo cliente.py
import time

def iniciar_servidor():
    # Función para iniciar el servidor
    servidor = Servidor()  # Creamos una instancia de la clase Servidor
    servidor.iniciar()     # Iniciamos el servidor

def ejecutar_cliente():
    # Función para ejecutar las operaciones del cliente
    cliente = Cliente()  # Creamos una instancia de la clase Cliente
    
    print("Agregando lociones:")
    # Agregamos varias lociones utilizando el método agregar_locion del cliente
    print(cliente.agregar_locion("Eau de Parfum", "Chanel"))
    print(cliente.agregar_locion("Cologne", "Hugo Boss"))
    print(cliente.agregar_locion("Eau de Toilette", "Dior"))
    
    print("\nCalificando lociones:")
    # Calificamos las lociones utilizando el método calificar_locion del cliente
    print(cliente.calificar_locion(1, 4.5))
    print(cliente.calificar_locion(1, 5.0))
    print(cliente.calificar_locion(2, 3.5))
    print(cliente.calificar_locion(2, 4.0))
    print(cliente.calificar_locion(3, 4.8))
    
    print("\nObteniendo promedios:")
    # Obtenemos los promedios de calificación utilizando el método obtener_promedio del cliente
    print(cliente.obtener_promedio(1))
    print(cliente.obtener_promedio(2))
    print(cliente.obtener_promedio(3))
    
    print("\nListando todas las lociones:")
    # Listamos todas las lociones utilizando el método listar_lociones del cliente
    print(cliente.listar_lociones())

if __name__ == "__main__":
    # Iniciamos el servidor en un hilo separado
    hilo_servidor = threading.Thread(target=iniciar_servidor)
    hilo_servidor.start()
    
    # Esperamos un momento para asegurarnos de que el servidor esté listo
    time.sleep(1)
    
    # Ejecutamos las operaciones del cliente
    ejecutar_cliente()
    
    # Nota: En un escenario real, podriamos querer mantener el servidor
    # en ejecución y no terminarlo automáticamente. Aquí lo dejamos correr
    # indefinidamente.
    # El servidor utiliza la clase Locion del archivo locion.py para manejar los objetos Locion
