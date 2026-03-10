# EL PROBLEMA: Si queremos agregar WhatsApp, tenemos que modificar esta clase (Violando OCP).
class Notificador:
    def enviar(self, mensaje: str, tipo: str):
        if tipo == "Email":
            print(f"Enviando Email: {mensaje}")
        elif tipo == "SMS":
            print(f"Enviando SMS: {mensaje}")
        else:
            print("Tipo de notificación no soportado")

# Uso actual
notificador = Notificador()
notificador.enviar("Hola, tu pedido ha sido enviado.", "Email")