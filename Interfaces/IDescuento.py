from abc import ABC, abstractmethod

# Interfaz
class IDescuento(ABC):
    @abstractmethod
    def aplicar(self, monto: float) -> float: pass

# Extensiones (Nuevas clases, no modificamos las existentes)
class DescuentoEstudiante(IDescuento):
    def aplicar(self, monto: float) -> float:return monto * 0.8
class DescuentoPremium(IDescuento):
    def aplicar(self, monto: float) -> float: return monto * 0.7
class Calculadora:
    # Depende de la abstracción, no de la concreción
    def calcular(self, monto: float, descuento: IDescuento) -> float:
        return descuento.aplicar(monto)

calculadora = Calculadora()
print(calculadora.calcular(200, DescuentoPremium()))