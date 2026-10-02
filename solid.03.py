# CORRECTO: Reorganizamos la jerarquía para que cada clase cumpla lo que promete

class Ave:
    pass


class AveVoladora(Ave):
    def volar(self):
        return "Volando..."


class Pinguino(Ave):
    def nadar(self):
        return "Nadando..."


# Programa principal

ave = AveVoladora()
pinguino = Pinguino()

print("Ave voladora:")
print(ave.volar())

print("\nPingüino:")
print(pinguino.nadar())