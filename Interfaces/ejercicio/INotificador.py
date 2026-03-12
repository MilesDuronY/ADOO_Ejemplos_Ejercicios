# 1. Creamos la abstracción (Interfaz)
from abc import ABC, abstractmethod
# - INotificador

class INotificador(ABC):
    @abstractmethod
    def enviar(self, mensaje:str):pass


# 2. Implementaciones concretas
# - NotificadorEmail
# - NotificadorSMS
class NotificadorEmail(INotificador):
    def enviar(self, mensaje:str):
        print('Enviando Email: '+mensaje)
class NotificadorSMS(INotificador):
    def enviar(self, mensaje:str):
        print('Enviando SMS: '+mensaje)
# 3. Nueva funcionalida
# - NotificadorWhatsApp
class NotificadorWhatsApp(INotificador):
    def enviar(self, mensaje:str):
        print('Enviando WhatsApp: '+mensaje)
class GestorNotificaciones:
    def __init__(self, notificador: INotificador):
        self.notificador = notificador

    def notificar_usuario(self, mensaje: str):
        self.notificador.enviar(mensaje)


# Uso
gestor = GestorNotificaciones(NotificadorWhatsApp())
gestor.notificar_usuario("Hola, tu pedido ha sido enviado.")
# Resultado : Enviando WhatsApp: Hola, tu pedido ha sido enviado.