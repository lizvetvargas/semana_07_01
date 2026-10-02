# CORRECTO: Separamos la estructura del reporte de la lógica de guardado
class Reporte:
    def __init__(self, contenido):
        self.contenido = contenido

class GuardadorReporte:
    def guardar(self, reporte: Reporte, ruta: str):
        with open(ruta, "w") as f:
            f.write(reporte.contenido)


#Programa principal
contenido= input("escribe el contenido de tu reporte")

reporte = Reporte(contenido)

ruta = input("¿Como quieres llamar a tu reporte?")

guardador = GuardadorReporte()
guardador.guardar(reporte, ruta)

print("reporte guardado correctamente")