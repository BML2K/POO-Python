#5.2 Ejercicios Propuestos para el Estudiante


"""
EJERCICIO PROPUESTO 1 — NIVEL COMPRENSIÓN
Sistema de Calificaciones Académicas
Cree una clase `Estudiante` con los atributos privados ` nombre` y ` notas` (lista). Implemente
métodos para agregar notas, calcular el promedio de calificaciones e impedir que se registren valores
negativos o superiores a 5.0
"""

class Estudiante:
    def __init__(self, nombre: str, notas: list = None):
        self.__nombre = nombre
        self.__notas = []
        if notas is not None:
            for n in notas:
                if 0.0 <= n <= 5.0:
                    self.__notas.append(n)

    # Métodos
    def agregar_nota(self, nota: float):
        if 0.0 <= nota <= 5.0:
            self.__notas.append(nota)
            print(f"Nota {nota} agregada correctamente para {self.__nombre}.")
        else:
            print(f"Error: La nota {nota} no es válida. Debe estar entre 0.0 y 5.0.")

    # Promedio
    def calcular_promedio(self) -> float:
        if not self.__notas:
            return 0.0
        return sum(self.__notas) / len(self.__notas)

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def notas(self) -> list:
        return self.__notas.copy()


# --- PRUEBAS DEL SISTEMA ---

# Crear una instancia del estudiante
estudiante1 = Estudiante("Sofía Pérez")

# Intentar agregar notas válidas e inválidas
estudiante1.agregar_nota(4.5)
estudiante1.agregar_nota(3.8)
estudiante1.agregar_nota(-1.5)  # Será rechazada correctamente
estudiante1.agregar_nota(6.0)   # Corregido: llamando al método correctamente
estudiante1.agregar_nota(5.0)

# Mostrar el promedio final
promedio = estudiante1.calcular_promedio()
print(f"El promedio final de {estudiante1.nombre} es: {promedio:.2f}")
print(f"Lista de notas registradas: {estudiante1.notas}")