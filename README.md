# Sistema de Calificación de Lociones - Documentación

## Introducción
Este proyecto es un ejercicio académico desarrollado en el marco del curso de Arquitectura de Software, impartido por el profesor Joaquín Sánchez, como parte de la Actividad 3 - Arquitectura Cliente Servidor.

El sistema implementa una aplicación de calificación de lociones utilizando una arquitectura cliente-servidor. Los usuarios pueden agregar lociones, calificarlas y obtener información sobre ellas, mientras que el servidor gestiona toda la lógica y el almacenamiento de datos.

Esta aplicación, aunque diseñada con fines educativos, tiene el potencial de evolucionar hacia una aplicación más completa y robusta en el futuro. Podría servir como base para una plataforma de reseñas de productos de belleza o una herramienta de gestión de inventario para tiendas de perfumería.

## Estructura del Proyecto
El proyecto está organizado en cuatro archivos principales:

1. `main.py`: Archivo principal para ejecutar la aplicación.
2. `servidor.py`: Contiene la lógica del servidor.
3. `cliente.py`: Implementa la funcionalidad del cliente.
4. `locion.py`: Define la clase Locion.

## Clases y Métodos

### Clase `Locion`
La clase `Locion` representa una loción individual en el sistema.

**Atributos:**
- `id`: Identificador único de la loción.
- `nombre`: Nombre de la loción.
- `marca`: Marca de la loción.
- `calificaciones`: Lista de calificaciones recibidas.
- `promedio`: Promedio de las calificaciones.

**Métodos:**
- `__init__(self, id, nombre, marca)`: Constructor de la clase.
- `agregar_calificacion(self, calificacion)`: Agrega una nueva calificación.
- `actualizar_promedio(self)`: Actualiza el promedio de calificaciones.
- `__str__(self)`: Retorna una representación en string de la loción.

### Clase `Servidor`
La clase `Servidor` maneja las solicitudes de los clientes y gestiona los datos de las lociones.

**Atributos:**
- `host`: Dirección del servidor.
- `puerto`: Puerto en el que escucha el servidor.
- `lociones`: Diccionario para almacenar las lociones.

**Métodos:**
- `__init__(self, host='localhost', puerto=12345)`: Constructor de la clase.
- `iniciar(self)`: Inicia el servidor y escucha conexiones.
- `procesar_solicitud(self, data)`: Procesa las solicitudes recibidas.
- `agregar_locion(self, nombre, marca)`: Agrega una nueva loción.
- `calificar_locion(self, id, calificacion)`: Califica una loción existente.
- `obtener_promedio(self, id)`: Obtiene el promedio de una loción.
- `listar_lociones(self)`: Lista todas las lociones.

### Clase `Cliente`
La clase `Cliente` proporciona métodos para interactuar con el servidor.

**Atributos:**
- `host`: Dirección del servidor.
- `puerto`: Puerto del servidor.

**Métodos:**
- `__init__(self, host='localhost', puerto=12345)`: Constructor de la clase.
- `enviar_solicitud(self, solicitud)`: Envía una solicitud al servidor.
- `agregar_locion(self, nombre, marca)`: Solicita agregar una nueva loción.
- `calificar_locion(self, id, calificacion)`: Solicita calificar una loción.
- `obtener_promedio(self, id)`: Solicita el promedio de una loción.
- `listar_lociones(self)`: Solicita la lista de todas las lociones.

## Ejecución del Programa
El archivo `main.py` contiene el código para ejecutar tanto el servidor como el cliente. Inicia el servidor en un hilo separado y luego realiza una serie de operaciones de cliente para demostrar la funcionalidad del sistema.

Para ejecutar el programa, use el siguiente comando en la terminal:

```bash
python main.py
