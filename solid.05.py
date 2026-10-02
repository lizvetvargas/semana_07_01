# CORRECTO: Notificador depende de una abstracción (ServicioMensaje)

from abc import ABC, abstractmethod


class ServicioMensaje(ABC):

    @abstractmethod
    def enviar(self, msg):
        pass


class ServicioSMS(ServicioMensaje):

    def enviar(self, msg):
        print(f"SMS: {msg}")


class ServicioEmail(ServicioMensaje):

    def enviar(self, msg):
        print(f"Email: {msg}")


class Notificador:

    def __init__(self, servicio: ServicioMensaje):  # Inyección de dependencia
        self.servicio = servicio

    def enviar_alerta(self, msg):
        self.servicio.enviar(msg)


# Programa principal

sms = ServicioSMS()
notificador_sms = Notificador(sms)

notificador_sms.enviar_alerta("Su cita ha sido confirmada.")


email = ServicioEmail()
notificador_email = Notificador(email)

notificador_email.enviar_alerta("Tiene una nueva notificación.")