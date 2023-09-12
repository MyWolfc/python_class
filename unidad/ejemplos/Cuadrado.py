from Color import Color
from Figura import Figura

class Cuadrado(Color,Figura):
    def __init__(self, color,lado) -> None:
        Figura.__init__(self,lado,lado)
        Color.__init__(self,color)


    def CalcularArea(self):
        return self._largo*self._ancho

    def __str__(self) -> str:
        return f"{Figura.__str__(self)} {Color.__str__(self)} Area: {self.CalcularArea()}"

    

Cuadrado1 = Cuadrado("Rojo",4)
print(Cuadrado1)