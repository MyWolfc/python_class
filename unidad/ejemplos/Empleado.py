from Persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad,sueldo) -> None:
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    def __str__(self)->str:
        return f"{super().__str__()} sueldo: {self._sueldo}"


miEMP = Empleado("pedro",22,3000)
print(miEMP)