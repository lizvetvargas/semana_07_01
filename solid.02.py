# CORRECTO: Usamos clases. Para un nuevo cliente, creamos una clase nueva sin tocar las anteriores
class Descuento:
    def aplicar(self, precio):
        return precio

class DescuentoVIP(Descuento):
    def aplicar(self, precio):
        return precio * 0.8

class DescuentoEstudiante(Descuento):
    def aplicar(self, precio):
        return precio * 0.9

class DescuentoNuevoEstudiante(Descuento):
    def aplicar(self, precio):
        return precio * 0.10


# Programa principal____
precio = float(input("Ingresa el precio del producto: "))

print("\nTipos de descuento:")
print("1. Cliente normal")
print("2. Cliente VIP")
print("3. Estudiante")
print("4. Nuevo estudiante")

opcion = input("Elige una opción: ")

if opcion == "1":
    descuento = Descuento()
elif opcion == "2":
    descuento = DescuentoVIP()
elif opcion == "3":
    descuento = DescuentoEstudiante()
elif opcion == "4":
    descuento = DescuentoNuevoEstudiante()
else:
    print("Opción no válida")
    exit()

precio_final = descuento.aplicar(precio)

print(f"\nPrecio original: S/ {precio:.2f}")
print(f"Precio final: S/ {precio_final:.2f}")