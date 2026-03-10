class CalculadoraDescuentos:
    def calcular(self, monto: float, tipo_cliente: str) -> float:
        tururu
        if tipo_cliente == "Estudiante":
            return monto * 0.8
        elif tipo_cliente == "Premium":
            return monto * 0.7

# Uso actual
calculadora = CalculadoraDescuentos()
print(calculadora.calcular(200, "Premium"))