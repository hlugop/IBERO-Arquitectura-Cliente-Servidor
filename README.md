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

# Sistema de Calificación de Lociones - Interfaz de Usuario

## Descripción General

El Sistema de Calificación de Lociones es una aplicación de escritorio diseñada para proporcionar una interfaz de usuario intuitiva y fácil de usar para la gestión y calificación de lociones. Esta interfaz está desarrollada utilizando la biblioteca Tkinter de Python, lo que garantiza una experiencia de usuario consistente en diferentes plataformas.

## Mejoras en la Usabilidad

1. **Diseño Simplificado**: La interfaz presenta un diseño minimalista y directo, reduciendo la curva de aprendizaje para nuevos usuarios.

2. **Organización Lógica**: Los elementos de la interfaz están organizados de manera secuencial, siguiendo el flujo natural de las operaciones (agregar, calificar, obtener promedio, listar).

3. **Feedback Inmediato**: Cada acción del usuario genera una respuesta visible en el área de resultados, proporcionando confirmación inmediata de las operaciones realizadas.

4. **Manejo de Errores**: Se implementan mensajes de advertencia para guiar al usuario en caso de entradas incorrectas o campos faltantes.

5. **Flexibilidad**: La interfaz permite realizar múltiples operaciones sin necesidad de navegar entre diferentes ventanas.

## Clase Principal: App

La clase `App` es el componente central de la interfaz de usuario. A continuación, se detallan sus atributos y métodos principales:

### Atributos

- `cliente`: Instancia de la clase `Cliente` para la comunicación con el servidor.
- `master`: Ventana principal de la aplicación (instancia de `tk.Tk`).
- `frame`: Frame principal que contiene todos los widgets.
- `tipos_perfume`: Lista de tipos de perfumes disponibles.
- Varios `Entry` y `StringVar` para la entrada de datos del usuario.
- `resultado_text`: Área de texto para mostrar los resultados de las operaciones.

### Métodos

#### `__init__(self, master)`

Inicializa la aplicación y configura la ventana principal.


