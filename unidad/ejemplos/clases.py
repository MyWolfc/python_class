class Epico:
    def __init__(self,ancho,largo) -> None:
        self._ancho = ancho
        self._largo = largo
        #decorador

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self,ancho):
        self._ancho=ancho

    def CalcularArea(self):
        return self._ancho*self._largo


Ep = Epico(10,20)
print(Ep._ancho)
print(Ep.CalcularArea())
