#5.2 Ejercicios Propuestos para el Estudiante


"""
Modelar una jerarquía donde exista la clase base `TarjetaCredito` y subclases `TarjetaGold` y
`TarjetaBlack`. Aplique polimorfismo en el método `calcular_cashback(monto)` de modo que la tarjeta
Gold retorne el 2% y la Black retorne el 5% de las compras realizadas.
"""

from tarjeta_credito import TarjetaCredito

class TarjetaGold(TarjetaCredito):
    def __init__(self, numero: str):
        super().__init__(numero, "gold")
        self.porcentaje_cashback = 0.02

    #metodos
    def calcular_cashback(self, monto: float):
        return monto * self.porcentaje_cashback

class TarjetaBlack(TarjetaCredito):
    def __init__(self, numero: str):
        super().__init__(numero, "black")
        self.porcentaje_cashback = 0.05

    #metodos
    def calcular_cashback(self, monto: float):
        return monto * self.porcentaje_cashback


tarjeta_gold = TarjetaGold("123")
cashback_gold = tarjeta_gold.calcular_cashback(1000)
print(f"Tarjeta {tarjeta_gold.tipo_tarjeta.capitalize()} ({tarjeta_gold.numero}): Cashback = ${cashback_gold}")


tarjeta_black = TarjetaBlack("456")
cashback_black = tarjeta_black.calcular_cashback(1000)
print(f"Tarjeta {tarjeta_black.tipo_tarjeta.capitalize()} ({tarjeta_black.numero}): Cashback = ${cashback_black}")