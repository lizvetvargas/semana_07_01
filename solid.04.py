# CORRECTO: Dividimos en interfaces independientes usando clases abstractas

from abc import ABC, abstractmethod


class Impresora(ABC):

    @abstractmethod
    def imprimir(self):
        pass


class Escaner(ABC):

    @abstractmethod
    def escanear(self):
        pass


class ImpresoraSencilla(Impresora):

    def imprimir(self):
        print("Imprimiendo documento...")


# Programa principal

impresora = ImpresoraSencilla()

impresora.imprimir()