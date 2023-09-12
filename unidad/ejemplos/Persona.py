class Persona:
    def __init__(self,nombre,edad) -> None:
        self._nombre = nombre
        self._edad = edad

    def __str__(self) -> str:
        return f"Nombre {self._nombre} edad {self._edad}"

P1 = Persona("Juan",22)
print(P1.__str__())