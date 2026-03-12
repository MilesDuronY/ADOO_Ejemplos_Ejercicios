# EL PROBLEMA: Si queremos agregar un nuevo tipo de envío,
# tenemos que modificar esta clase (Violando OCP).

class CotizadorEnvio:
    def cotizar(
        self,
        peso: float,
        distancia_km: float,
        tipo_envio: str,
        es_fragil: bool,
        requiere_seguro: bool
    ) -> dict:

        if tipo_envio == "Estandar":
            tarifa_base = 40
            costo_por_kg = 5
            costo_por_km = 0.8
            dias_estimados = 5

        elif tipo_envio == "Express":
            tarifa_base = 80
            costo_por_kg = 8
            costo_por_km = 1.2
            dias_estimados = 2

        elif tipo_envio == "Internacional":
            tarifa_base = 200
            costo_por_kg = 12
            costo_por_km = 2.5
            dias_estimados = 10

        else:
            return {
                "error": "Tipo de envío no soportado"
            }

        subtotal = tarifa_base + (peso * costo_por_kg) + (distancia_km * costo_por_km)
        recargo_fragil = subtotal * 0.10 if es_fragil else 0
        costo_seguro = subtotal * 0.05 if requiere_seguro else 0
        total = subtotal + recargo_fragil + costo_seguro

        return {
            "tipo_envio": tipo_envio,
            "subtotal": subtotal,
            "recargo_fragil": recargo_fragil,
            "costo_seguro": costo_seguro,
            "total": total,
            "dias_estimados": dias_estimados
        }


# Uso actual
cotizador = CotizadorEnvio()
resultado = cotizador.cotizar(
    peso=12,
    distancia_km=150,
    tipo_envio="Express",
    es_fragil=True,
    requiere_seguro=True
)

print(resultado)