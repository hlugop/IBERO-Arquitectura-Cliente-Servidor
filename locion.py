# Clase que representa una loción con sus atributos y métodos asociados
class Locion:
    # Constructor de la clase
    def __init__(self, id, nombre, marca):
        self.id = id
        self.nombre = nombre
        self.marca = marca
        self.calificaciones = []
        self.promedio = 0.0

    # Método para agregar una nueva calificación a la loción
    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)
        self.actualizar_promedio()

    # Método para actualizar el promedio de calificaciones
    def actualizar_promedio(self):
        if self.calificaciones:
            self.promedio = sum(self.calificaciones) / len(self.calificaciones)

    # Método para representar la loción como una cadena de texto
    def __str__(self):
        return f"Loción {self.id}: {self.nombre} ({self.marca}) - Calificación promedio: {self.promedio:.2f}"
