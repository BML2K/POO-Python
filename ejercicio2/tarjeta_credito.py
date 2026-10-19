#5.2 Ejercicios Propuestos para el Estudiante


"""
Modelar una jerarquía donde exista la clase base `TarjetaCredito` y subclases `TarjetaGold` y
`TarjetaBlack`. Aplique polimorfismo en el método `calcular_cashback(monto)` de modo que la tarjeta
Gold retorne el 2% y la Black retorne el 5% de las compras realizadas.
"""

class TarjetaCredito:
    def __init__(self, numero: str, tipo_tarjeta: str):
        self.numero = numero
        self.tipo_tarjeta = tipo_tarjeta

    #metodos
    def calcular_cashback(self, monto: float):
        pass