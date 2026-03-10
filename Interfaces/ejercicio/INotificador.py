# 1. Creamos la abstracción (Interfaz)
# - INotificador
# 2. Implementaciones concretas
# - NotificadorEmail
# - NotificadorSMS
# 3. Nueva funcionalida
# - NotificadorWhatsApp
class GestorNotificaciones:
    def __init__(self, notificador: INotificador):
        self.notificador = notificador

    def notificar_usuario(self, mensaje: str):
        self.notificador.enviar(mensaje)


# Uso
gestor = GestorNotificaciones(NotificadorWhatsApp())
gestor.notificar_usuario("Hola, tu pedido ha sido enviado.")